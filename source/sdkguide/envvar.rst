.. _env-var-label:

Runtime environmental variables exported by the OpenClovis SAFplus Platform environment
=======================================================================================
Following are the environmental variables exported by the OpenClovis SAFplus Platform environment, which are available to the 
application developers. Using these environmental variables to create additional files/logs (if any) etc is recommended, because in 
case of any problems in SAFplus Platform, it will be easier to correlate the log files present in these locations and hence to 
diagnose the cause of the problem.

* ``ASP_DIR`` - Location of the sandbox directory, i.e. the directory in which SAFplus Platform is deployed.
* ``ASP_RUNDIR`` - Default working directory of application components.
* ``ASP_LOGDIR`` - Place where the log files should be created. (This can be overridden using the clLog.xml, but it is recommended 
  that application developers create their logs here.)
* ``ASP_DBDIR`` - Location where persistent files (if any) by the application should be created.
* ``ASP_CONFIG`` - Place where all the configuration data used by the SAFplus Platform is stored.
* ``ASP_BINDIR`` - Location of all the binaries (SAFplus Platform as well as user applications).
* ``ASP_WITHOUT_CPM`` - This environment variable is exported (=1) when you run your program manually (not started by SAFplus AMF) 
  using the "safplus_run" command. This is valuable because programs running outside AMF will not get work assignments -- that is they 
  won't be told to become active or standby.

.. note::
    When deploying SAFplus Platform images on a particular node, if there is a ``extras`` directory present in the model directory, then 
    the directory structure underneath it will be overlaid on top of the sandbox directory, without overwriting the files in the sandbox 
    directory, in case of file name clash. For e.g. if model name is test, and if there is a file called test/extras/bin/test_bin, then 
    if the deployed image is extracted to directory called ``asp``, then asp/bin/ will contain test_bin file (provided there already isn't 
    test_bin file in bin/ directory). This can be helpful to package custom scripts, binaries etc when deploying an SAFplus Platform image.
