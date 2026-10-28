.. _comp-debug-label:

Debugging Applications and SAFplus Platform Components
======================================================
The high availability features of the SAFplus Platform interfere with debugging applications because the act of debugging an 
application breaks the performance and availability "contract" between the SAFplus Platform and an application and therefore causes 
the SAFplus Platform to restart the application.

This HOWTO describes strategies that can be used to debug within an high availability environment. It is not a primer on gdb. In fact, 
it assumes an in-depth knowledge of debugging using gdb (or gdb derivatives such as Wind River's IDE) and therefore focuses exclusively 
on the interactions between the debugger and the SAFplus Platform.

It is useful to toggle the following debugging interventions on an as needed basis since many "defeat" the high availability features 
of the SAFplus Platform. Therefore the examples below use a global variable (that you could define in your component's clCompAppMain.c) 
called debuggingOn to control some features.

.. code-block:: c

    int debuggingOn = 1; /* Set to 0 to turn debugging off, 1 to turn it on */

Debugging Configuration Settings
--------------------------------
To aid in debugging, options exist to "defeat" the normal SAFplus monitoring of processes and threads. The following settings are 
accessible either via global or environment variables. The global variable can be used to initiate debugging behavior some time during 
the execution of your process. The environment variable will cause debugging behavior across the entire SAFplus model. These variables 
are all "FALSE" (not in debug mode) by default, setting to TRUE will enable their effects. In the following list, the global variable 
is first and the environment variable is in parenthesis.

* **clDbgPauseOn (CL_DEBUG_PAUSE)**

  If a thread is going to abort or assert, SAFplus can cause the thread to block on a semaphore instead. This allows the engineer to 
  attach to the process via gdb and look at the thread's state.

* **clDbgPauseOnCodeError (CL_DEBUG_PAUSE_CODE_ERROR)**

  If clDbgPauseOn is TRUE, then this variable enables "pauses" on errors that are clearly application bugs -- such as passing a NULL 
  pointer to a SAFplus API. Normally, SAFplus API calls return an error in these cases. But realistically, an application's error 
  handling code can rarely solve bugs in itself -- other then via very granular solutions such as running with reduced functionality 
  or by exiting gracefully. By pausing at the moment the bug is detected, the stack remains available for analysis through gdb.

* **clDbgNoKillComponents (CL_DEBUG_COMP_NO_KILL)**

  This global variable exists in the AMF server and your component. If the AMF was going to kill a component for any reason, or a 
  SAFplus library is going to assert for issues like thread pool timeouts, it will not do so with this variable set to TRUE. This 
  allows the developer to attach to it via gdb. However, note that the AMF or application will continue as if it had actually killed 
  the component and so proper AMF (application) operation after the event is not guaranteed. For this reason, other ways to avoid 
  common cases where the AMF kills a component are discussed in the next sections.

* **clDbgCompTimeoutOverride (CL_DEBUG_COMP_TIMEOUT_OVERRIDE)**

  This global variable exists in the AMF server. If the AMF was going to kill a component due to a timeout, it will not do so. This 
  allows the developer to attach to it via gdb. However, note that the AMF will continue as if it had actually killed the component 
  and so proper AMF operation after the event is not guaranteed. For this reason, other ways to avoid component timeouts are discussed 
  in the next few sections.

Stopping Process Health Monitoring
----------------------------------
It is extremely irritating to attach to your process via a debugger only to have the SAFplus's high availability features intervene 
and kill the process you are trying to debug! Certain techniques can be used to temporarily "defeat" this feature to allow debugging 
to occur. Of course, while the feature is "off" the high availability features do not work.

Turning off heartbeat
^^^^^^^^^^^^^^^^^^^^^
Use ``saAmfHealthcheckStop()`` to stop heartbeat, or do not call ``saAmfHealthcheckStart()`` to begin with. 

.. seealso::
    AMF heartbeating is discussed in detail in the **SAF AMF Specification**

"ACK"ing Messages Early
-----------------------
The SAFplus Platform also monitors the response of certain crucial messages to your component. If your component does not respond in 
time, the SAFplus Platform kills your component. This feature ensures that your application does not have a bug in the handling of 
these messages; however when debugging the message handling we must "defeat" this feature. The most common messages are the CSI (work) 
assignment messages, which trigger the ``clCompAppAMFCSISet`` (clCompAppMain.c) function call. When debugging your component, it is best 
to "ACK" the message right away so the SAFplus Platform will think that you have handled the message. However, it is important to NOT 
do so when not in debugging mode, to ensure that the HA features work.

In the routine below, note that the "clCpmResponse(cpmHandle, invocation, CL_OK);" function has been moved above the switch statement 
when debugging is on (and moved to below it, for succinctness, when debugging is off).

.. code-block:: c

    ClRcT clCompAppAMFCSISet(
        ClInvocationT       invocation,
        const ClNameT       *compName,
        ClAmsHAStateT       haState,
        ClAmsCSIDescriptorT csiDescriptor)
    { 
        /* If component hang detection is off, then reply with an OK first, 
        so that this call won't time out causing the controller to kill me. 
        "debuggingOn" is NOT part of SAFplus.  It is a global variable that 
        you could define in your own application to control this behavior. 
        */
        if (debuggingOn)
        {
            if (haState != CL_AMS_HA_STATE_QUIESCING)
            clCpmResponse(cpmHandle, invocation, CL_OK);
        }
    
        /* DO NOT SET BREAKPOINTS ABOVE THIS LINE (IN THIS FUNCTION)
    
        (the controller will think that your process is dead)
    
        To set a breakpoint in this routine:
    
        1. First set "debuggingOn" to 1
        2. Set your breakpoint below this comment
        3. Continue
        */  
    
    
        /* Print information about the CSI Set */
        clprintf ("Component [%s] : PID [%d]. CSI Set Received\n", 
                compName->value, mypid);
        clCompAppAMFPrintCSI(csiDescriptor, haState);
    
    
        /* Take appropriate action based on state */
        switch ( haState )
        {
            case CL_AMS_HA_STATE_ACTIVE:
            {
                /*
                AMF has requested application to take the active HA state 
                for the CSI.
                */
                break;
            }
            case CL_AMS_HA_STATE_STANDBY:
            {
                /*
                AMF has requested application to take the standby HA state 
                for this CSI.
                */
                break;
            }
            case CL_AMS_HA_STATE_QUIESCED:
            {
                /*
                AMF has requested application to quiesce the CSI currently
                assigned the active or quiescing HA state. The application 
                must stop work associated with the CSI immediately.
                */
                break;
            }
            case CL_AMS_HA_STATE_QUIESCING:
            {
                /*
                AMF has requested application to quiesce the CSI currently
                assigned the active HA state. The application must stop work
                associated with the CSI gracefully and not accept any new
                workloads while the work is being terminated.
                */
                clCpmCSIQuiescingComplete(cpmHandle, invocation, CL_OK);
                break;
            }
            default:
            {
                /*
                Should never happen. Ignore.
                */
            }
        }
    
        /* If I'm am killing components, then reply with an OK after
        execution, to ensure that the handling did not hang */
        if (!debuggingOn)
        {
            if (haState != CL_AMS_HA_STATE_QUIESCING)
            clCpmResponse(cpmHandle, invocation, CL_OK);
        }
        return CL_OK;
    }

Component State Transition Timeouts
-----------------------------------
The SAFplus Platform also ensures that your component transitions through various states within reasonable a time. To debug during 
these transitions (startup, shutdown, etc) it is necessary to increase these timeouts. These timeouts are available in the IDE, or 
directly in the XML configuration files for temporary changes.

Search for the following XML in your **etc/clAmfDefinitions.xml** file and change the numbers for every component you need to debug to 
large values.

.. code-block:: mxml

    <timeouts>
        <instantiateTimeout>1000000</instantiateTimeout>
        <terminateTimeout>1000000</terminateTimeout>
        <cleanupTimeout>1000000</cleanupTimeout>
        <amStartTimeout>1000000</amStartTimeout>
        <amStopTimeout>1000000</amStopTimeout>
        <quiescingCompleteTimeout>1000000</quiescingCompleteTimeout>
        <csiSetTimeout>1000000</csiSetTimeout>
        <csiRemoveTimeout>1000000</csiRemoveTimeout>
        <proxiedCompInstantiateTimeout>1000000</proxiedCompInstantiateTimeout>
        <proxiedCompCleanupTimeout>1000000</proxiedCompCleanupTimeout>
    </timeouts>

Creating core files on failure
------------------------------
Core files are configured to be automatically created and will be found int the "var/run" directory. If core files are not being 
created, your environment configuration may be overriding our changes.

Make sure the core file size is "unlimited" by running "ulimit -c unlimited" before executing SAFplus.

You can test core creation by jamming a SEGFAULT into a program by doing

.. code-block:: text

    kill -SEGV <process id>

Pausing and Resuming a Thread
-----------------------------
Sometimes a problem occurs during startup -- before you have the opportunity to attach to a process, set a breakpoint, and resume the 
process. In a standard application this is easy to debug because "gdb" starts up with your program "stopped". But in a high availability 
framework, where the SAFplus Platform starts and stops programs, this is trickier.

To debug this, 2 functions are available from **clDebugApi.h,** one which "pauses" the calling thread, the other "resumes" it. The 
programmer adds the "pause" function to the code and recompiles. When the function is called and the global variable ``clDbgPauseOn`` (or 
``CL_DEBUG_PAUSE`` environment variable) is true, the thread will output a log and block on a semaphore. The programmer can then check the 
logs to see if a thread was paused. If so, he goes into gdb, attaches to the process, finds the thread that is paused -- "thread apply 
all backtrace" ("thr a a bt") and look for a call to "pause" -- switches to that thread ("thread x"), and then debugs the thread. The 
programmer can even "resume" the thread by calling the ``clDbgResume`` function from gdb's prompt:

.. code-block:: text

    gdb> call clDbgResume()

The "pause" function is actually a macro so that the file and line from which the function was called can be passed. This information 
is very useful if a log is all that is provided for debugging.

Intercepting the Automatic Start of a Component
-----------------------------------------------
It is possible to run your component within a wrapper application (such as gdb or purify). When the SAFplus Platform is deployed on a 
target, all applications are placed in the "bin" subdirectory of the SAFplus Platform tree (for example "/root/asp/bin"). To intercept 
the application start for debugging purposes:

* rename your application
* create a script and name it the same as the original application name
* edit the script to add your wrapper.

  * Note that you will have to start a separate window for applications that need a console (like gdb)

For example the following simple script can be used to make your application start within gdb (note though that it must be used in 
conjunction with the techniques described in the "Stopping Process Health Monitoring" section above unless you are a very fast typist, 
since your application's initialization will be monitored by the OpenClovis HA infrastructure to ensure that it succeeds). This script 
assumes that your application is called "myapp" and that you moved it to "/root/asp/bin/myapp.orig". It also assumes that your Linux 
installation has X-windows and the gnome desktop environment installed (however, a similar technique can be used for other window 
managers):

.. code-block:: bash

    #!/bin/bash
    /usr/bin/gnome-terminal --window --command "gdb /root/asp/bin/myapp.orig $1 $2 $3 $4 $5 $6 $7 $8 $9"

Useful Environment Variables
----------------------------
* ``ASP_NODE_REBOOT_DISABLE``

Disable reboot of nodes, even if the AMF high availability algorithm determines a reboot is necessary. Example:

.. code-block:: bash
    
    export ASP_NODE_REBOOT_DISABLE=1

* ``CL_LOG_CODE_LOCATION_ENABLE``

Adds file/line to each log message, so logs can be easily found in the source code. Example:

.. code-block:: bash
   
    export CL_LOG_CODE_LOCATION_ENABLE=1

* ``CL_LOG_TO_FILE``

Sends all logs to a file or stdout. This environment variable is very helpful when debugging problems that occur before the SAFplus 
log server has started. For example:

.. code-block:: bash
   
    export CL_LOG_TO_FILE=stdout
    export CL_LOG_TO_FILE=/var/log/mylog.txt
