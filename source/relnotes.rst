.. _rl-nt-label:

Release Notes
=============

Preface
-------
Welcome to OpenClovis Release Notes. This document provides information about the details of the platforms on which OpenClovis 
SAFplus Availability/Scalability Platform (the SAFplus Platform for short) and Integrated Development Environment (IDE) have been 
tested and validated for SDK Release 6.0. It contains the additional features and enhancements of the product since the previous 
release. It also summarizes the known issues and limitations of the product and provides workaround wherever applicable.

Key Topics
^^^^^^^^^^
OpenClovis Release Notes covers the following topics in details:

* Tested Platforms
* What Is New
* Migration To Latest Version
* Known Issues
* Environment Related Observation
* Documentation Issues

Audience
^^^^^^^^
OpenClovis Release Notes addresses system integrators, designers, and system architects. To use SAFplus Platform, you must be aware 
of the fundamentals of operation, management, and configuration of telecom and networking domains. You must also be familiar with 
C programming, UML notations, and have basic knowledge of Linux.

.. TODO: Documentation Conventions and refs in Related Documents. Colored headings
 
Related Documents
^^^^^^^^^^^^^^^^^
For additional information about OpenClovis products, refer to the following guides:

* **SAFplus Platform SA Forum Compliance** describes the level of compliance of OpenClovis SAFplus Platform and its Application Programming Interface (API) with the relevant Service Availability Forum Specifications.
* **SAFplus Platform Installation Guide** provides the system requirements, installation procedure for OpenClovis SAFplus Platform, IDE, and the Evaluation System.
* **SAFplus Platform Sample Application Tutorial** explains the steps to create and build a sample model using OpenClovis IDE and OpenClovis SAFplus Platform. It also provides troubleshooting information for this process. This provides the logical first step in understanding the SAFplus Platform offering.
* **SAFplus Platform Evaluation System User Guide** provides all the required information to configure and run the sample models packaged within the Evaluation System. This document also provides good understanding of OpenClovis SAFplus Platform's functionality. This is the natural follow on to the OpenClovis Sample Application Tutorial as it builds on the example created in that document.
* **SAFplus Platform SDK User Guide** provides information about SAFplus Availability/Scalability Platform architecture, various SAFplus Platform components, and their interactions. This guide helps you to configure the OpenClovis SAFplus Platform components, compile, and execute the SAFplus Platform code to build your custom application.
* **SAFplus Platform IDE User Guide** describes the usage of Integrated Development Environment (IDE), a graphical development environment that complements the SAFplus Platform. This guide helps you to understand how to use the various features of the IDE to build the application.
* **SAFplus Platform Log Tool User Guide** provides information about the usage of OpenClovis Log Tool. OpenClovis Log Tool is an interactive utility that allows you to view binary log files in a readable format and hence monitor system errors, warnings, and other log information. Log Tool allows you to format the .log files and filter them to view the required entries.
* **SAFplus Platform API Reference Guide** is provided for each component. It describes the Application Programming Interface (API), Service Model, and Management Information Model of the various OpenClovis Application Service Platform (SAFplus Platform) services. It helps the developer to understand the capabilities of the SAFplus Platform services and the APIs provided by these services.
* **SAFplus Platform Console Reference Guide** provides details about managing applications built on SAFplus Platform using the SAFplus Platform runtime debug console commands. SAFplus Platform Console commands can be used to manage, monitor, and test your application.

OpenClovis Online Technical Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis customers and partners can register on our Web site and receive personalized services and information. If you need any 
support or assistance while working on OpenClovis products, you can access the following: `openclovis.com <https://www.openclovis.com/>`__. 
Send your queries to: support@openclovis.com. Open source community support is available at: `openclovis.org/forum <http://www.openclovis.org/forum/>`__.

Documentation Feedback
^^^^^^^^^^^^^^^^^^^^^^
We are interested in hearing from our customers on the documentation provided with the product. Let us know your comments and 
suggestions on improving the documentation at OpenClovis Inc. Send your comments to: support@openclovis.com. Or even better, edit 
(or comment in) the page on our documentation wiki located at `help.openclovis.com <http://help.openclovis.com/>`__.

Tested Platforms
----------------
This chapter provides the details of the platforms on which OpenClovis SAFplus Platform have been tested and validated.

+------------------------+-----------------------------------------------------------------------------------+
| Platform               | Configuration                                                                     |
+========================+===================================================================================+
| Hardware               | * ATCA 5U Chassis - Schroff, ASIS                                                 |
|                        | * ATCA 12U Chassis - Schroff, Sanmina, HP, Sun Netra, Radisys, Huawei Tecal Server|
|                        | * Pigeon Point Systems ShMM300 and ShMM500 based Shelf Controllers                |
|                        | * Radisys Promentum 60x0 and its 2100 Switch/Shelf Controller blades              |
|                        | * CPU Blades:                                                                     |
|                        |                                                                                   |
|                        |   * Intel Xeon based server cards                                                 |
|                        |   * Intel Pentium and Xeon based desktops and rack mount servers (RMS)            |
|                        |   * Intel Itanium based RMS                                                       |
|                        |   * AMD Opteron based ATCA cards                                                  |
|                        |   * AMD Opteron and Athlon based desktops                                         |
|                        |   * PowerPC based AMCs                                                            |
|                        |   * PowerPC based desktops                                                        |
|                        |   * Huawei Tecal BH23                                                             |
|                        |   * Sun 3020 and 3090                                                             |
+------------------------+-----------------------------------------------------------------------------------+
| Software               | * Wind River PNE-LE 1.2 (2.6.10 kernel) on CPU blades                             |
|                        | * Wind River PNE-LE 1.3 (2.6.14 kernel) on CPU blades                             |
|                        | * Wind River PNE-LE 1.4 (2.6.14 kernel) on CPU blades                             |
|                        | * Wind River PNE-LE 2.0 (2.6.21 kernel) on CPU blades                             |
|                        | * MontaVista Linux Carrier Grade Edition 5.0 (2.6.21 kernel)on CPU Blades         |
|                        | * QNX Neutrino RTOS 6.3.2                                                         |
|                        | * Pigeon Point Systems Shelf Manager version 2.2.1 on ShMM300, ShMM500            |
|                        | * SCM software version 1.7 on ATCA 2100 Shelf Manager                             |
|                        | * OpenHPI 2.8.1 and 2.10.2                                                        |
|                        | * Radisys HPI Client Library (HCL) version 1.1                                    |
+------------------------+-----------------------------------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Tested Platform Configurations**

For more details on the hardware and software requirements and the steps to install OpenClovis SAFplus Platform and IDE, refer to 
*OpenClovis Installation Guide*.

What Is New
-----------
This chapter outlines the new features and enhancements provided by OpenClovis SAFplus Platform and IDE for all releases.

New In Release 6.1
^^^^^^^^^^^^^^^^^^
* Management Transformation: The SAFplus management is deprecated and replaced with an add-on product that supports NETCONF, SNMP, and CLI access.
* Multi-language code generation and support: Applications can generate C, C++, or Python code. Language-specific wrappers are provided for many SAFplus services.
* Support for gcc 4.8: Compilation errors/warnings fixed
* C++ compilation: SAFplus can compiled with the C or C++ (gcc or g++) compiler.

Porting Prior Models to 6.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The changes in 6.1 mean that 6.0 models will not compile without modification. However, the required changes are simple and so your 
model can be fixed in minutes.

* Problem: clCompCfg.c:39:1: error: too many initializers for ClEoConfigT

  * Remove the first initializer:
    COMP_EO_NAME,               /* EO Name                                  \*/

* Problem: undefined symbol: ClNameT.

  * Convert all your references to SaNameT -- it is the exact same structure

* Problem: CL_DEBUG_XXXX was not declared in this scope.

  * Change the symbol to CL_LOG_SEV_XXXX.

New In Release 6.0
^^^^^^^^^^^^^^^^^^
**SAF Message Service**

* Optimization: The SAF message service now operates using a peer-to-peer instead of client-server model, resulting in a 400% speedup and reduced network utilization.
* Additional features: Persistent message queues are always stored off-node and will not lose messages during application or node failures. The SAF standard allows node failures to lose messages in persistent queues.

**Availability Management Framework**

* 1+N system controller redundancy: More then 2 system controllers are now supported.
* Custom redundancy model: Our SAF-extension "Custom" redundancy model allows the application to chose Active/Standby pairing.

**Platform Support Package**

* HPI event filter plugin: A facility was created to intercept, analyze and modify or squelch HPI events before they are handled by the SAFplus Platform. Since it is implemented as a plug-in to our chassis manager, this feature does not affect the latency of our fast-path event handling.
* OpenHPI 3.0 is now the default HPI package
* The HPI dynamic simulator is fully supported, with OpenClovis extensions that generate HPI events if a threshold is changed so that the simulated sensor value falls outside of the nominal range.

**Messaging Layer**

* The messaging subsystem used by SAFplus Platform has been converted to a plug-in, allowing the user to implement different transport mechanisms.
* UDP and TIPC plugins are now supported with the default set to TIPC as before*.

**Leader Election**

* Cluster leader election is now based on results from the messaging layer (i.e. from TIPC) rather then running an independent algorithm.

  .. note::
    This feature is not yet supported by the IDE, but can be enabled by changing configuration files.

Release 6.0 Patch 201212102041 Dec 10,2012
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Changes to support Emerson HPI (along with the existing OpenHPI and Radisys) for users of the Platform Support Package
* Removed accidental inclusion of OpenHPI header files, even when HPI is not selected.

  * Note: this will cause a compile error in the auto-generated file src/config/clCmResourceDeps.c. The fix is to add the following #ifdef near the top of the file (and #endif at the end):

    .. code-block::

        #include <clCmApi.h>
        #ifdef CL_USE_CHASSIS_MANAGER
        #include <SaHpi.h>
        .
        .
        .
        #endif

  * Additionally, add the following line to the top of src/config/Makefile:

    .. code-block::

        include $(CLOVIS_ROOT)/SAFplus/mk/preface.mk

  * This will ensure that CL_USE_CHASSIS_MANAGER is defined if required.
  * Theses file will be automatically corrected if you regenerate the code from within the IDE.

* Updated the "eval" (tutorial) model to work with the 6.0 release. It is located in src/examples/eval.

New In Release 5.0
^^^^^^^^^^^^^^^^^^
**General Features**

* **Support for Wind River PNELE 2.0:** OpenClovis SDK can seamlessly build SAFplus Platform and binaries for Wind River Platform for Network Equipment Linux Edition 2.0 on all supported SDK platforms, either using the build tool-chain of OpenClovis or of the development environment of Wind River.

**High Availability (HA)**

* **ISSU - In Service Software Upgrade:** Supports middleware upgrade in a rolling (in-service) or single-step mode.

  * **Single-Step** For deployment of non-backwards compatible software, or rapid deployment of software. This method stops the relevant services on all nodes (causing an outage) and then upgrades that software and restarts. Note that services are stopped at various granularity levels depending on what is being upgraded. In other words, application A can be taken out-of-service and upgraded across the cluster without affecting application B running on the same nodes.
  * **Inservice Rolling** This is the most commonly known telecom quality upgrade method. For deployment of backwards-compatible software across the cluster, this method stops service in one "upgrade unit" at a time, upgrades the software and restarts before stopping the next "upgrade unit". This process continues iteratively until the entire cluster is upgraded. Since the available redundant capacity takes over for the unit being upgraded service will be unaffected.

**Infrastructure and Communications**

* **Group Membership Service (GMS) over TIPC:** By default GMS/openais is now compiled to run over TIPC.
* **SAF Message Service:**

  * SAF messaging data types and APIs supported by OpenClovis:

    * classes/types:
    * SaMsgMessageT
    * SaMsgHandleT
    * SaMsgQueueStatusT
    * SaMsgQueueHandleT
    * SaMsgSenderIdT
    * SaMsgQueueCreationAttributesT
    * SaMsgQueueOpenFlagsT
    * SaMsgQueueGroupPolicyT
    * SaMsgQueueGroupNotificationBufferT
    * SaMsgQueueGroupNotificationT
    * SaMsgQueueUsageT
    * SaMsgCallbacksT
    * SaMsgMessageReceivedCallbackT

  * APIs:

    * saMsgMessageSend
    * saMsgMessageSendAsync
    * saMsgQueueOpen
    * saMsgQueueClose
    * saMsgQueueStatusGet
    * saMsgMessageGet
    * saMsgMessageDataFree
    * saMsgQueueGroupCreate
    * saMsgQueueGroupInsert
    * saMsgQueueGroupTrack
    * saMsgQueueGroupNotificationFree
    * saMsgInitialize
    * saMsgFinalize
    * saMsgDispatch

**SAF Component cleanup script support**

* 5.0 introduces support to configure cleanup commands for SA-AWARE components using the Openclovis IDE. The cleanup command is invoked by AMF on component cleanup or abrupt terminations.

**System Management**

* Support of net-snmp 5.4.2.
* SNMP Traps in 64 Bit architectures.

**Platform Management**

* OpenClovis SAFplus Platform provides pre-integrated support for commonly used ATCA platforms. All service affecting events reported by the shelf manager via HPI are intercepted and service on affected hardware is migrated to standby equipment, ensuring continuity of service.
* This support is provided with the Platform Support Package (PSP) for Piegon Point Shelf manager 500ShMM via openHPI.
* PSP is available as a separate product, please contact OpenClovis Sales for further information.

**Features of OpenClovis IDE**

* **Running SAFplus Platform without manageability components:** IDE is having the support for enable/disable SAFplus Platform components. For more information refer to OpenClovis IDE User Guide.
* **AMF Clean-up script:** IDE is having support to specify the cleanup command in SAF Component. For more information refer to OpenClovis IDE User Guide.
* **Versioning the Configuration Files:** IDE is having support for versioning the configuration files.
* **SAF Messaging:** IDE is having support to enable the SAF messaging. For more information refer to OpenClovis IDE User Guide.

**SAFplus Platform Run-Time Director**

A new product, the SAFplus Platform Run-Time Director(ARD), provides cluster management of the SAFplus Platform via a web interface. This new product is available separately, please contact OpenClovis for demonstration and evaluation. The ARD has the following features:

* Software Distribution: Allows individual applications to be packaged in a "bundle" and be deployed to any set of nodes in the cluster.
* Inservice Software Upgrade: Supports application upgrade in a rolling (in-service) or single-step mode.
* WYSIWYG: Provides intuitive cluster management via an HTTP (web) interface.
* AJAX: Displays all SAF AMF entities and their current status -- uses asynchronous Javascript requests to dynamically update browser when changes occur.
* Dynamic AMF: Allows modification of AMF entity state and supports creation/deletion of AMF entities.
* High Availability: The ARD runs in unprotected or 2N redundancy mode.
* Python AMF API: Provides an easy-to-use CLI/programmatic API for cluster management
* Easy installation: The ARD can install itself into a running SAFplus Platform model, and therefore requires no changes to your existing model.
* Extensible: The ARD is built on top of TurboGears, a popular open source web mega-framework. Thus it provides a basis and example for your custom SaaS or EMS project.
* Integration of Platform Support Package (PSP), provides chassis configuration through OpenHPI.

**OpenClovis Documentation**

* OpenClovis Documentation is provided in two formats now, PDF and HTML. They both contain the same information.
* A new OpenClovis SA Forum Compliance document has been added
* As a courtesy, all relevant SA Forum specifications are supplied as part of our OpenClovis documentation package (only in PDF format).
* A new OpenClovis Sample Application Tutorial has been added, replacing the former Modeling Tutorial. The new document provides explanation for the various steps involved in creating and running a new application.
* The OpenClovis SDK User Guide has been extended to cover many additional topics, including:

  * Communication infrastructure
  * Hardware platform support
  * How to debug SAFplus Platform based applications
  * Build and deployment

* The OpenClovis API Reference Guide has been significantly revised:

  * Numerous coding examples
  * New reference pages for API error codes for easy lookup
  * HTML version of API Refernce Guide is heavily cross-referenced, allowing easy navigation between the various programming construcs

* New, complete OpenClovis SAFplus Platform Console Reference Guide as a separate document

  .. note::
    From this release, the Debug CLI has been renamed to SAFplus Platform Console.

Migration To Latest Version
---------------------------
Migration of a project or model from an earlier version of the OpenClovis IDE to the most recent version is performed automatically 
when the model it opened for the first time in the newer vesion. The IDE auto-detects the project's version and changes the 
internal files so that the information is in valid format and can be read by the current version. It also provides an option to 
create a backup of the project while performing the migration. For more information, refer to OpenClovis IDE User Guide, Section 
Migrating Project. IDE supports migration from R2.3 and above.

Any issues regarding migration from a previous version of the IDE are documented below:

* Change in Log File Locations: As of release 3.0 all SAFplus Platform runtime log files are created in the var/log subdirectory of the SAFplus Platform install directory. It is recommended that you update existing models to also use this directory. To update an existing model edit the clLog.xml file in the model's src/config directory. Change all references of .:log in the <fileLocation> elements

  * <fileLocation>.:log</fileLocation> to .:var/log
  * <fileLocation>.:var/log</fileLocation>
  * Once the model is rebuilt and deployed these new settings will take effect.

* gmsConfig.xml file

  * Models of R2.3 may not contain the gmsConfig.xml file if GMS configuration is not done. If you migrate this project you will get error message saying that Migration was unable to create this file. But this is not going to affect further use of model. Model will be OK and user can make changes to it from IDE, generate source, build it, etc without any problem.
  * Although this error is not going to affect the functionality of the model, there is a work around for this. Before migrating your model, just open up the model in your old IDE setup. Launch "SAFplus Platform Component Configuration" dialog from the Clovis menu. Press OK. Now just migrate the model with new IDE setup, you will not get this error. Bug has been raised for this and it will be fixed in next release.

Known Issues
------------
This chapter describes the known issues in the current release and provides the associated workarounds. These issues arise due to 
deviation from the normal functioning of the system or as a result of an unexpected behavior of a component or a service.

Known Issues of OpenClovis SAFplus Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Following are the known issues for OpenClovis SAFplus Platform:

* **Infrastructure and Communications**

  * **TIPC address:** TIPC with 1.5.12 versions was found to give problems (link unstable) when you have 2 different TIPC netids configured for the same TIPC address. This issue is not seen with the 1.7.x TIPC releases, but in general we recommend you to keep the TIPC addresses unique and not collide with the same addresses on nodes configured with different TIPC netids. One of the symptoms of this is that the TIPC link between 2 machine starts going UP and DOWN continuously when there is another machine in the network, whose TIPC address is conflicting with address of one of those 2 machines. The behavior can be observed through continuous execution of command "tipc-config -l" or through "dmesg".
  * In general, TIPC 1.5.XX has been found to be unstable, especially under high multicast load, and should not be used in production environments.
  * **Bug ID #7269** A cluster having a mixture of 32bit little endian, 32bit big endian and 64 bit little endian machines/nodes may find that the GMS service in inadvertently terminates.

    * **Workaround** - None

  * **aspinfo known issues:** (1) On some systems, especially systems with Python version 2.3, aspinfo can be slow to respond. (2) Some corner cases may not be properly handled and aspinfo may prematurely exit, dumping its Python stack.

* **System Management**

  * **Bug ID #7313** If an Alarm Server is restarted after it published an alarm, it won't allow to clear/publish that alarm again.

    * **Workaround** - Currently there is no workaround.

* **SAF Compliance**

  * **Deviation from SAF in Event Service:** Event Service does not yet support Event Retention as specified in SAF specification. The retention time specified in the clEventPublish() API would have no effect.
  * **Bug in SAF specificaion B11:** The clEventDataGet() API of Event Service is in compliance with the SAF specification B11. This allows the user to either allocate memory for the event payload or obtain it from the API by passing a pointer. The latter is not possible with this API as the argument needs to be a pointer to a pointer which is not the case. As per the new specification and the recommended way the user is always required to allocate and free the memory.

Known Issues of OpenClovis IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Bug ID # 6543: X Error in Ubuntu Installation.** Starting the IDE in Ubuntu installation may result some X errors in the console. This is not an IDE issue, this will not affect any of the IDE functionalities.

  * **Workaround** - See the Limitations section of the OpenClovis IDE User Guide.

* **SNMP MIB Enumerated Integer Construct Limitations:** During SNMP code generation all enumerated integer labels are converted to #define statements. The constant names used in these statements are the enumerated integer labels converted to upper case. Because of this the all labels used within an enumerated integer construct must be unique regardless of case.
* **SNMP MIB V1 TRAP-TYPE Construct Not Supported:** Due to an issue in the Net-SNMP mib2c compiler code generation for MIBs using the V1 TRAP-TYPE construct does not work properly.

  * **Workaround** - To generate trap code from an SNMP MIB use the SNMP V2 NOTIFICATION-TYPE construct.

Known Issues of Install Package
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Bug ID # 6749: Potential conflict with net-snmp package on local system:** In certain rare instances, building OpenHPI from the included third-party packages during SDK installation fails owing to a conflict with an already-installed version of NetSNMP on the system. In these instances, it is recommended that NetSNMP be removed from the local system before installing OpenClovis SDK, and that it be reinstalled after completing the SDK installation.
* **Installation on Red Hat Enterprise 4:** On a Red Hat Enterprise Linux 4 system, the 'Development Tools' subset of packages must be installed to cover the requirements for installing OpenClovis SDK. In general, an installation with the default package set contains all requirements for installation.
* **Installation on Fedora Core 6:** On a Fedora Core 6 system, installation of OpenClovis SAFplus Platform automatically builds and installs the TIPC opensource package. To build TIPC, the kernel headers must be present and so these are automatically installed (by our ./preinstall-fedora-core.sh script) using the "yum install kernel-devel" command. On rare configurations, this command does not work correctly. It is supposed to install headers so that the symbolic link located at "/lib/modules/`uname -r`/build" points to a valid directory of Linux header files. However, on some systems this symbolic link points to "/usr/src/kernels/2.6.22.14-72.fc6-i586" but the headers are actually installed in "/usr/src/kernels/2.6.22.14-72.fc6-i686" (note 'i586' vs 'i686'). To resolve this problem, change the symbolic link to point to the correct directory name, and then restart the OpenClovis SAFplus Platform installation.
* **Configuring TIPC and assigning the SAFplus Platform node address** to an OpenClovis SAFplus Platform is done by SAFplus Platform start up script. But if manual configuration of TIPC is allowed. Misconfiguration (such as assigning 2 nodes the same TIPC address) will result in an unstable system. When this happens the whole system (all the SAFplus Platform nodes including the ones which are already up and running properly) have to be brought down, the TIPC kernel driver unloaded (to remove its configuration) and the system restarted.
* **Installation of SQLite using Preinstall script:** The Preinstall script installs SQLite by default as database engine. It locates SQLite - if it is already installed - without verifying version number. If its version is older than 3.3.13, then SAFplus Platform will fail to start.

  * **Workaround** - Use SQLite 3.3.13 or newer. The source code can be downloaded from http://www.sqlite.org/download.html. The user can install the latest version of SQLite if its not present in the repository.

* **Installation on Solaris 10/SPARC (beta):** Installation of OpenClovis SAFplus Platform requires the following third party packages installed via either installation media or using pkgadd with packages obtained from http://www.sunfreeware.com/. Missing third-party packages may cause unpredictable behavior during installation and SDK use.

  * db-4.2.52
  * fileutils
  * flex
  * gcc-3.4.2
  * gdbm-1.8.3
  * glib-2.14.1
  * gmake
  * gtar
  * libintl
  * libiconv
  * ncurses
  * openssl
  * pkgconfig
  * python-2.5.1
  * readline
  * snprintf
  * tipc-solaris-1.7.5 or SUNWtipc
  * SUNWbtool
  * SUNWsprot
  * SUNWhea
  * wget

Environment Related Observation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Bug ID #7549** When SAFplus Platform is running in non simulation mode, if SAFplus Platform is started from one sandbox, then it can be stopped/zapped from another sandbox.

* **Enabled Firewall Can Cause SAFplus Platform to Shutdown:**

  * The enablement of a firewall on a system running a deployed SAFplus Platform image can cause the software to shutdown. An indication that you may be running into this problem is if you see an entry similar to the following in your log file (in the log file it is one line):

    .. code-block:: text

        Wed Sep 26 15:06:54 2007   (SCNodeI0.10499 : GMS.---.---.00036 :  ERROR)
           [clGmsEngine.c:448] No nodes in the cluster view to run leader 
           electionLeader Election Aborted

  * To resolve this problem disable all filtering in the Netfilter framework by issuing the following command.

    .. code-block::

        iptables -F

* **Reusing A Project Area With New Version of OpenClovis SDK**

  * Every Project Area is associated with an installation of OpenClovis SDK at a given location. If one elects to reinstall the SDK at a different location or install a newer version at a different location, the project area will stay associated with the original SDK location. This allows one to work with multiple versions of the SDK simultaneously. In order to use an existing project area with a different or moved installation of OpenClovis SDK, remove the .config file from your project area directory and re-run configure as you normally would to work with a model.

* **Running Multiple SAFplus Platform Clusters in the same Subnet**

  * If you are running multiple SAFplus Platform clusters within the same subnet, please ensure that the TIPC network ID selected for each cluster is unique.

Documentation Issues
^^^^^^^^^^^^^^^^^^^^
This chapter describes the known issues with the OpenClovis Documentation shipped along with the product.

* Formatting issues

  * Following cross-references pointing to a heading, the PDF viewer will jump to the end of the previous page if the heading is on the top of a page.
  * Firefox web browsers sometimes do not correctly jump to intra-page anchors when the user clicks on a reference. This is a known issue with Firefox. The workaround is to click on Back button and then on the reference again. The browser jumps to the correct position for the 2nd time.
