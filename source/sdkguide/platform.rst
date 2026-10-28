Hardware Platform Support
=========================
The features described in the previous chapters can provide complete service without any assumption on or any special integration 
with the underlying hardware. For example, fault detection and service recovery works without direct tie between SAFplus Platform 
and the hardware. This ensures that SAFplus Platform and SAFplus-based systems are portable across a wide range of hardware, from a 
cluster of desktop PCs, rack mount servers, to carrier grade, chassis based systems and virtual hosts. However, additional 
communication between the software and the underlying hardware platform can further enhance some key characteristics of the system.

Modern hardware platforms provide a set of control and monitoring access for the software running on them. Such platforms are often 
referred to as "managed hardware platforms." Tapping into these interfaces can provide additional features or can strengthen the 
characteristics of existing features of a carrier grade middleware such as SAFplus Platform.

In order to exploit the advantages of managed hardware platforms OpenClovis provides additional Platform Support Packages (PSPs). 
The PSP realizes a direct interface between SAFplus Platform and the underlying hardware platform, using an open, standards-based 
API, the Hardware Platform Interface (HPI) defined by the Service Availability Forum. This solution preserves the hardware agnostic 
nature of SAFplus Platform.

The specific benefits of the PSP, and its realization are described in this chapter.

Benefits of the Platform Support Package
----------------------------------------
The PSP provides the following additional main benefits compared to running SAFplus Platform on an "unmanaged" hardware platform:

* Early detection of hardware anomalies and faults can be fed into the HA decision process
* Service impacting faults can trigger immediate service failover from the impacted hardware. Since these anomalies are often 
  precursors of impending hardware failures, yet the hardware may be still operational, the handling of these events provides a 
  chance to gracefully fail over the software service, thus minimizing service impact.
* Minor hardware events (no direct threat to service) can be routed to Fault Manager, which allows customized event handlers to deal 
  with the problem
* Dependency relationships between various hardware components can be described using dependency tables
* SAFplus Platform is notified in case of hot-swapping or hot removal of blades, allowing the SAFplus Platform Availability Manager 
  Framework (AMF) to fail over all services from the to-be-removed blade before the blade is powered off

In addition to the above main benefits, a few add-on tools, scripts are also included in the PSP:

* **bladeinfo utility** - this command line program provides an easy access to vital information about the host FRU. When executed on 
  an IPMI-enabled FRU (as part of the OpenClovis SAFplus Platform installation), it can display the following information: IPMI 
  address, logical slot, physical slot, slot type, board/product manufacturer, board/product name, product part number, 
  board/product serial number. This information can be readily used in other scripts to make decisions based on such information. 
  Examples of such use are:

  * Physical slot based IP addresses
  * Blade model based role selection
  * Unique blade identifier based on serial number

* **Lifesignal utility** (for AdvancedTCA blades only) - a small program that can control LED 2 on an AdvancedTCA blade to show vital 
  status information about an SAFplus-based node running on the blade. Different color and timing patterns identify different states.

.. note::
    Both bladeinfo and lifesignal require local IPMI driver on the node. In addition, bladeinfo requires IPMI over RMCP access to 
    the shelf manager in order to determine the physical slot. This requires knowledge of the IP address of the shelf manager card 
    and may also require username and password (depending on the shelf manager's configuration).

.. note::
    PSPs are available only for commercially licensed version of the OpenClovis SDK, and are not available for a GPL-licensed SDK.

For all supported hardware platforms, OpenClovis conducts a series of integration tests to verify correct operation. As there are 
slight variations in how chassis from different vendors work, sometimes small adjustments are needed in the software. At the time 
of the release of OpenClovis SDK 3.0, a single Platform Support Package, called "OpenClovis Common PSP" contains all such adjustments. 

.. seealso::
    For the list of hardware platforms supported by the Common PSP, please turn to the **OpenClovis Release Notes**.

As OpenClovis integrates with additional platforms over time, additional changes/extensions may be packaged into separate, platform 
specific PSPs.

How to Work With PSPs
---------------------
The following topics are covered here:

* How to install PSP(s)
* How to build SAFplus Platform to include platform management
* What to expect when running SAFplus Platform on the target

How to install PSP(s)
^^^^^^^^^^^^^^^^^^^^^
As noted above, PSPs are offered only for commercially licensed version of OpenClovis SDK. PSPs are packaged separately and need to 
be installed separately on the development host.

The installation process is as follows:

#. (Prerequisite) Complete the OpenClovis SDK installation as directed in the **OpenClovis Installation Guide**
#. Fetch/download the OpenClovis Common PSP (file name is openclovis-sdk-3.0*-psp-common*.tar.gz) and optionally the MD5 signature 
   file (openclovis-sdk-3.0*-psp-common*.md5) into an arbitrary directory
#. File integrity can be verified by running md5sum on the .tar.gz file and comparing its output with the content of the .md5 file. 
   This step is optional. Example:

   .. code-block:: bash

        md5sum -c openclovis-sdk-3.0-psp-common.md5

   This should report OK.

#. Untar the .tar.gz file by running (example):

   .. code-block:: bash

        tar xmf openclovis-sdk-3.0-psp-common.tar.gz

   This will create a subdirectory called openclovis-sdk-3.0-psp-common.

#. Enter the newly created subdirectory and initiate installation. If you installed the OpenClovis SDK as root, you will need to 
   install the PSP also as root.

   .. code-block:: bash

        cd openclovis-sdk-3.0-psp-common
        ./install

#. Follow the install script directions to complete the installation. The install script will prompt for the SDK installation root 
   directory. By default this will be the place where you last installed SAFplus Platform using the same user account that you are 
   using now. Therefore, in most cases the default can be accepted. Otherwise, please specify the proper location. If all went well, 
   the install script will report **installation completed**.

Additional steps
""""""""""""""""
For SAFplus Platform to communicate with the hardware, it needs to be built with using the proper HPI client library for the given 
hardware platform. The Common PSP supports the following HPI client libraries:

* Radisys libhcl (version 1.1 or 1.4.4) used for Radisys Promentum-6000 and 6010 AdvancedTCA chassis
* OpenHPI daemon and client libraries (version 2.8.0 and above) used for chassis that utilize the Pigeon Point Systems (PPS) Shmm 
  500 shelf manager module (Sentry). The OpenClovis Common PSP has been tested with both the open source version as well as the 
  PPS-provided commercial version of OpenHPI.

If you intend to use the open-source version of OpenHPI, no additional special installation steps are necessary as it is installed by default during the SDK installation.

If you intend to use Pigeon Point System's OpenHPI package, please follow these steps:

#. Consult with your Pigeon Point Systems representative or your chassis vendor to obtain the source package of Pigeon Point OpenHPI
#. If your target OS is Wind River PNE LE 1.4, please follow the instructions in the SDK Guide, Section "Building SAFplus Platform 
   and SAFplus Platform Based Systems", Sub-section "Using OpenClovis SDK with Wind River Workbench" to generate a cross-build 
   toolchain which integrates the Pigeon Point OpenHPI.
#. For any other target OS, please contact an OpenClovis field engineer for further support.

If you intend to use the Radisys libhcl client, please follow these steps:

#. Make sure you have the libhcl software package (named as libhcl-1.4.4.tar.gz or similar). If you do not have it, consult with 
   your Radisys representative to obtain the package.
#. If your target OS is Wind River PNE LE 1.4, please follow the instructions in the SDK User Guide, Section "Building SAFplus 
   Platform and SAFplus Platform Based Systems", Sub-section "Using OpenClovis SDK with Wind River Workbench" to generate a 
   cross-build toolchain which integrates the libhcl library.
#. For any other target OS, please contact an OpenClovis field engineer for further support.

How to build SAFplus Platform to include platform management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The PSP installation by itself does not make subsequent builds to include platform support. When configuring SAFplus Platform, you 
need to explicitly request the build to include platform support. Once your project is configured to use platform management, all 
subsequent builds will create and package the additional binaries.

Configuring SAFplus Platform to use platform management can be done either from the IDE or from the command line:

* From the IDE, use the **Project > Build Project** menu to bring up the **Build Configuration** dialog, enable **"Include Chassis 
  Manager for HPI Access"** option and select the proper HPI client library type. Click **OK**. All subsequent builds will contain 
  platform support.
  
  .. seealso::
    For further details, check the **OpenClovis IDE User Guide**, Section "Building the Project."

* Alternatively, the same can be achieved from the command line. Go to the top level directory of your project area, and re-issue 
  the configure step, this time with using the **--with-cm-build[=mode]** option, where mode is either openhpi or libhcl. If the mode 
  is omitted, it defaults to openhpi.
  
  .. seealso::
    For more information, check Section **Building SAFplus Platform and SAFplus-based Systems**.

Next, during the packaging step you need to specify a few additional information, such as IP address of the shelf manager and (for 
Pigeon Point based hardware platforms) the user credentials to access the shelf manager. This can be done either from the IDE or 
from the command line:

* For the IDE based process, check the **"Making Project Images"** in the **OpenClovis IDE User Guide**. Please note that for 
  Radisys chassis using the libhcl client library only the shelf manager's IP address needs to be provided, the remaining three fields 
  (Module IP, Username, and Password) should be left blank. For platforms using the openhpi libraries all four fields need to be 
  provided. The last three fields must correspond to a valid user account defined on the shelf manager. The user account must have 
  Administrator privileges. Note: do not use the "openhpi" user account, as that disables the default hot-swap operation of the shelf 
  manager. Once the IDE dialog is properly completed, the IDE will generate/update the **target.conf** configuration file under the 
  model's src subdirectory and will complete the packaging with the correct information.

  .. seealso::
    you can check the **"Making Project Images"** in the **OpenClovis IDE User Guide**

* Alternatively, the same result can be achieved by editing the corresponding four fields in the **target.conf** configuration file 
  mentioned above with a text editor. Once the values are specified in **target.conf**, any subsequent make images operation will 
  correctly embed this information to the run-time images.

For those who are interested in the details, the make images step uses the platform management settings from the target.conf file 
in two ways:

* For openhpi based systems, it generates the proper openhpi.conf file as part of the target image
* For libhcl based systems, it properly defines the **SAHPI_UNSPECIFIED_DOMAIN_ID** environment variable which is used to convey the IP 
  address of the shelf manager to the libhcl client library.

What to expect when running SAFplus Platform on the target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The active presence of the Platform Support Package will result in the following new behavior (compared to a system with no PSP):

* On each system controller node an additional middleware component, the Chassis Manager (CM, processo asp_cm) will be installed and 
  started when SAFplus Platform starts.
* The booting time of CM depends on the underlying shelf manager technology. On some shelves the HPI discovery time can take 
  significant amount of time (20-40 seconds). CM will wait till the discovery completes before it send its readiness signal to the 
  availability manager. Consequently the boot time of SAFplus Platform may be longer.
* A major or critical HPI event on a server FRU (that runs SAFplus Platform) will trigger SAFplus Platform to preventively remove 
  all service assignments from the problematic FRU. In case the HPI event is de-asserted later, the services will be re-assigned to 
  the recovered FRU. (Indirect FRU dependencies can be modeled during design time by extending the FRU dependency table used by CM.)
* Upon an extraction request event (triggered either by manually opening the ejection latches/levers of an AdvatncedTCA blade or 
  other FRU, or requesting such event via the shelf manager or HPI interface), CM will notify AMF about such event, and AMF will 
  immediately remove the services from the given FRU. In case of redundant setup, the services will be switched over to other FRUs. 
  Then, SAFplus Platform will allow normal OS shutdown to take place. Upon completion of the OS shutdown process, the blade will be 
  powered down as usual, hence reaching the deactivated state, allowing the removal of the FRU. Please note that once the shutdown 
  process is started, closing the latch will not reverse the process: the blade will be inactivated. Once the inactive state is 
  reached, the FRU can be freely removed or it can be re-activated by opening and closing the latches.
* If a minor HPI event is detected by CM, it will be processed using customized callback functions, if provided. Callback functions 
  can be specific to FRU types and instances. The default behavior is to ignore all minor events.











