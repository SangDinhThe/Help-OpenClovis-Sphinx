High Availability (AMF)
=======================

Overview
--------

OpenClovis ASP provides a SA-Forum compliant High Availability solution (the AMF in SAF terminology). This component controls the 
starting/stopping of applications, application redundancy configuration, and role assignment.

FAQ
---

How to get the IOC address for the given node?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The relevant API is "clCpmIocAddressForNodeGet" in "clCpmExtApi.h".

What's the best way for an application to determine the name/slot of the currently active controller in the cluster?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The relevant API is "clCpmMasterAddressGet". Example code (which also converts the node's address into its name) is as follows:

.. code-block:: c

    #include <clCpmExtApi.h>
    ClRcT masterNodeGet(void)
    {
        ClIocNodeAddressT node = 0;
        ClRcT rc = clCpmMasterAddressGet(&node);
        if(node)
        {
            ClCpmSlotInfoT slotInfo = {.slotId = node } ;
            rc = clCpmSlotGet(CL_CPM_SLOT_ID, &slotInfo);
            if(rc == CL_OK)
                clLogNotice("MASTER", "GET", " Currently active controller node name is [%.*s]",
                            slotInfo.nodeName.length, slotInfo.nodeName.value);
        }
        return rc;
    }

How does component recovery and escalation work ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If your recovery is component restart and your component is marked as restartable, and it restarts sgconfig.compRestartCountMax 
within sgconfig.compRestartDuration, then it escalates to SU restart. If the SU restart happens sgconfig.surestartcountmax within 
sgconfig.surestartduration, then it escalates to SU failover. If SU is not marked as restartable, then it escalates to SU failover. 
If the SU failover happens nodeconfig.sufailovercountmax within nodeconfig.sufailoverduration, then it escalates to node failover. 
If the nodeconfig.autorepair is set to TRUE (default), the node is rebooted on node recovery escalations. Also if a component cleanup 
action fails which typically happens when the configured component cleanup script fails when run on abnormal process exits/crashes, 
the recovery is escalated to node failover if the compconfig.nodeRebootCleanupFail is set to TRUE (default). The node reboot behavior 
on escalation/recovery can be controlled by exporting the following environment variables in your MODEL/target.env location thats 
automatically copied to etc/asp.conf while building the target images with make images.

.. code-block:: bash

    export ASP_NODE_REBOOT_DISABLE=1

The above flag would disable reboot of nodes. If the user wants to restart the middleware or ASP on node recovery, then he could:

.. code-block:: bash

    export ASP_NODE_RESTART=1

What is the purpose of each timeout, what happen after the timeout expires?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **instantiateTimeout**
  
  The component has to respond to AMF instantiation request with saAmfResponse within this time. Otherwise on timeout, amf would kill 
  it and try to relaunch it compConfig.numMaxInstantiate times after which it would try to launch it compConfig.numMaxInstantiate 
  times after compConfig.instantiationDelay. If they fail or timeout, the component is marked INSTANTIATION-FAILED. Recovery from 
  INSTANTIATION-FAILED is intended to happen by operator intervention through an "amfRepaired" operation, accessible via API or 
  debug CLI.

* **terminateTimeout**
  
  If the component doesn't respond to the appterminate request from AMF within the terminate timeout, it would be marked 
  termination-failed and component cleanup would be issued. (abrupt termination or SIGKILL sent with configured compCleanupScript 
  invocation)

* **cleanupTimeout**
  
  If component cleanup times out which usually happens when the configured component cleanup script takes more than cleanupTimeout 
  to return during component cleanup trigger and compConfig.nodeRebootCleanupFail is set to TRUE, then node is reset/rebooted 
  (based on env flags in etc/asp.conf. Default is reboot). Otherwise if its false, then SU is failed over on cleanup error.

* **amStartTimeout/amStopTimeout**
  
  Nothing happens on monitoring these timeouts as its not present and processes can use amf healthcheck with recommended recovery.

* **quiescingCompleteTimeout**
  
  When the component doesn't respond with saAmfQuiescingComplete within the quiescingcompletetimeout for a component CSI QUIESCING 
  set request, then its configured recovery takes effect.

* **csiSetTimeout**
  
  Same as above. If the process doesn't respond with saAmfResponse for a csi set request (ACTIVE/STANDBY or QUIESCED), then 
  component recommended recovery takes place.

* **csiRemoveTimeout**
  
  Same. If the process doesn't respond with saAmfResponse to the amf csiRemove request, then recovery is triggered.

* **proxiedCompInstantiateTimeout**
  
  This is only true for SAF-proxy-proxied components. If the SA-AWARE proxy doesn't respond with saAmfResponse to the 
  proxiedCompInstantiate request or proxied-non-preinstantiable doesn't respond to the proxied csiset request (BOTH requests sent 
  to the PROXY component) with saAmfResponse within the proxied instantiate timeout, then recovery is triggered for the proxied.

* **proxiedCompCleanupTimeout**
  
  Again only true for proxy-proxied. If the proxy component doesn't respond to the proxied cleanup callback with saAmfResponse, 
  then a cleanup error for the proxied is processed which is the same as cleanup error for cleanup timeout mentioned above. Either 
  nodeReset if nodeRebootCleanupFail is configured for the component or recovery to SU failover (proxied compcleanup is triggered 
  when proxied component is failed by proxy or fails healthcheck from proxy and proxy returns failure with saAmfResponse or times 
  out the healthcheck for its proxied component which proxy is managing).

How to do a graceful switchover?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A 'graceful' switchover is one where the running applications have a chance to finish ongoing work before the "active" designation is 
moved to another instance of the applications.

Graceful switchover must be implemented in your application by handling the SAF "SA_AMF_HA_QUIESCING" flag in the work assignment 
callback. This callback must initiate the clean up process. When you application is done, it should call 
"saAmfCSIQuiescingComplete(amfHandle, invocation, SA_AIS_OK);" to tell the AMF that it has finished.

To trigger a graceful switchover, you can call clAmsMgmtEntityShutdown, or clCpmNodeRestart from any application, or from the ASP 
debug CLI (within CPM context -- setc master; setc cpm) you can initiate a graceful shutdown by doing "amslockassignment <entity 
type> <entity name>". Then run "amsunlock <entity type> <entity name>" to bring the entity back into service (as standby). For 
example, to effect switchover of the node named "controller1" use "amslockassignment node controller1".
