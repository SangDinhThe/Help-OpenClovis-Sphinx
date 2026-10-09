Dynamic HA Evaluation Guide
===========================

Objective
---------
This sample application demonstrates dynamic HA (High Availability) functionality. The application has two components : dhaDemo and 
dummyComp

* dhaDemo creates/deletes the AMF entities (SG, SI, CSI, SU, Component, etc) dynamically.
* dummyComp is a sample SAF component whose binary(executable) will be used while launching the dynamically created component.

What you will learn
-------------------
How to create a 2N model dynamically by creating/deleting various AMF entities using Clovis AMF management APIs related to Dynamic HA.

Building the dynamic HA model (dynamicHaDemo) and deploying runtime images
--------------------------------------------------------------------------
The Clovis dynamic HA Application is located in : 

.. code-block:: text

    <install_dir>/6.1/sdk/src/examples/dynamicHaDemo

You need to build the model and deploy the runtime images for following nodes : SysCtrlI0, WorkerI0, WorkerI1

It can be done in very similar manner to evaluation system model (eval). For more information about building and deploying a model, 
please refer to the following section of evalguide:

**Building the Evaluation System and Deploying Runtime Images**

Code
----
The application code can be found within the following directory

.. code-block:: text

    <project-area_dir>/dynamicHaDemo/src/app/dhaDemo

This sample component is implemented in a single C module (main.c). It uses the AMF dynamic HA apis to create a 2N SG on the fly 
using the clAmsMgmtCCB apis.

There is an alternate version of this C file: main_batch.c which uses a faster version of these apis using clAmsMgmtCCBBatch apis.

The batch version of the dynamic HA apis are faster as the AMF entity CRUD operatons are batched/cached on the client side before 
they are committed with clAmsMgmtCCBBatchCommit api.

Both the clAmsMgmtCCB and clAmsMgmtCCBBatch version of the APIs are declared in clAmsMgmtClientApi.h which needs to be included for usage.

Start/Stop the application
^^^^^^^^^^^^^^^^^^^^^^^^^^
The safAssignWork() function is called to set the component's HA state, and the following block of code assigns this requested state 
to the component, while verbosely detailing this process:

* clDhaDemoStart() will start the workload in a separate thread to create the AMF entities (SG, SI, CSI, SU, Components, etc) when 
  the HA state of dhaDemo becomes ACTIVE. In this case dhaDemo will be assigned active state when you unlock the SG 'dhaDemoSG'

  .. code-block:: c
    :caption: main.c

    switch ( haState )
    {
        case SA_AMF_HA_ACTIVE:
        {
            /*
             * AMF has requested application to take the active HA state 
             * for the CSI.
             */

            /*
             * ---BEGIN_APPLICATION_CODE---
             */
            clprintf(CL_LOG_SEV_NOTICE, "Starting dynamic HA demo.");
            clprintf(CL_LOG_SEV_NOTICE, "It will create 2N SG : %sSG", BASE_NAME);
            rc = clDhaDemoStart();
            if(rc != CL_OK)
            {
                clprintf(CL_LOG_SEV_CRITICAL, "Failed to start dynamic HA demo.");
            }

            /*
             * ---End_APPLICATION_CODE---
             */

            saAmfResponse(amfHandle, invocation, SA_AIS_OK);
            break;
        }

* clDhaDemoStop() will start the workload in a separate thread to delete the AMF entities (SG, SI, CSI, SU, Components, etc) only 
  if they are already created, when the HA state of dhaDemo becomes QUIESCED or QUIESCING. In this case dhaDemo will be get QUIESCED 
  state when you lock the unlocked SG 'dhaDemoSG'

  .. code-block:: c
    :caption: main.c

        case SA_AMF_HA_QUIESCED:
        {
            /*
             * AMF has requested application to quiesce the CSI currently
             * assigned the active or quiescing HA state. The application 
             * must stop work associated with the CSI immediately.
             */

            /*
             * ---BEGIN_APPLICATION_CODE---
             */

            rc = clDhaDemoStop();
            if(rc != CL_OK)
            {
                clprintf(CL_LOG_SEV_CRITICAL, "Failed to stop dynamic HA demo.");
            }

            /*
             * ---END_APPLICATION_CODE---
             */

            saAmfResponse(amfHandle, invocation, SA_AIS_OK);
            break;
        }

Create/Delete the AMF entities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
clDhaDemoCreate() contains the code to create various AMF entities dynamically:

.. code-block:: c
    :caption: main.c

    rc = clAmsMgmtInitialize(&mgmtHandle, NULL, &version);
    if(rc != CL_OK)
    {
        clprintf(CL_LOG_SEV_ERROR, "AmsMgmt initialize returned [%#x]", rc);
        return NULL;
    }

    clDhaExmpExec(("Running MGMT CCB initialize"),
                  (rc = clAmsMgmtCCBInitialize(mgmtHandle, &ccbHandle)) == CL_OK,
                  ("MGMT CCB initialize returned [%#x]", rc),
                  goto out1);

    /*                                                                                                                                                               
     * Create the entities only if they are not created already                                                                                                      
     */
    entity.type = CL_AMS_ENTITY_TYPE_SG;
    snprintf(entity.name.value, sizeof(entity.name.value), "%sSG", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;

    rc = clAmsMgmtEntityGetConfig(mgmtHandle,
                                  &entity,
                                  &pEntityConfig);

    clHeapFree(pEntityConfig);

    if(rc == CL_OK)
    {
        clprintf(CL_LOG_SEV_INFO, "Not creating SG[%sSG], it already exist", pBaseName);
		goto out2;
    }

    /* SG doesn't exist, create SG and other entities dynamically*/

    /*First create the service hierarchies*/

    clprintf(CL_LOG_SEV_NOTICE,
             "Creating 2N SG [%sSG] and other entities(si, csi, su, comp, etc)",
             pBaseName);

    /* Create SG*/
    entity.type = CL_AMS_ENTITY_TYPE_SG;
    snprintf(entity.name.value, sizeof(entity.name.value),
             "%sSG", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;

    clDhaExmpExec(("Creating SG [%s]",
                   entity.name.value),
                  (rc = clAmsMgmtCCBEntityCreate(ccbHandle,
                                                 &entity)) == CL_OK,
                  ("SG create returned [%#x]", rc),
                  goto out2);

    /* Create SI*/
    entity.type = CL_AMS_ENTITY_TYPE_SI;
    snprintf(entity.name.value, sizeof(entity.name.value),
             "%sSI", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;
    clDhaExmpExec( ("Create SI [%s]", entity.name.value),
                   (rc = clAmsMgmtCCBEntityCreate(ccbHandle, &entity)) == CL_OK,
                   ("SI create returned [%#x]", rc),
                   goto out2);

    ...
    ...
    ...

    /* CCB Commit*/
    clDhaExmpExec(("CCB Commit Create"),
                  (rc = clAmsMgmtCCBCommit(ccbHandle)) == CL_OK,
                  ("CCB commit returned [%#x]", rc),
                  goto out2);

    ...
    ...

clDhaDemoDelete() contains the code to delete the created AMF entities dynamically:

.. code-block:: c
    :caption: main.c

    rc = clAmsMgmtInitialize(&mgmtHandle, NULL, &version);
    if(rc != CL_OK)
    {
        clprintf(CL_LOG_SEV_ERROR, "AmsMgmt initialize returned [%#x]", rc);
		return NULL;
    }

    clDhaExmpExec(("Running MGMT CCB initialize"),
                  (rc = clAmsMgmtCCBInitialize(mgmtHandle, &ccbHandle)) == CL_OK,
                  ("MGMT CCB initialize returned [%#x]", rc),
                  goto out1);


    /*                                                                                                                                                               
     * Delete the entities only if they exist                                                                                                                        
     */
    entity.type = CL_AMS_ENTITY_TYPE_SG;
    snprintf(entity.name.value, sizeof(entity.name.value), "%sSG", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;

    rc = clAmsMgmtEntityGetConfig(mgmtHandle,
                                  &entity,
                                  &pEntityConfig);
    clHeapFree(pEntityConfig);
    if(rc != CL_OK)
    {
        clprintf(CL_LOG_SEV_INFO, "Not deleting SG[%sSG],  SG config get returned [%#x]", pBaseName, rc);
        goto out2;

    }

    /* SG exist, Delete SG and other entities dynamically*/

    clprintf(CL_LOG_SEV_NOTICE,
             "Deleting SG [%sSG] and other entities(si, csi, su, comp, etc)",
             pBaseName);

    /*First move entities to lock instantiated mode*/
    clDhaExmpExec(("LockI AMS entities"),
                  (rc = clAmsMgmtTestLockI(mgmtHandle, ccbHandle, pBaseName)) == CL_OK,
                  ("Unlock AMS entities returned [%#x]", rc),
                  goto out2);

    ...
    ...

    /* Delete SI*/
    entity.type = CL_AMS_ENTITY_TYPE_SI;
    snprintf(entity.name.value, sizeof(entity.name.value),
             "%sSI", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;
    clDhaExmpExec( ("Delete SI [%s]", entity.name.value),
                   (rc = clAmsMgmtCCBEntityDelete(ccbHandle, &entity)) == CL_OK,
                   ("SI delete returned [%#x]", rc),
                   goto out2);

    /* Delete SG*/
    entity.type = CL_AMS_ENTITY_TYPE_SG;
    snprintf(entity.name.value, sizeof(entity.name.value),
             "%sSG", pBaseName);
    entity.name.length = strlen(entity.name.value)+1;
    clDhaExmpExec(("Deleting SG [%s]",
                   entity.name.value),
                  (rc = clAmsMgmtCCBEntityDelete(ccbHandle,
                                                 &entity)) == CL_OK,
                  ("SG delete returned [%#x]", rc),
                  goto out2);

    /* CCB Commit*/
    clDhaExmpExec(("CCB Commit Delete"),
                  (rc = clAmsMgmtCCBCommit(ccbHandle)) == CL_OK,
                  ("CCB commit returned [%#x]", rc),
                  goto out2);

    ...
    ...

Usage of AMF management APIs for Dynamic HA
-------------------------------------------
The detailed documentation of AMF management APIs can be found in **"OpenClovis API Reference Guide"**. Please refer **"Availability 
Management Service"** section under the High Availability.

How to Run dhaDemo application and What to Observe
--------------------------------------------------
We will use the SAFplus Platform Console to manipulate the administrative state of the dhaDemoSG service group.

Start the SAFplus Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^
Start the SAFplus Platform on all deployed nodes

.. code-block:: console

    # cd /root/asp/
    # ./etc/init.d/asp start

Start the console
^^^^^^^^^^^^^^^^^
Start the SAFplus Platform Console

.. code-block:: console

    # cd /root/asp/bin
    # ./asp_console

Lock assignment dhaDemoSG
^^^^^^^^^^^^^^^^^^^^^^^^^
Then put the dhaDemoSG service group into lock assignment state using the following commands:

.. code-block:: console

    # cli[Test]-> setc master
    # cli[Test:SysCtrlI0]-> setc cpm
    # cli[Test:SysCtrlI0:CPM]->  amsLockAssignment sg dhaDemoSG

The logs for dhaDemo application will be logged into file **/root/asp/var/log/app.0** on node **WorkerI0**. Viewing these application logs 
using the tail -f, you should see the following:

.. code-block:: text
    :caption: /root/asp/var/log/app.0

    Wed Sep  3 16:03:02 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00031 :   INFO) Component [dhaDemo] : PID [21785]. Initializing

    Wed Sep  3 16:03:02 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00032 :   INFO)    IOC Address             : 0x3

    Wed Sep  3 16:03:02 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00033 :   INFO)

Create the AMF entities
^^^^^^^^^^^^^^^^^^^^^^^
To create the AMF entities dynamically, unlock the dhaDemoSG service group using the following SAFplus Platform Console command.

.. code-block:: text

    # cli[Test:SysCtrlI0:CPM]->  amsUnlock sg dhaDemoSG

and in the **/root/asp/var/log/app.0** file (on node **WorkerI0**) , we should see:

.. code-block:: text
    :caption: /root/asp/var/log/app.0

    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00036 :   INFO) Component [dhaDemo] : PID [21785]. CSI Set Received

    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00037 :   INFO) CSI Flags : [Add One]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00038 :   INFO) CSI Name : [dhaDemoCSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00039 :   INFO) Name value pairs :
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00040 :   INFO) HA state : [Active]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00041 :   INFO) Active Descriptor :
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00042 :   INFO) Transition Descriptor : [1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00043 :   INFO) Active Component : [dhaDemo]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00044 : NOTICE) Starting dynamic HA demo.
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00045 : NOTICE) It will create 2N SG : dynamicTwoNSG
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00046 :   INFO) Running MGMT initialize
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00047 :   INFO) Running MGMT CCB initialize
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00048 : NOTICE) Creating 2N SG [dynamicTwoNSG] and other entities(si, csi, su, comp, etc)
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00049 :   INFO) Creating SG [dynamicTwoNSG]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00050 :   INFO) Create SI [dynamicTwoNSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00051 :   INFO) Create CSI [dynamicTwoNCSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00052 :   INFO) Create SU [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00053 :   INFO) Create SU [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00054 :   INFO) Create COMP [dynamicComp0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00055 :   INFO) Create COMP [dynamicComp1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00056 :   INFO) CCB Commit Create
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00057 :   INFO) Fill SG config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00058 :   INFO) SG config get [dynamicTwoNSG]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00059 :   INFO) SG set SI [dynamicTwoNSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00060 :   INFO) SG set SU [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00061 :   INFO) SG set SU [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00062 :   INFO) SG set commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00063 :   INFO) Fill SI config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00064 :   INFO) SI config get [dynamicTwoNSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00065 :   INFO) SI config set [dynamicTwoNSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00066 :   INFO) SI set CSI [dynamicTwoNCSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00067 :   INFO) SI set commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00068 :   INFO) Fill CSI config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00069 :   INFO) CSI config get [dynamicTwoNCSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00070 :   INFO) CSI type set [dynamicTwoNCSIType]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00071 :   INFO) CSI set nvplist
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00072 :   INFO) CSI ccb commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00073 :   INFO) Fill SU config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00074 :   INFO) SU config get [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00075 :   INFO) SU config set [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00076 :   INFO) SU config set [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00077 :   INFO) SU [dynamicTwoNSU0] add comp [dynamicComp0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00078 :   INFO) SU [dynamicTwoNSU1] add comp [dynamicComp1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00079 :   INFO) SU set commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00080 :   INFO) Fill NODE config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00081 :   INFO) NODE config get [WorkerI1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00082 :   INFO) Node set SU [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00083 :   INFO) NODE config get [WorkerI0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00084 :   INFO) Node set SU [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00085 :   INFO) Node set commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00086 :   INFO) Fill COMP config
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00087 :   INFO) COMP config get [dynamicComp0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00088 :   INFO) Comp config set [dynamicComp0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00089 :   INFO) Comp config set [dynamicComp1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00090 :   INFO) Comp set commit
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00091 :   INFO) Unlock AMS entities
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00092 :   INFO) LockA [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00093 :   INFO) Unlock [dynamicTwoNSU0]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00094 :   INFO) LockA [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00095 :   INFO) Unlock [dynamicTwoNSU1]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00096 :   INFO) Unlock SI [dynamicTwoNSI]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00097 :   INFO) LockA SG [dynamicTwoNSG]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00098 :   INFO) Unlock SG [dynamicTwoNSG]
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00099 :   INFO) Running CCB finalize
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.DHA.DMO.00100 :   INFO) Running MGMT finalize
    Wed Sep  3 16:07:33 2008   (WorkerI0.21785 : dhaDemo_EO.---.---.00101 : NOTICE) Successfully created 2N SG [dynamicTwoNSG] and its entities(si, csi, su, comp, etc) dynamically

The dynamically created components 'dynamicComp0' and 'dynamicComp1' will come up as active/standby. Which can be verified through 
the logs present at nodes WorkerI0 and WorkerI1.

In **/root/asp/var/log/app.0** file (on node **WorkerI0**) , we should see the dynamically created component getting assigned ACTIVE state:

.. code-block:: text
    :caption: /root/asp/var/log/app.0

    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00031 :   INFO) Component [dynamicComp0] : PID [22187]. Initializing

    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00032 :   INFO)    IOC Address             : 0x3

    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00033 :   INFO)    IOC Port                : 0x81

    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00036 :   INFO) Component [dynamicComp0] : PID [22187]. CSI Set Received

    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00037 :   INFO) CSI Flags : [Add One]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00038 :   INFO) CSI Name : [dynamicTwoNCSI]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00039 :   INFO) Name value pairs :
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00040 :   INFO) Name : [model]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00041 :   INFO) Value : [twoN]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00042 :   INFO) HA state : [Active]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00043 :   INFO) Active Descriptor :
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00044 :   INFO) Transition Descriptor : [1]
    Wed Sep  3 16:07:43 2008   (WorkerI0.22187 : dummyComp_EO.---.---.00045 :   INFO) Active Component : [dynamicComp0]

In **/root/asp/var/log/app.0** file (on node **WorkerI1**) , we should see the dynamically created component getting assigned STANDBY state:

.. code-block:: text
    :caption: /root/asp/var/log/app.0

    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00031 :   INFO) Component [dynamicComp1] : PID [14623]. Initializing

    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00032 :   INFO)    IOC Address             : 0x4

    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00033 :   INFO)    IOC Port                : 0x80

    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00036 :   INFO) Component [dynamicComp1] : PID [14623]. CSI Set Received

    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00037 :   INFO) CSI Flags : [Add One]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00038 :   INFO) CSI Name : [dynamicTwoNCSI]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00039 :   INFO) Name value pairs :
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00040 :   INFO) Name : [model]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00041 :   INFO) Value : [twoN]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00042 :   INFO) HA state : [Standby]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00043 :   INFO) Standby Descriptor :
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00044 :   INFO) Standby Rank : [1]
    Wed Sep  3 16:07:43 2008   (WorkerI1.23159 : dummyComp_EO.---.---.00045 :   INFO) Active Component : [dynamicComp0]

.. note::
    The dynamically created component might come up as ACTIVE on WorkerI1 and STANDBY on WorkerI0 or vice versa (depending on the 
    order in which they are launched).

Delete the AMF entities
^^^^^^^^^^^^^^^^^^^^^^^
To delete the AMF entities dynamically, lock the dhaDemoSG service group using the following SAFplus Platform Console command:

.. code-block:: text

    # cli[Test:SysCtrlI0:CPM]->  amsLockAssignment sg dhaDemoSG

and in the **/root/asp/var/log/app.0** (on node **WorkerI0**) file, we should see:

.. code-block:: text
    :caption: /root/asp/var/log/app.0

    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00102 :   INFO) Component [dhaDemo] : PID [17193]. CSI Set Received

    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00103 :   INFO) CSI Flags : [Target One]     
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00104 :   INFO) CSI Name : [dhaDemoCSI]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00105 :   INFO) HA state : [Quiesced]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00106 :   INFO) Running MGMT initialize
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00109 :   INFO) Component [dhaDemo] : PID [17193]. CSI Remove Received

    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00110 :   INFO)    CSI                     : dhaDemoCSI

    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00111 :   INFO)    CSI Flags               : 0x2

    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00112 :   INFO) Running MGMT CCB initialize
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00113 : NOTICE) Deleting SG [dynamicTwoNSG] and other entities(si, csi, su, comp, etc)
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00114 :   INFO) LockI AMS entities 
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00115 :   INFO) LockA [dynamicTwoNSU0]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00116 :   INFO) LockI [dynamicTwoNSU0]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00046 :   INFO) Component [dynamicComp0] : PID [17217]. CSI Set Received

    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00047 :   INFO) CSI Flags : [Target One]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00048 :   INFO) CSI Name : [dynamicTwoNCSI]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00049 :   INFO) HA state : [Quiesced]
    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00052 :   INFO) Component [dynamicComp0] : PID [17217]. CSI Remove Received

    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00053 :   INFO)    CSI                     : dynamicTwoNCSI

    Wed Sep  3 16:34:27 2008   (WorkerI0.17217 : dummyComp_EO.---.---.00054 :   INFO)    CSI Flags               : 0x2

    Wed Sep  3 16:34:29 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00117 :   INFO) LockA [dynamicTwoNSU1]
    Wed Sep  3 16:34:29 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00118 :   INFO) LockI [dynamicTwoNSU1]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00119 :   INFO) LockA SI [dynamicTwoNSI]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00120 :   INFO) LockA SG [dynamicTwoNSG]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00121 :   INFO) LockI SG [dynamicTwoNSG]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00122 :   INFO) Delete COMP [dynamicComp0]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00123 :   INFO) Delete COMP [dynamicComp1]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00124 :   INFO) Delete SU [dynamicTwoNSU0]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00125 :   INFO) Delete SU [dynamicTwoNSU1]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00126 :   INFO) Delete CSI [dynamicTwoNCSI]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00127 :   INFO) Delete SI [dynamicTwoNSI]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00128 :   INFO) Deleting SG [dynamicTwoNSG]
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00129 :   INFO) CCB Commit Delete
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00130 :   INFO) Running CCB finalize
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.DHA.DMO.00131 :   INFO) Running MGMT finalize
    Wed Sep  3 16:34:31 2008   (WorkerI0.17193 : dhaDemo_EO.---.---.00132 : NOTICE) Successfully deleted dynamically created SG [dynamicTwoNSG] and other entities(si, csi, su, comp, etc)

.. note::
    These can be watched in a separate terminal window using tail -f <file_name>

Things to do
^^^^^^^^^^^^
You can continue to observe this create/delete of AMF entities dynamically by unlocking/locking the SG dhaDemoSG.

* To unlock the dhaDemoSG using the SAFplus Platform Console (this will create the AMF entities dynamically):

  .. code-block:: text

    # cli[Test:SysCtrlI0:CPM]-> amsUnlock sg dhaDemoSG

* To lock the dhaDemoSG using the SAFplus Platform Console (this will delete the AMF entities dynamically):

  .. code-block:: text

    # cli[Test:SysCtrlI0:CPM]-> amsLockAssignment sg dhaDemoSG

* To stop the demo and exit, following CLI commands may be used:

  .. code-block:: text

    # cli[Test:SysCtrlI0:CPM]-> amsLockAssignment sg dhaDemoSG
    # cli[Test:SysCtrlI0:CPM]-> amsLockInstantiation sg dhaDemoSG
    # cli[Test:SysCtrlI0:CPM]-> bye

Summary
-------
This Sample Application has covered basic dynamic HA functionality, with creation/deletion of AMF entities (SG, SI, CSI, SU, 
Component, etc) using Clovis AMF management APIs.

