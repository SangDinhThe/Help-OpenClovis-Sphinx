SAFplus Hardware Management
===========================
SAFplus can be integrated with an ATCA chassis manager via an additional product called the SAFplus Platform Support Package.

However, for non-ATCA systems, SAFplus provides some simple APIs to allow your custom hardware manager to report errors to the AMF. 
If your hardware manager can report a sensor error such as a severe overtemperature event to the AMF, this will allow the AMF to 
transition AIS (software) services onto a redundant blade before a failure actually occurs.

AMF Hardware Manager API
------------------------
The AMF API is located in the header file "clCmIpi.h", and implementation in the libmw.a library. This API is only available to 
SAF-aware applications that have successfully initialized AMF services (via the saAmfInitialize API). The following events can be 
communicated to the AMF:

* **CL_CM_BLADE_SURPRISE_EXTRACTION:** 
  The node was abruptly removed
* **CL_CM_BLADE_REQ_EXTRACTION:** 
  The node's power button was pushed or latch was opened -- extraction is imminent.
* **CL_CM_BLADE_REQ_INSERTION:** 
  The node's latch was closed
* **CL_CM_BLADE_NODE_ERROR_REPORT:** 
  Your software has determined (via a sensor read) that failure is imminent. Software applications should be transitioned away from 
  this node.
* **CL_CM_BLADE_NODE_ERROR_CLEAR:** 
  The node has returned to nominal behavior, software applications may be returned to this node.

This event type is combined with information identifying the FRU (node) that has the problem:

.. code-block:: c

    typedef struct {

        /** The event (described above) */
        ClCmCpmMsgTypeT cmCpmMsgType;
        /** The slot number (node identifier) with the problem */
        ClUint32T physicalSlot;
        /** For future use */
        ClUint32T subSlot ;
        /** Not to be used by AMF, can be used by the hardware manager to identify the problem */ 
        ClUint32T resourceId;
    } ClCmCpmMsgT;

And passed to the AMF via a simple API:

.. code-block:: c

    extern ClRcT clCpmHotSwapEventHandle(ClCmCpmMsgT *pCmCpmMsg);

The AMF will use this information to move software applications on nodes with no issues to standby nodes, or to transition 
applications back to nodes that have returned to a nominal state.

AMF Hardware Manager API Example
--------------------------------
The following routine generates a node error report or error clear based on the passed "asserted" variable.

.. code-block:: c

    void clCmInformAMFBySlot(ClUint32T slotId, ClBoolT asserted) {

        ClRcT rc = CL_OK;
        ClCmCpmMsgT cmCpmMsg;
        const ClCharT *msg;
        
        memset(&cmCpmMsg, 0, sizeof(ClCmCpmMsgT));
        cmCpmMsg.physicalSlot = slotId;
        
        if (asserted)
        {
            cmCpmMsg.cmCpmMsgType = CL_CM_BLADE_NODE_ERROR_REPORT;
            msg = "(imminent) failure";
        }
        else
        {
            cmCpmMsg.cmCpmMsgType = CL_CM_BLADE_NODE_ERROR_CLEAR;
            msg = "recovery";
        }
        rc = clCpmHotSwapEventHandle(&cmCpmMsg);
        if (CL_OK != rc)
        {
            clLog(CL_LOG_ERROR, AREA_HPI, CTX_EVT,
                    "Failed to notify AMF about [%s] of slot [%d]", msg, slotId);
            return;
        }
        clLog(CL_LOG_INFO, AREA_HPI, CTX_EVT, "Notified AMF about [%s] of slot [%d]", msg, slotId);
    }



