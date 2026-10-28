SAFplus Platform Command Line and Environment Variable Reference
================================================================

Environment Variables
---------------------

Variables controlling automatic restart or reboot of SAFplus Platform or Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``ASP_RESTART_SAFplus`` -- If set to 1 will restart SAFplus Platform in case AMF crashed or SAFplus Platform was not able to come up 
  for some reason, if set to 0 will not restart SAFplus Platform. Default value is 1.
* ``ASP_NODE_REBOOT_DISABLE`` --
* ``ASP_NODE_RESTART`` --

This table describes the interaction between the various SAFplus Platform restart and reboot variables:

+-------------------+-------------+------------------+--------------------------+
| ASP_NODE_REBOOT   | ASP_RESTART | ASP_NODE_RESTART | Action taken             |
+===================+=============+==================+==========================+
| undefined         | undefined   | undefined        | reboot                   |
+-------------------+-------------+------------------+--------------------------+
| 1                 | undefined   | undefined        | Restart SAFplus Platform |
+-------------------+-------------+------------------+--------------------------+
| 1                 | 0           | undefined        | SAFplus Platform stopped |
+-------------------+-------------+------------------+--------------------------+
| 1                 | 0           | 1                | Restart SAFplus Platform |
+-------------------+-------------+------------------+--------------------------+

Cluster Membership Configuration (GMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``CL_LEADER_NODE_ID`` --
* ``LINK_NAME`` -- This tells SAFplus Platform which Network Interface (ex. eth0, bind0, lo, etc.) to be used for communication with 
  other SAFplus Platform's on same/other nodes.
* ``ASP_MULTINODE`` -- This environment variable must be used, when multiple SAFplus Platform's are to be run on single machine. Then 
  user must export this environment variable before starting each of SAFplus Platform's.

ValGrind
^^^^^^^^

* ``ASP_VALGRIND_FILTER`` --
* ``ASP_VALGRIND_CMD`` --

Logging
^^^^^^^

* ``ASP_LOG_FILTER_DIR`` -- place where log filter file should be present. It should be named logfilter.txt. Default value /tmp
* ``CL_LOG_SEVERITY`` -- Environment variable used to set the log filter. You can export this env variable to any log severity like 
  ``DEBUG``, ``INFO``, ``NOTICE``, ``ERROR``, etc. Note that setting of this env variable has higher priority than the log filter file 
  explained above.
* ``CL_LOG_CODE_LOCATION_ENABLE`` -- Environment variable if set to 1, will show the file name, function name and line number when 
  displaying logs. Default value is 0.
* ``CL_LOG_TO_FILE`` -- sends all logs to a file or stdout. Very useful when debugging issues that occur before the SAFplus log server 
  is up

  .. code-block:: bash

    export CL_LOG_TO_FILE=stdout 

* ``CL_LOG_STREAM_ENABLE``
* ``CL_LOG_TIME_ENABLE``
* ``CL_LOG_DEBUG_LEVEL`` (clLogDebug.c)
* ``ASP_SAVE_PREV_LOGS`` -- if set to 1 will save logs in the sandbox from the previous run of SAFplus Platform (if any) during SAFplus 
  Platform startup into location specified by the environment variable ``ASP_PREV_LOG_DIR`` or to /tmp/asp_saved_logs, creating the 
  directory if necessary. If set to 0, the logs will deleted. Default value is 1.
* ``ASP_PREV_LOG_DIR`` -- place where logs of previous SAFplus Platform run will be stored. Default value is /tmp/asp_saved_logs
* ``AMS_DEBUG`` -- Enable special availability management framework console logging. This occurs outside of the normal log infrastructure 
  since the AMF process manages the logging process.
* ``AMS_NOTIFICATION_DEBUG`` --
* ``CPM_LOG_FILE_SIZE`` --
* ``CPM_LOG_FILE_ROTATIONS`` --
* ``ASP_CPM_LOGFILE`` --

Miscellaneous
^^^^^^^^^^^^^

* ``ASP_RMD_METRIC`` --
* ``CL_TXN_DSBLE_CKPT`` --
* ``CL_HEAP_DEBUG`` --
* ``CL_MEM_TIME`` --
* ``ASP_WITHOUT_CPM`` --
* ``CL_NODE_REPRESENTATIVE`` --
* ``ASP_DB_SYNC`` --

Debugging
^^^^^^^^^

* ``CL_DEBUG_PAUSE`` --
* ``CL_DEBUG_PAUSE_CODE_ERROR`` --
* ``CL_DEBUG_COMP_NO_KILL`` --
* ``CL_DEBUG_COMP_TIMEOUT_OVERRIDE`` --
* ``CL_DEBUG_LOG_LEVEL`` --
* ``CL_DEBUG_RESOURCE_LOG_LEVEL`` --
* ``CL_DEBUG_REVERSE_TIMING`` --

Intra-Cluster Message Traffic Shaping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis SAFplus Platform optionally uses a well known traffic shaping algorithm to modulate intracluster traffic. This is very 
useful if the internal communications between your applications can potentially overwhelm an application with requests. But if your 
application's inter-communication is designed to ensure that this cannot happen then the traffic shaping is not needed. By default 
(compile time) it is off.

These environment variables can be used to override the default leaky bucket intra-cluster message shaping parameters.

* ``CL_LEAKY_BUCKET_VOL`` -- Leaky bucket volume in bytes
* ``CL_LEAKY_BUCKET_LEAK_SIZE`` -- Leaky bucket removal in bytes
* ``CL_LEAKY_BUCKET_LEAK_INTERVAL`` -- How often the leak occurs in milliSeconds

Environment Variables Set by OpenClovis SAFplus Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
These variables are available for use in your application:

Locations
"""""""""
Note these environment variables have equivalent "C" global variables (defined in clEoApi.h) which are recommended over using the 
environment variable directly.

* ``ASP_NODENAME`` -- The name of the node (as defined in the SAF AMF model)
* ``ASP_COMPNAME`` -- The name of this component (as defined in the SAF AMF model)
* ``ASP_RUNDIR`` -- The "current working directory" SAFplus Platform runs from
* ``ASP_LOGDIR`` -- The SAFplus Platform log directory
* ``ASP_BINDIR`` -- The location of SAFplus Platform binaries
* ``ASP_APP_BINDIR`` -- The location of the program binary. This is often, but not always the same as ``ASP_BINDIR``.
* ``ASP_CONFIG`` -- Directory of the SAFplus Platform configuration files (normally <asp install dir>/etc)
* ``ASP_CPM_CWD`` -- The current working directory to use for SAFplus Platform and programs started by SAFplus Platform (defaults to 
  var/run)
* ``ASP_DBDIR`` -- The location the SAFplus Platform stores its database files

CLI
---

Starting and Stopping SAFplus Platform: <aspDir>/etc/init.d/asp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

    Usage : asp {start|stop|restart|console|status|zap|help} [options]

options can be one of the following : (these options only work with start command, e.g. etc/init.d/asp start -v etc.)

* ``-v``: Be verbose
* ``--enforce-tipc-settings``: Use etc/asp.conf's TIPC settings overriding the system TIPC settings
* ``--ignore-tipc-settings``: Use systems TIPC settings ignoring the etc/asp.conf's settings
* ``--remove-persistent-db``: Delete all of the SAFplus Platform persistent database files
* ``--asp-log-level <level>``: Start SAFplus Platform with particular log level.

  * ``<level>`` is [trace|debug|info|notice|warning|error|critical]

bin/asp_console
^^^^^^^^^^^^^^^
SAFplus Platform console is a comprehensive CLI for examination and debugging of the SAFplus Platform system. SAFplus Platform console 
documentation is available as a separate document.

.. code-block:: text

    Start: <aspDir>/etc/init.d/asp console or <aspDir>/bin/asp_console

bin/asp_info
^^^^^^^^^^^^
The SAFplus Platform info CLI is a simple interface for display of SAFplus Platform status and basic control

.. code-block:: text

    Start: <aspDir>/bin/asp_info

Directly running a component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run:

.. code-block:: console

    # bin/asp_run
