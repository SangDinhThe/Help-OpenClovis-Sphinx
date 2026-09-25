Install Guide
=============

Preface
-------
Welcome to OpenClovis Release Notes. This document provides information about the details of the platforms on which OpenClovis 
SAFplus Availability/Scalability Platform (the SAFplus Platform for short) and Integrated Development Environment (IDE) have 
been tested and validated for SDK Release 6.0. It contains the additional features and enhancements of the product since the 
previous release. It also summarizes the known issues and limitations of the product and provides workaround wherever applicable.

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
 
.. _ins-gd-rd-label:

Related Documents
^^^^^^^^^^^^^^^^^
For additional information about OpenClovis products, refer to the following guides:

* :ref:`SAFplus Platform Release Notes <rl-nt-label>` provides information about the software and the hardware required to install OpenClovis Application Service Platform (SAFplus Platform) and Integrated Development Environment (IDE). It summarizes the additional features and enhancements of the product since the previous release. It also summarizes the issues and limitations of the product and provides workarounds wherever applicable.
* **SAFplus Platform SA-Forum Compliance** describes the level of compliance of OpenClovis SAFplus Platform and its Application Programming Interface (API) with the relevant Service Availability Forum Specifications.
* **SAFplus Platform Installation Guide** provides the system requirements, installation procedure for OpenClovis SAFplus Platform, IDE, and the Evaluation System.
* **SAFplus Platform Sample Application** Tutorial explains the steps to create and build a sample model using OpenClovis IDE and OpenClovis SAFplus Platform. It also provides troubleshooting information for this process. This provides the logical first step in understanding the SAFplus Platform offering.
* **SAFplus Platform Evaluation System User Guide** provides all the required information to configure and run the sample models packaged within the Evaluation System. This document also provides good understanding of OpenClovis SAFplus Platform's functionality. This is the natural follow on to the OpenClovis Sample Application Tutorial as it builds on the example created in that document.
* **SAFplus Platform SDK User Guide** provides information about SAFplus Availability/Scalability Platform architecture, various SAFplus Platform components, and their interactions. This guide helps you to configure the OpenClovis SAFplus Platform components, compile, and execute the SAFplus Platform code to build your custom application.
* **SAFplus Platform IDE User Guide** describes the usage of Integrated Development Environment (IDE), a graphical development environment that complements the SAFplus Platform. This guide helps you to understand how to use the various features of the IDE to build the application.
* **SAFplus Platform Log Tool User Guide** provides information about the usage of OpenClovis Log Tool. OpenClovis Log Tool is an interactive utility that allows you to view binary log files in a readable format and hence monitor system errors, warnings, and other log information. Log Tool allows you to format the .log files and filter them to view the required entries.
* **SAFplus Platform API Reference Guide [1]** is provided for each component. It describes the Application Programming Interface (API), Service Model, and Management Information Model of the various OpenClovis Application Service Platform (SAFplus Platform) services. It helps the developer to understand the capabilities of the SAFplus Platform services and the APIs provided by these services.
* **SAFplus Platform Console Reference Guide** provides details about managing applications built on SAFplus Platform using the SAFplus Platform runtime debug console commands. SAFplus Platform Console commands can be used to manage, monitor, and test your application.
* **Installation of OpenClovis 6.1 is captured**

OpenClovis Online Technical Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis customers and partners can register on our Web site and receive personalized services and information. If you need any 
support or assistance while working on OpenClovis products, you can access the following: `openclovis.com <https://www.openclovis.com/>`__. 
Send your queries to: support@openclovis.com. Open source community support is available at: `openclovis.org/forum <http://www.openclovis.org/forum/>`__.

Documentation Feedback
^^^^^^^^^^^^^^^^^^^^^^
We are interested in hearing from our customers on the documentation provided with the product. Let us know your comments and 
suggestions on improving the documentation at OpenClovis Inc. Send your comments to: support@openclovis.com. Or even better, 
edit (or comment in) the page on our documentation wiki located at `help.openclovis.com <http://help.openclovis.com/>`__.

Prerequisites to Install
------------------------
This chapter provides an overview of the OpenClovis SDK solution comprising OpenClovis SAFplus Platform and IDE. It also provides 
the hardware and software requirements for running OpenClovis SDK and the Evaluation System.

Overview
^^^^^^^^

* OpenClovis provides a modular and cost-effective software platform for creating next-generation communication systems. OpenClovis SDK is designed for solution integrators, network equipment manufacturers (NEPs), and telecommunication equipment manufacturers (TEMs) to facilitate the creation of a broad range of telecommunication devices, including routers, switches, media gateways and wireless infrastructure nodes.
* OpenClovis fits seamlessly with various distributions of Linux and hardware platforms such as AdvancedTCA, BladeCenter T, and other off-the-shelf proprietary hardware.
* The OpenClovis solution comprises OpenClovis SAFplus Platform and OpenClovis IDE.
* **OpenClovis Application Service Platform (SAFplus Platform)** is middleware that offers a comprehensive set of modular, portable, reusable software components designed to provide system management and high availability functionality. OpenClovis SAFplus Platform is the run-time part of the OpenClovis offering. It provides run-time services for your value add applications, offering a layered, hardware-platform independent application environment.
* **OpenClovis Integrated Development Environment (IDE)** is designed to simplify and accelerate the development of application service platforms for the telecommunication marketplace. Coupled with the OpenClovis SAFplus Platform, this intuitive software solution streamlines the process of specifying the information model, high availability (HA) aspects, and the communication infrastructure of a system. OpenClovis IDE stores all information describing a project in well defined XML files that can be modified by the user. Modeling of system resources and relationships are specified using a graphical UML editor.
* **OpenClovis Evaluation System** is a evaluation sample system based on SAFplus Platform that provides the user with a better understanding of the scope of the product, usage patterns, its quality and usability.

Development Host Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This section provides the hardware and software requirements for installing OpenClovis SAFplus Platform and IDE. It is not necessary 
to install OpenClovis IDE on the target host, as all the modeling activities are performed on the development host. The system 
requirements for the development host is summarized in Table System Requirements for a Development Host.

+-----------------------------------------+------------------------------------------------------------------+
| Requirement Type                        | Requirements                                                     |
+=========================================+==================================================================+
| Hardware                                | * Intel Pentium II (or higher)                                   |
|                                         | * Hard Disk - 10 GB (minimum suggested)                          |
|                                         | * RAM - 512 MB (minimum suggested)                               |
+-----------------------------------------+------------------------------------------------------------------+
| Linux Distributions                     | * Red Hat Enterprise Linux 4                                     |
|                                         | * Ubuntu Linux                                                   |
|                                         | * CentOS 4.0                                                     |
|                                         | * Gentoo Linux                                                   |
|                                         | * Fedora Linux                                                   |
|                                         | * Yellow Dog Linux 4                                             |
+-----------------------------------------+------------------------------------------------------------------+
| Third Party Packages                    | * glib-2.0 - 2.6.0                                               |
|                                         | * glibc 2.3.2                                                    |
|                                         | * gcc 3.2.3                                                      |
|                                         | * beecrypt                                                       |
|                                         | * gdbm 1.8.0                                                     |
|                                         | * net-snmp 5.4                                                   |
|                                         | * openhpi 2.8.1                                                  |
|                                         | * openhpi-subagent 2.3.4                                         |
|                                         | * Gtk                                                            |
|                                         | * Eclipse SDK 3.2.2                                              |
|                                         | * EMF SDK 2.2.2                                                  |
|                                         | * GEF SDK 3.2.2                                                  |
|                                         | * JRE 1.5.0_03                                                   |
|                                         | * Python 2.4.1                                                   |
+-----------------------------------------+------------------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**System Requirements for a Development Host**

.. note::
    The OpenClovis SDK installation process verifies the Third Party Packages, and installs any missing packages automatically, as 
    a part of the SDK Installation.

Target Host Requirements
^^^^^^^^^^^^^^^^^^^^^^^^
This section provides the hardware and software requirements for installing OpenClovis SAFplus Platform on the target host. These 
requirements are summarized in Table System Requirements for the Target Platform.

+---------------------+--------------------------------------------------------------------------------+
| Requirement Type    | Requirements                                                                   |
+=====================+================================================================================+
| Hardware            | **ATCA Chassis**                                                               |
|                     |                                                                                |
|                     | * **CPU Types:** Intel Xeon, AMD64, Itanium2                                   |
|                     | * **Blades:** Intel MPCBL0001, Intel MPCBL0030, Intel MPCBL0040, Huawei Tel8000|
|                     | * **Shelf Management:** Pigeon Point ShMM500, RadiSys                          |
+---------------------+--------------------------------------------------------------------------------+
| Linux Distributions | **ATCA Chassis**                                                               |
|                     |                                                                                |
|                     | * Wind-River PNE LE 1.2 (2.6.10 kernel)                                        |
|                     | * Wind-River PNE LE 1.3 (2.6.14 kernel)                                        |
|                     | * Wind-River PNE LE 1.4 (2.6.14 kernel)                                        |
|                     | * Red Hat Enterprise Linux 4.0, 5.0, etc. or Centos equivalent                 |
|                     | * Ubuntu 9+ or similar Debian based Linux                                      |
|                     | * MontaVista Carrier Grade Linux 5.0                                           |
+---------------------+--------------------------------------------------------------------------------+

.. rst-class:: center

**System Requirements for the Target Platform**

.. note::
    These are the Linux distributions on which SAFplus Platform is tested and certified.

SAFplus Platform SDK Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The SAFplus Platform SDK Installation packages listed in Table Required Installation Packages.

.. TODO: add refs to the numbers. eg: [2], [3]

+-----------------------------------------+--------------------------------------------------------------------------+
| File Names                              | Description                                                              |
+=========================================+==========================================================================+
| openclovis-safplus-sdk-X.Y-STAMP.tar.gz | This file is the core installation tarball, to install SAFplus           |
|                                         |                                                                          |
|                                         | Platform, IDE, and the evaluation system. This file is available at [2]  |
+-----------------------------------------+--------------------------------------------------------------------------+
| openclovis-safplus-sdk-X.Y-STAMP.md5    | This file is used to perform the data integrity check of the             |
|                                         |                                                                          |
|                                         | downloaded SDK tar file.                                                 |
+-----------------------------------------+--------------------------------------------------------------------------+
| 3rdparty-base-A.B.C-ARCH.tar            | This file contains the third party packages for SAFplus Platform         |
|                                         |                                                                          |
|                                         | SDK. Please pick your architecture (32 or 64 bit). This file is          |
|                                         |                                                                          |
|                                         | available at github [3]                                                  |
+-----------------------------------------+--------------------------------------------------------------------------+
| 3rdparty-base-A.B.C-ARCH.md5            | This file is used to perform the data integrity check of the             |
|                                         |                                                                          |
|                                         | downloaded third party tar file.                                         |
+-----------------------------------------+--------------------------------------------------------------------------+
| crossbuild-*                            | Crossbuild toolchains are available for a variety of embedded            |
|                                         |                                                                          |
|                                         | operating systems. Please ask if you need one. However, most embedded    |
|                                         |                                                                          |
|                                         | OSes provide a crossbuild toolchain as part of the OS distribution.      |
+-----------------------------------------+--------------------------------------------------------------------------+

.. rst-class:: center

**Required Installation Packages**

.. note::
    OpenClovis SDK is supplemented with a set of crossbuild packages for different CPU and Operating System combinations. The md5 
    and crossbuild packages are optional and maybe downloaded depending on your requirements.

OpenClovis SDK Installation
---------------------------
This chapter provides a step-by-step approach for installing OpenClovis SDK. Before proceeding with installation, ensure that all 
the required hardware and software are available on your system. You need not install the third-party packages, as the installation 
package installs the third-party packages along with OpenClovis SDK.

Installation Procedure - Get Started
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To install Openclovis SDK on your local machine, go to the directory where you have downloaded the required installation files.

Before you install:

* Ensure you have write permissions for the current directory (directory where the installation files are downloaded) and the target directory (directory where you will install the application.)
* At least 512MB of free disk space.
* You can install the SDK either as a root user or a non root user. Installing as root user is not required for a single user host. When using the SDK for larger projects it is advisable to install as root, since multiple users can share the same SDK. Irrespective of the mode of installation, the SDK can be used to model and build code using non-root privileges.

To extract the SDK package, execute the following command:

.. code-block::

    # tar -xzmf openclovis-safplus-sdk-*.tar.gz

.. note::
    The m option to tar ensures that the timestamps on the files within the SDK package are consistent with the host system. This 
    is important, since discrepancies can adversely affect the build procedure.

To ensure that your system has all the prerequisite software packages required by the installation process, the SDK package 
contains "preinstallation" scripts for a variety of Linux distributions. Prerequisite packages are packages that are supplied 
by your distribution but may not have been installed on your system. Essentially this is the GNU compiler toolchain and 
programming utilities such as pkg-config, flex, and bison. These scripts enable the user to acquire and install the prerequisite 
software packages automatically. Some distributions provide these packages on your installation CDROMs, so you may be asked to 
insert them. Other distributions provide these packages via internet-based software repositories (notably Ubuntu). If your 
system does not have internet access, please see Appendix A: Installing the Prerequisites without Internet Access. The installer 
supports most major RedHat and Debian (Ubuntu) based distributions.

Please run the install script corresponding with your Linux distribution by executing the following commands:

.. code-block::

    # cd openclovis-safplus-sdk-*
    # ./install

.. note::
    The install scripts prefers to be run as root so that it can run the "preinstall" and also so it can install SAFplus in 
    /opt/clovis. However, if you need to install SAFplus as a normal user, you may do so. First run ./install as root and choose 
    to install prerequisites only (or install them by hand). Then run ./install again as a normal user.

After you execute the install command, the Welcome screen is displayed.

.. code-block:: text

    Welcome to the OpenClovis SAFplus 6.1 Installer

    This program helps you to install:
        - Required 3rd-party Packages
        - The OpenClovis SAFplus Availabiltiy Scalability Platform

    Installation Directory Prerequisites
        - At least 512MB free disk space
        - Write permission to the installation directory

    Note: You may experience slow installation if the target installation
          directory is mounted from a remote file system (e.g., NFS).

    Please press <enter> to continue or <ctrl-c> to quit this installer

    Please hit <enter> to continue. You will now be presented with the top level install screen.

    --------------------------------------------------------------------------------
               OpenClovis SAFplus 6.1 private Installer - Ubuntu 64-bit
    --------------------------------------------------------------------------------
    Installation Type:

        1) Standard          -  Select all default options
        2) Custom            -  Recommended
        3) Preinstall Only   -  Only does the preinstall phase
        4) Install Only      -  Only does the install phase

    Please choose an installation option [default: 2]: 

If are running as root and want to install in the "standard" /opt/clovis location, please press "1" and follow the instructions. 
Otherwise choose "2". You will be presented with choices as to where to install SAFplus, whether to prebuild it 
(please choose "yes"), and so on.

If you are installing SAFplus as non-root, then choose option 3 (as root) to install the required standard packages from your 
distribution's package management system. Then run ./install again as the normal user and choose option 4.

Depending on your choice, the installer will next present you with the "preinstall" screen:

.. code-block:: text

    --------------------------------------------------------------------------------
               OpenClovis SAFplus 6.1 private Installer - Ubuntu 64-bit           
    --------------------------------------------------------------------------------
    Here are the preinstall dependencies:

    flex  linux-headers-3.13.0-32-generic
    gawk  build-essential
    swig  libsqlite3-dev
    bison libglib2.0-dev
    gettext  e2fslibs-dev
    uuid-dev  libltdl3-dev 
    libdb-dev  libsqlite3-0
    e2fsprogs  libsnmp-dev
    pkg-config  libperl-dev
    zlib1g-dev  libgdbm-dev

    These will be installed via the "apt-get install" command. Some of these may already be installed.

    Please press <enter> to continue or <ctrl-c> to quit this installer

Press <enter> to allow the installer to use your distribution's package manager to install these standard packages.

Note, some distributions (notably Red Hat) obsolete the kernel header files rapidly. Therefore the preinstaller may require that 
you upgrade your Linux kernel, if it has determined that it will need the kernel headers (these are only needed for the TIPC 
communications subsystem, which comes with the kernel on all modern Linux distributions).

Next, the installer will install required dependencies from the "thirdparty-*" archive. If you did not download this archive, the 
installer will download it automatically. These dependencies are not universally available in all Linux distributions so are 
provided by us.

.. code-block:: text

    --------------------------------------------------------------------------------
    Here are the install dependencies for Ubuntu 64-bit:

    Module                  Needed     (Installed)
    ----------------------------------------------
    gcc                     3.2.3      (4.8)
    glibc                   2.3.5      (2.19)
    glib                    2.28.5     (2.40.2)
    openhpi                 3.0.0*     (None)
    net-snmp                5.4.2      (5.7.2)
    openhpi-subagent        2.3.4*     (N/A)
    tipc                               (2.0.0)
    tipc-config             2.0.2*     (N/A)
    JRE                     1.7.0_17*  (N/A)
    eclipse                 4.2.2*     (N/A)
    EMF                     2.8.3*     (N/A)
    GEF                     3.8.2*     (N/A)
    CDT                     8.1.2*     (N/A)
    sqlite                  3.6.7*     (N/A)

    (* needs install)

    Please press <enter> to continue or <ctrl-c> to quit this installer
    Next, the installer installs SAFplus (it will ask you where to put it if you chose option 2):

    Cleaning up...
    Done cleaning.
    Installing SAFplus...

Next, the installer will ask if you would like to prebuild the SAFplus libraries. This option is recommended as it dramatically 
reduces the build time of your model. Please choose the default location, and hit enter to just build for the local machine.

.. code-block:: text

    Build SAFplus libraries for the local machine and/or installed crossbuild toolchains ? <y|n> [y]: 
    Where to build ? [default: /opt/clovis/6.1/sdk/prebuild]: 
    The following installed build tool packages are found:
    local
    Select the crossbuild tool(s) to build from the above list, [Default: local]

You will now see the build in progress...

When the build completes, it will ask whether you want symbolic links created to our binaries so they can be run easily:

.. code-block:: text

    A few binaries are installed in /opt/clovis/6.1/sdk/bin.
    For convenience, you can add the above directory to your PATH defination.
    Alternatively, we can create symlinks for you (from a binary direcory that is already in you path).

    Create symbolic links for items in /opt/clovis/6.1/sdk/bin ? <y|n> [y]: 

Enter Y to create the symbolic links. The installer then prompts the user for a location to place the links with a default option /usr/local/bin if you are installing as root, or $HOME/bin for non root user installation.

If you choose not to create symbolic links and enter N, then you can either:

* Add the installation directory to the shell path. For example with a bash shell: export PATH=$PATH:<install_dir>/<VERSION>/sdk/bin
* or access the SDK commands from the <install_dir>/<VERSION>/sdk/bin/ directory. For example to run the IDE: <install_dir>/6.1/sdk/bin/cl-ide

After creating symbolic links, the installation of OpenClovis SDK is complete. All the required packages and crossbuild toolchains 
are installed and the directory where you have downloaded the installation packages can be discarded.

.. note::
    If your installation is not successful, or if you encounter any problems during the installation, refer to the Chapter :ref:`ins-gd-tbs-label`.

Next Steps
^^^^^^^^^^
After completing the Installation, the OpenClovis SDK Documentation set listed in the :ref:`ins-gd-rd-label` section is available in 
the doc folder located at <install_dir>/6.1/sdk directory.

We recommend the following steps to get familiar with our product:

* **Read and follow the OpenClovis Sample Application Tutorial** - The Sample Application Tutorial will step you through the process of creating a high available system. It takes you from model conception all the way through deployment and running of the sytem. After going through this guide you will understand the basics of the OpenClovis offering.
* **Read and follow the OpenClovis Evaluation System User Guide** - Evaluation System User Guide will introduce you to more advanced modelling topics. These topics are introduced incrementally through a series of targeted tutorials. After completing this guide you will be ready to start building your own system.

.. _ins-gd-tbs-label:

Troubleshooting
---------------
This chapter describes some of the probable errors that you may encounter during the installation. This chapter also provides the 
solution to these errors.The errors that you may encounter are:

* **Error:** Installation Failure, during third party installation.

  * **Solution:** You can manually fix this error by getting more information from the corresponding log file under the log directory. You can also send the log.tar.gz to support@openclovis.com for more help. The installation can be resumed after the errors are fixed. The installer will detect any new updates and proceed with the missing prerequisites.

* **Error:** gcc (pkg-config, perl, md5sum) not found in your PATH.

  * **Solution:** Ensure that the directory where the gcc resides is in the PATH variable.

* **Error:** Not enough space on the target installation directory.

  * **Solution:** Change the target installation directory to the directory with at least 500MB free disk space.

* **Error:** <WORKING_DIRECTORY> is read-only.

  * **Solution:** You need to have write permission for the current working directory to extract the contents of the archive, configure, and build. Ensure that you turn ON write permission using chmod +w ... command.

* **Error:** md5 checksums are used to check if the packages are correctly downloaded. If they are not downloaded correctly, the system displays the message: It is not safe to install these packages, please download them again.

  * **Solution:** The installer checks the integrity of the downloaded packages. If the download is either incomplete or corrupt, download the packages again.

* **Error:** SAFplus Platform fails to start, reporting the underlying SQLite database version used is not-supported.

  * **Solution:** Use SQLite version 3.3.13 or newer. The source code can be downloaded from http://www.sqlite.org/download.html. The user can install the latest version of SQLite if the specified version is not present in this repository.

Appendix A: Installing the Prerequisites without Internet Access
----------------------------------------------------------------
Some customers do not want their evaluation system to have internet access for security purposes. If this is your situation, 
please consider temporarily enabling internet access while running the "preinstall-<os>" script. At this point the evaluation 
system should only have the base OS installed, so there is no proprietary data on the system. Also note that the "preinstall" 
scripts are only about a page long so you can easily review them for security purposes.

However, if you still do not want to enable internet access one strategy that can be used is to go to a system with internet 
access (it must use the same Linux distribution and the same version), download them there, use a USB flash drive to move them 
to the unconnected system, and then install them on that system. If this approach is unacceptable (it does still use the internet), 
then perhaps the Linux distribution you chose is not appropriate -- instead use one that contains all packages on the installation CDROMs.

Example Using Ubuntu 7.04
^^^^^^^^^^^^^^^^^^^^^^^^^
Packages can be downloaded but not installed on Ubuntu by using the "-d" flag to the "apt-get" package manager. The files are 
downloaded to "/var/cache/apt/archives". It is recommended to remove (or move) all files in this directory first (it is just a 
cache, and so it will contain any packages that you have previously installed), so that the directory contains just the packages 
needed for the OpenClovis SDK:

.. code-block:: text

    rm /var/cache/apt/archives/*

Next edit the preinstall-ubuntu.sh script, search for all instances of "apt-get" and add the flags "-d --reinstall" just after the 
"apt-get" program. For example:

.. code-block:: text

    apt-get -d --reinstall -y --force-yes install build-essential

Next run this modified script on your internet-connected machine. This script will download 6MB of files (this list will vary by 
Linux distribution or version):

* bison_1%3a2.3.dfsg-4build1_i386.deb                           
* libgdbm-dev_1.8.3-3_i386.deb
* build-essential_11.3_i386.deb                                 
* libltdl3-dev_1.5.22-4_i386.deb
* e2fslibs-dev_1.39+1.40- WIP-2006.11.14+dfsg-2ubuntu1_i386.deb  
* libperl-dev_5.8.8-7build1_i386.deb
* e2fsprogs_1.39+1.40-WIP-2006.11.14+dfsg-2ubuntu1_i386.deb     
* linux-headers-2.6.20-16-generic_2.6.20-16.32_i386.deb
* flex_2.5.33-10build1_i386.deb                                 
* gawk_1%3a3.1.5.dfsg-4build1_i386.deb                          
* gettext_0.16.1-1ubuntu2_i386.deb                              
* pkg-config_0.21-1build1_i386.deb
* libdb4.5-dev_4.5.20-1ubuntu1_i386.deb                         
* uuid-dev_1.2- 1.39+1.40-WIP-2006.11.14+dfsg-2ubuntu1_i386.deb

Now copy these files to a new directory in your unconnected machine.

On the connected machine:

.. code-block:: text

    root@desktop:/# cp /var/cache/apt/archives/*.deb <your flash media>

On the unconnected machine:

.. code-block:: text

    root@desktop:/# mkdir /root/pkgs
    root@desktop:/# cp <your flash media> /root/pkgs/

Finally, install them using the standard "dpkg" package installer:

.. code-block:: text

    root@desktop :/# cd /root/pkgs
    root@desktop:~/pkgs# dpkg -i *.deb
    (Reading database ... 113653 files and directories currently installed.)
    ...
    root@desktop:~/pkgs#

At this point, you should be done installing the prerequisites! You should now continue the installation procedure at the step 
after installing prequisites.
