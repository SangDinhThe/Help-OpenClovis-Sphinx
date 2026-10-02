Building the Evaluation System and Deploying Runtime Images
===========================================================
This chapter logically follows from the Installation Guide where we installed the OpenClovis SAFplus Platform SDK. The following 
sections use the term <install_dir> to refer to the directory in which the SAFplus Platform SDK was installed. By default, this 
directory is /opt/clovis for root installation and $HOME/clovis for non root users. The following sections describe how to build 
the evaluation model and deploy the runtime images so that we can run them and observe their behavior.

Building the Target Images
--------------------------
This section describes the steps to:

* Create a project area
* Modify OpenClovis sample applications
* Build SAFplus Platform and the Evaluation System
* Setup a configuration file to run any of the six Hardware Setups 1.1 to 2.3
* Create the target image.

Creating a Project Area
-----------------------
To work with the OpenClovis SDK Evaluation System, you will need to use the example project area provided with the SDK. A project 
area is designed to hold multiple models which share the SAFplus Platform source tree within the SDK installation.

#. If you have write access to the examples area of the <install_dir> you can simply use this as you project area. In this case 
   your **<project_area>** would be **<install_dir>/6.1/sdk/src/examples**.
#. If you do not have write access to **<install_dir>/6.1/sdk/src/examples** create a new directory and copy the evaluation system 
model to it. For example:

   .. code-block:: text

      $ mkdir <new_project_area>
      $ cp -r <install_dir>/6.1/sdk/src/examples/eval <new_project_area>/.

   In this case your **<project_area>** would be **<new_project_area>**.

In either case your **<project_area>** should have the following directory structure:

.. code-block:: text

    <project_area>
        |ide_workspace
        |+eval
        |   |+build
        |   |   |+local
        |   |   |   |-Makefile
        |   |+src
        |   |   |+app
        |   |   |+config
        |   |   |+doc
        |   |   |-target.conf
        |   |-Makefile
        |-Makefile

Modifying the Clovis Sample Applications
----------------------------------------
We have provided the option to modify and rebuild the supplied sample applications.

#. Modifying sample application code as you see fit:

   The Clovis Sample Application's are located in: **<project_area>/eval/src/app**

   The source files for the sample application components csa101comp to csa113comp are listed here. Make the necessary alteration to 
   the csa files.

#. Build the single/distributed target images, as discussed below.

Building SAFplus Platform and the Evaluation System
---------------------------------------------------
The next step is to build both SAFplus Platform and the evaluation model in the existing project area.

Configure the eval model
^^^^^^^^^^^^^^^^^^^^^^^^
Configure the eval model for building by running the following:

.. code-block:: text

    $ cd <project_area>
    $ <install_dir>/6.1/sdk/src/SAFplus/configure --with-model-name=eval --with-safplus-build

It is possible to use prebuilt libraries to configure eval model by running the following:

.. code-block:: text

    $ cd <project_area>
    $ <install_dir>/6.1/sdk/src/SAFplus/configure --with-model-name=eval --with-safplus-build

It is also possible to configure the eval model without configure option --with-model-name, but without using prebuilt libraries 
by running the following:

.. code-block:: text

    $ cd <project_area>/eval
    $ <install_dir>/6.1/sdk/src/SAFplus/configure --with-safplus-build

With reference to above mentioned different configure options, we can configure eval model, by running the following:

.. code-block:: text

    $ cd <project_area>/eval
    $ <install_dir>/6.1/sdk/src/SAFplus/configure

These all options will configure the eval model for deployment on the local machine.

In order to crossbuild this model for deployment on a non-native target supported by the <crossbuild> toolchain, run:

.. code-block:: text

    $ <install_dir>/6.1/sdk/src/SAFplus/configure \
        --with-model-name=eval --with-safplus-build \
        --with-cross-build=<crossbuild>

It is possible to configure the model to be built for multiple targets by issuing as many configure commands as necessary. Each 
run sets up a target-specific build location at <project_area>/eval/build.

If this model is to be deployed on an ATCA-based system with OpenHPI-based shelf management, enable Chassis Management with:

.. code-block:: text

    $ <install_dir>/6.1/sdk/src/SAFplus/configure \
        --with-model-name=eval --with-safplus-build \
        --with-cross-build=<crossbuild> --with-cm-build=openhpi

For a complete list of options to configure, including a list of available crossbuild toolchains, run:

.. code-block:: text

    $ <install_dir>/6.1/sdk/src/SAFplus/configure --help

If the necessary crossbuild toolchain does not exist, then you must install it by downloading it adjacent to the OpenClovis SDK 
installer and re-running install.sh.

The configure step prepares the project area to build the eval model, with the following directory structure:

.. code-block:: text

    <project_area>
        |ide_workspace
        |+eval
        |   |+build
        |   |   |+local
        |   |   |   |-Makefile
        |   |   |+<crossbuild>
        |   |   |   |-Makefile
        |   |+src
        |   |   |+app
        |   |   |+config
        |   |   |+doc
        |   |   |-target.conf
        |   |+target 
        |   |-Makefile
        |-Makefile

Build the configured model
^^^^^^^^^^^^^^^^^^^^^^^^^^
Build the configured model by issuing make in **<project_area>/eval**:

.. code-block:: text

    $ cd <project_area>/eval
    $ make

This will build the eval model for all the targets it has been configured to build. In order to do a target-specific build, issue 
make from the target-specific build location. e.g. for a local build:

.. code-block:: text

    $ cd <project_area>/eval
    $ make

For a target supported by the <crossbuild> toolchain:

.. code-block:: text

    $ cd <project_area>/eval/build/<crossbuild>
    $ make

For a complete list of options to make, run:

.. code-block:: text

    $ make help

The model source is located at <project_area>/eval/src. If any changes are made to this, rebuild the model by issuing another make 
from either the target-specific build location or the top project area directory.

Configuration File - target.conf
--------------------------------
Now that the code has been built we are almost ready to build images for deployment to our hardware. But first we must define the 
target system's configuration so that we build the correct images. A model's target system configuration is specified using a 
configuration file - target.conf. It is located at <project_area>/eval/src/target.conf. Open this file using your favorite editor 
(e.g. vi):

.. code-block:: text

    $ vi <project_area>/eval/src/target.conf

This file specifies a number of parameters that need to be defined for a given run-time target:

#. **TRAP_IP** (Mandatory): Specifies where the SNMP SubAgent should send traps at runtime. If you do not have an SNMP SubAgent in 
   your model specify 127.0.0.1 as the value. e.g.:

   TRAP_IP=127.0.0.1

#. **CMM_IP** (Mandatory if deployed on an ATCA chassis): Specifies the IP address of the target system's chassis management module 
   or shelf manager. If you are running Hardware Setup 2.1, 2.2 or 2.3 involving PC(s)/Laptop(s) then do not define this variable. 
   ATCA chassis Example:

   CMM_IP=169.254.1.2

#. **CMM_USERNAME** and **CMM_PASSWORD** (Mandatory if deployed on an ATCA chassis): Specifies the username and password required 
   for the OpenClovis SAFplus Platform Chassis Manager to connect to the target system's chassis management module. e.g.:

   CMM_USERNAME=root

   CMM_PASSWORD=password

#. **INSTALL_PREREQUISITES=YES|NO** (Mandatory): Specifies whether the target images will include 3rd party runtime prerequisites 
   or not. Say YES if the target nodes do not meet the target host requirements specified in the Installation section of this document. 
   e.g.:

   INSTALL_PREREQUISITES=YES

#. **INSTANTIATE_IMAGES=YES|NO** (Mandatory): Specifies whether make images will generate node-instance specific images instead of 
   only generating node-type specific images. This option is a development optimization for advanced users of OpenClovis SDK. 
   If unsure, say YES. e.g.:

   INSTANTIATE_IMAGES=YES

#. **CREATE_TARBALLS=YES|NO** (Mandatory): Specifies whether the node-instance specific images created will be packaged into 
   tarballs for deployment onto the target system. If unsure, say YES. e.g.:

   CREATE_TARBALLS=YES

#. **TIPC_NETID** (Mandatory): Specifies a unique identifier used by TIPC to set up interprocess communication across the deployed 
   OpenClovis SAFplus Platform cluster. This is an unsigned 32-bit integer, and must be unique for every model that is deployed. e.g.:

   TIPC_NETID=1337

#. **Node Instance Details**: These specify the node-instance specific parameters required for deploying the model. For each node 
   in the model there is a corresponding entry in the file:

    #. **SLOT_<node instance name>** (Mandatory): Specifies which slot the node is located in. The first slot is slot 1 -- DO NOT 
       USE SLOT NUMBER 0, it is invalid. When deployed to an ATCA chassis, the physical slot in which the blade is actually installed 
       will override this value. When deployed to regular (non-ATCA) systems, this is a logical slot and must be unique for every node 
       in the cluster. e.g.:
    
       SLOT_SCNodeI0=1
    
    #. **LINK_<node instance name>** (Optional): Specifies the ethernet interface used by the node for OpenClovis SAFplus Platform 
       communication with the rest of the cluster. If unspecified, this defaults to eth0. e.g.:
    
       LINK_SCNodeI0=eth0
    
    #. **ARCH_<node instance name>** (Optional if **ARCH** is specified): Specifies the target architecture of the node as a 
       combination of machine architecture (MACH) and linux kernel version. This is only required on a per-node basis if the target 
       cluster has heterogeneous architectures across the nodes. If it is a homogeneous cluster, a single ARCH parameter (described 
       below) will suffice. e.g.:
    
       ARCH_SCNodeI0=i386/linux-2.6.14
    
    #. **ARCH** (Optional if node-specific **ARCH_** parameters are specified): Specifies the target architecture of all nodes in a 
       homogeneous cluster as a combination of machine architecture (MACH) and linux kernel version. Note: The build process automatically 
       populates this variable based on the last target the model is built for.e.g.:
    
       ARCH=i386/linux-2.6.14

    For example, if we have a three-node cluster with the following details:

    +-----------------+-------------+----------------+-------------------+
    | Node Name       | Slot Number | Link Interface | Architecture      |
    +=================+=============+================+===================+
    | SCNodeI01       | 01          | eth0           | i386/linux-2.6.14 |
    +-----------------+-------------+----------------+-------------------+
    | PayloadNodeI03  | 03          | eth0           | i386/linux-2.6.14 |
    +-----------------+-------------+----------------+-------------------+
    | PayloadNodeI14  | 14          | eth1           | ppc/linux-2.6.9   |
    +-----------------+-------------+----------------+-------------------+

    .. raw:: html

        <style>
            .center {text-align: center;} 
        </style>

    .. rst-class:: center

    **Example Node Instance Detail**

    we would specify the node instance details as:

    .. code-block:: text

        SLOT_SCNodeI0=1
        SLOT_PayloadNodeI0=3
        SLOT_PayloadNodeI1=4

        LINK_SCNodeI0=eth0
        LINK_PayloadNodeI0=eth0
        LINK_PayloadNodeI1=eth1

        ARCH_SCNodeI0=i386/linux-2.6.14
        ARCH_PayloadNodeI0=i386/linux-2.6.14
        ARCH_PayloadNodeI1=ppc/linux-2.6.9

Evaluation Kit 'Node Instance Details' Examples
-----------------------------------------------
The 'Node Instance Details' of your target.conf file will be different depending on the hardware setup you are using for your 
evaluation. Below are some example settings for the various hardware setups.

#. If you are using single node case as in Hardware Setup 1.1 or 2.1, either using one blade or PC, you set up similar to the 
   following configuration details. Change the slot number accordingly.

   SLOT_SCNodeI0=1

#. If you wish to set up a 3 node distributed system, as in Hardware Setup 1.2 or 2.2, your target.conf file may be set up similar 
   to the following configuration details. Again change the slot numbers accordingly.

   SLOT_SCNodeI0=1

   SLOT_PayloadNodeI0=2

   SLOT_PayloadNodeI1=3

#. If you are setting up a 4 node distributed system, as in Hardware Setup 1.3 or 2.3, you would use a configuration that is 
   similar to the following details.

   SLOT_SCNodeI0=1

   SLOT_SCNodeI1=2

   SLOT_PayloadNodeI0=3

   SLOT_PayloadNodeI1=4

Building Single/Distributed Target Image(s)
-------------------------------------------
This section describes how to build target images for particular Hardware Setups. In essence we provide two types of target image, 
the System Controller or Payload Node. The images are built with the make images command:

.. code-block:: text

    $ cd <project_area>/eval
    $ make images

If target.conf has been configured to instantiate images and create tarballs as recommended, these are populated at 
<project_area>/target/eval/images. Each node-specific image is provided as a directory containing the run-time files (binaries, 
libraries, prerequisites, and configuration files) as well as a tarball with the same content. e.g. For a model containing three 
nodes: SCNodeI0, PayloadNodeI0 and PayloadNodeI1, the following are the files and directories generated for deployment on the 
run-time system.

.. code-block:: text

    <project_area>
        |+target
            |+<model>
                |+images
                    |+SCNodeI0
                    |   |+bin
                    |   |+etc
                    |   |+lib
                    |   |+var
                    |-SCNodeI0.tgz
                    |+PayloadNodeI0
                    |-PayloadNodeI0.tgz
                    |+PayloadNodeI1
                    |-PayloadNodeI1.tgz

Content of Target Images
------------------------

Content of Single Node Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you chose to create a single node setup then the following directory structure is created. Note it is not the exhaustive directory 
structure but instead highlights directories and files of importance.

.. code-block:: text

    <project_area>target/eval/images/
        |-target
            |
            |-eval
            |   |images
            |   |   |-generic
            |   |   |   |+bin
            |   |   |   |+etc
            |   |   |   |+lib
            |   |   |   |+modules
            |   |   |   |+share
            |   |   |
            |   |   |-SCNodeI0
            |   |   |   |+bin
            |   |   |   |+etc
            |   |   |   |+lib
            |   |   |   |+modules
            |   |   |   |+share
            |   |   |
            |   |   |-SCNodeI0.tgz

The images directory contains everything required to deploy SAFplus Platform on the chosen runtime setup. In this case, a generic 
node image and one created specifically for SCNodeI0 are created, both containing the following:

* **bin**

  contains executable binaries and scripts, such as asp_amf, asp_console and csa101.

* **etc**

  contains XML and text configuration files for SAFplus Platform and third-party tools, as well as an init.d style script to 
  start/stop SAFplus Platform

* **lib**

  libraries, including 3rd party dependencies, required by the sample applications

* **modules**

  kernel modules (ioc, alarm)

* **share**

  contains snmp & mib information

**SCNodeI0**

Contains the System Controller image to be used for the single node case. This image is to be copied to the target platform.

Content of 3 Node Distributed Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we are building the distributed Evaluation System, additional images for PayloadNode0 and PayloadNode1 are now utilized and 
this is represented within the content of the directory structure. (When compared to the single node set up, the bold directories/files 
represent the difference in file structure).

.. code-block:: text

    <project_area>target/eval/images/
        |-target
            |
            |-eval
            |   |images
            |   |   |+generic
            |   |   |
            |   |   |-PayloadNodeI0
            |   |   |   |+bin
            |   |   |   |+etc
            |   |   |   |+lib
            |   |   |   |+modules
            |   |   |   |+share
            |   |   |-PayloadNodeI0.tgz
            |   |   |
            |   |   |-PayloadNodeI1
            |   |   |   |+bin
            |   |   |   |+etc
            |   |   |   |+lib
            |   |   |   |+modules
            |   |   |   |+share
            |   |   |-PayloadNodeI1.tgz
            |   |   |
            |   |   |+SCNodeI0
            |   |   |-SCNodeI0.tgz

**PayloadNode0 & PayloadNode1**

These additional directories are required for a distributed setup and have a similar structure to SCNodeI0. PayloadNodeI0.tgz and 
PayloadNodeI1.tgz are the corresponding zipped tar images that are to be copied to the target Payload nodes.

There is nothing special about which node should be the System Controller verses a Payload Node, or which node should be Payload 
Node 0 verses Payload Node 1. You may copy any tar image to any node -- the contents of the tar image will make the node assume 
the role. The only exception is, of course, an environment that contains different hardware, for example, an Intel-based machine 
and a PowerPC based machine. In that case you need to define your ARCH variables correctly (see above) and deploy images only to 
matching hardware.

Content of 4 Node Distributed Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If we are building the 4 node distributed Evaluation System, the additional image SCNodeI1 is now created and this is represented 
within the content of the directory structure. (When compared to the 3 node distributed set up, the bold directories/files represent 
the difference in file structure)

.. code-block:: text

    <project_area>target/eval/images/
        |-target
            |-eval
            |   |images
            |   |   |+generic
            |   |   |
            |   |   |+PayloadNodeI0
            |   |   |-PayloadNodeI0.tgz
            |   |   |+PayloadNodeI1
            |   |   |-PayloadNodeI1.tgz
            |   |   |+SCNodeI0
            |   |   |-SCNodeI0.tgz
            |   |   |
            |   |   |-SCNodeI1
            |   |   |   |+bin
            |   |   |   |+etc
            |   |   |   |+lib
            |   |   |   |+modules
            |   |   |   |+share
            |   |   |
            |   |   |-SCNodeI1.tgz

**SCNodeI1**

These additional directories are required for a distributed setup and have a similar structure to SCNodeI0. SCNodeI1.tgz is the 
corresponding zipped tar image that needs to be copied to the second System Controller.

Runtime Software Installation
-----------------------------
The hardware setups require steps to copy the runtime images from the Development Machine to the Runtime target machine(s). The 
following describe the necessary steps required to copy runtime images to the desired target(s).

Installing SCNodeI0
^^^^^^^^^^^^^^^^^^^

#. On the Development Machine locate the target images

   .. code-block:: text

      $ cd <project_area>/target/eval/images

#. Copy the zipped tar System Controller image to the desired target.

   .. code-block:: text

      $ scp SCNodeI0.tgz root@<SystemController IPAddress>:/root/

   Enter password.

   .. code-block:: text

      # ssh root@<SystemController IPAddress>

   Enter password

   .. code-block:: text

      # cd /root
      
      # mkdir asp
      
      # cd asp
      
      # tar xzvf ../SCNodeI0.tgz

   This unzips and extracts the contents of SCNodeI0.tgz within /root/asp. The System Controller is now installed on the target.

   .. note::
      This step is necessary even if the System Controller and Management Machine are the same PC (As in Runtime Hardware Setup 2.1)

   If you are setting up a 4 node distributed setup, as in 'Runtime Hardware Setup 1.3.' repeat the above steps, replacing the IP 
   address with SCNodeI1's and securely copying SCNodeI1.tgz.

Installing PayloadNode0 and PayloadNode1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Perform the following, if the distributed Hardware Setup 1.2, 1.3, 2.2 and 2.3 is chosen:

#. On the Development machine locate the Target images
   .. code-block:: text

      $ cd <project_area>/target/eval/images

#. Copy the zipped tar PayloadNode0 image to the desired target.

   .. code-block:: text

      $ scp PayloadNodeI0.tgz root@<PayloadNode0 IPAddress>:/root/

   Enter password.

   .. code-block:: text

      # ssh root@<PayloadNode0 IPAddress>

   Enter password

   .. code-block:: text

      # cd /root
      # mkdir asp
      # cd asp
      # tar xzvf ../PayloadNodeI0.tgz

   This unzips and extracts the contents of PayloadNodeI0.tgz within /root/asp The PayloadNode0 is now installed on its target. 
   For PayloadNode1 repeat the above 2 steps, replacing the IP address with PayloadNode1's and securely copying PayloadNode1.tgz.

Summary and Next Steps
----------------------
This chapter covers a number of possible hardware configurations and the steps required to build and install the target images. 
Chapter **Sample Applications**, covers all the Evaluation applications that can be run. For each Sample Application, a description on 
its objective, what you will learn, key areas of code, how to run it, sample output and conclusion is provided.
