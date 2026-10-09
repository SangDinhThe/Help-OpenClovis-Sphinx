Logging
=======

FAQ
---

How to redirect standard output to syslog?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ASP normally redirects standard output/standard error to a file located in var/log. You go back to the default console output for 
these streams by setting ASP_STDOUT_LOGFILE (version 5.1+) or ASP_CPM_LOGFILE (version 5.1 or lower) to "console". From there you 
redirect in the normal fashion, see `this article <http://stackoverflow.com/questions/665509/redirecting-standard-output-to-syslog>`__

However, note that using the OpenClovis logging mechanism is preferred over the standard output. And all OpenClovis logs already go 
to the files "sys.XXX" and "app.XXX". The console logging is recommended for debugging only.

**Detailed example:**

#. Use only NodeName.logs by setting sys/app stream logs to have 10MB size with WRAP policy (in clLog.xml) -- so they remain in their 
   original log location on each node and are basically not used. You can even disable the log server.

#. Now change the <NodeName>.log filename and location. You can set these variables in target.env in $MODEL/src/ since that is copied 
   to etc/asp.conf. Or in set them yourself before starting ASP on the target:

   .. code-block:: bash

    export ASP_LOGDIR="/var/log/"
    export ASP_CPM_LOGFILE="asp.log"
    export CPM_LOG_FILE_ROTATIONS=0

   Using above configuration, logs are written into /var/log/asp.log file on all the cards.

#. Next, use syslog-ng to pre-create the named pipe with name "asp.log" in /var/log directory on all the nodes (it just requires an 
   entry in syslog-ng.conf file to achieve this). Through the reader of these pipes (syslog-ng on local node), logs are sent/forwarded 
   to the master/destination syslog-ng(s). The best choice is generally to forward to syslog-ng on both the system controller cards. 
   This redundancy is needed in order to avoid losing logs in case of hard disk failure on one of the system controller cards.

How to redirect a log stream to syslog?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ClLogStreamAttributesT object has a field "syslog". Set this field to TRUE before opening the log. This can also be done for 
"precreated" streams in the clLog.xml by setting the "syslog" tag to "yes". For example:

.. code-block:: mxml

    <stream name="appStream">
        <fileName>app</fileName>
        <fileLocation>.:var/log</fileLocation>
        <fileUnitSize>1500000</fileUnitSize>
        <recordSize>300</recordSize>
        <fileFullAction>ROTATE</fileFullAction>
        <maximumFilesRotated>3</maximumFilesRotated>
        <flushFreq>20</flushFreq>
        <flushInterval>20000000</flushInterval>
        <syslog>yes</syslog>
    </stream>
