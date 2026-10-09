Process Death
=============

FAQ
---

One of my processes is dying. Does ASP ever kill a process?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Yes. As per the SAF spec, all AMF communications are timed. Therefore if your process instantiation time or processing of AMF 
callbacks (CSI assignment) takes too long, then the process may be killed. The process must call saAmfResponse() within a 
configurable time limit (default 30 seconds) or it will be killed. You can check the "sys.latest" log on the active system 
controller to discover whether this is your problem.

Here is a handler for the "active" assignment:

.. code-block:: c

    void CSISetHandler(SaInvocationT invocation,const SaNameT *compName,SaAmfHAStateT haState, SaAmfCSIDescriptorT csiDescriptor)
    {
        switch ( haState )
        {
            case SA_AMF_HA_ACTIVE:  // BAD
                sleep(35);  // This "sleep" is placeholder for your actual routine that runs for 30+ seconds. Since this occurs before the saAmfResponse, it will cause the AMF to think that the process is hung.  The AMF will kill the process.
                saAmfResponse(amfHandle, invocation, SA_AIS_OK);
                break;
            case SA_AMF_HA_ACTIVE:  // BAD
                saAmfResponse(amfHandle, invocation, SA_AIS_OK);
                sleep(35);  // This is monopolising the AMF handler thread.  So if another event comes in just after this one, it will delay the processing of that event, causing the AMF to believe that the process is hung.
                break;
            case SA_AMF_HA_ACTIVE:  // GOOD
            {
                pthread_t thread;
                pthread_create(&thread, NULL, sleep, (void *) 35);  // This a contrived example to start a thread that sleeps for 35 seconds.  You would call your actual routine not sleep!
                saAmfResponse(amfHandle, invocation, SA_AIS_OK);
            }   break;

            /* All other HA states need to be added to this switch, so this is not good template code */
        }
    }

The AMF is killing my process, but my handler looks ok. What else could be wrong?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
It is possible that you are not letting the AMF dispatch handler run. Please make sure that you call saAmfDispatch() periodically. 
Code to do this is automatically generated within the "main" function (in clCompAppMain.c) of your process if you use the IDE code 
generation tool.
