Environment Variables
=====================

Logging
-------

CPM_LOG_FILE_SIZE
^^^^^^^^^^^^^^^^^
This variable defines the maximum size of the stdout (console) log. Use a number + K for kilobytes, M for megabytes and G for gigabytes.

.. code-block:: bash
    :caption: Example

    export CPM_LOG_FILE_SIZE=100K

CPM_LOG_FILE_ROTATIONS
^^^^^^^^^^^^^^^^^^^^^^
This variable defines the number of log files (i.e) name1.log name2.log, etc to use before restarting the count.

.. code-block:: bash
    :caption: Example

    export CPM_LOG_FILE_ROTATIONS=100

CL_LOG_TO_FILE
^^^^^^^^^^^^^^
Sends all logs to a file or stdout. This environment variable is very helpful when debugging problems that occur before the SAFplus 
log server has started. For example:

.. code-block:: bash

    export CL_LOG_TO_FILE=stdout
    export CL_LOG_TO_FILE=/var/log/mylog.txt

ASP_STDOUT_LOGFILE
^^^^^^^^^^^^^^^^^^
This variable (deprecates ASP_CPM_LOGFILE) [version 5.1+] overrides the log file name for the safplus_amf. Use either an absolute 
path (beginning with /) or a path relative to the ASP log directory. The special name "console" will output to the console instead 
of a file.

Note, setting this variable to "console" is equivalent starting with the command "etc/init.d/asp consolestart".

.. code-block:: bash
    :caption: Example

    export ASP_STDOUT_LOGFILE=/tmp/stdoutlog.txt
    export ASP_STDOUT_LOGFILE=stdoutlog.txt
    export ASP_STDOUT_LOGFILE=console

CL_LOG_CODE_LOCATION_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Adds file/line to each log message, so logs can be tracked in the source code

.. code-block:: bash
    :caption: Example

    export CL_LOG_CODE_LOCATION_ENABLE=1

CL_LOG_TIME_ENABLE
^^^^^^^^^^^^^^^^^^
Adds a timestamp to each log message (default is true)

.. code-block:: bash
    :caption: Example

    export CL_LOG_TIME_ENABLE=0

Debugging
---------

ASP_NODE_REBOOT_DISABLE
^^^^^^^^^^^^^^^^^^^^^^^
Disable reboot of nodes, even if the AMF HA algorithm determines a reboot is necessary.

.. code-block:: bash

    export ASP_NODE_REBOOT_DISABLE=1

ASP_NODE_RESTART
^^^^^^^^^^^^^^^^
Restart the SAFplus on node recovery, rather then wait for operator intervention.

.. code-block:: bash

    export ASP_NODE_RESTART=1
