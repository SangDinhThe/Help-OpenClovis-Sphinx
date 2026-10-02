Preface
=======
To help users gain a better understanding of our product the OpenClovis Evaluation System User Guide introduces sample applications 
that utilise the OpenClovis Application Services Platform (SAFplus Platform). It provides all the required information to configure 
and run the sample applications (or "models") packaged within the Evaluation System. This document also provides a good understanding 
of OpenClovis SAFplus Platform functionality.

This document does not cover the creation of the models through the OpenClovis IDE. For a detailed description of how to create the 
first example model in the OpenClovis IDE see the OpenClovis Sample **Application Tutorial** document.

Audience
--------
The OpenClovis Evaluation System User Guide is intended for individuals who wish to gain an understanding of the OpenClovis SAFplus 
Platform. If you wish to run this Evaluation System this document assumes you have installed the OpenClovis SAFplus Platform by 
following the installation steps found within the OpenClovis Installation Guide

Definitions
-----------
Throughout this document the term "node" is used generically to refer to either a PC, laptop or ATCA blade. Several nodes all 
running the OpenClovis SAFplus Platform combine to form one tightly coupled distributed computing environment called a "cluster". 
The number and configuration of these nodes and the applications that are running on them together form the "system model", or just 
"model". In summary the term "SAFplus Platform" denotes the common OpenClovis programs and libraries running on all nodes in the 
cluster, while the term "model" denotes all of the user applications.

Related Documents
-----------------
For additional information about OpenClovis products, refer to the following guides:

* **OpenClovis Release Notes** provides information about the software and the hardware required to install OpenClovis Application Service Platform (SAFplus Platform) and Integrated Development Environment (IDE). It contains the additional features and enhancements of the product since the previous release. It also summarizes the issues and limitations of the product and provides workarounds wherever applicable.
* **OpenClovis SA Forum Compliance** describes the level of compliance of OpenClovis SAFplus Platform and its Application Programming Interface (API) with the relevant Service Availability Forum Specifications.
* **OpenClovis Installation Guide** provides the system requirements, installation procedure for OpenClovis SAFplus Platform, IDE, and the Evaluation System.
* **OpenClovis Sample Application Tutorial** provides the steps to create and build a sample model using OpenClovis IDE and OpenClovis SAFplus Platform. It also provides troubleshooting information for this process. This provides the logical first step in understanding the OpenClovis offering.
* **OpenClovis SDK User Guide** provides information about OpenClovis Application Service Platform (SAFplus Platform) architecture, various OpenClovis SAFplus Platform components, and their interactions. This guide helps you to configure the OpenClovis SAFplus Platform components, compile, and execute the OpenClovis SAFplus Platform code to build your custom application.
* **OpenClovis IDE User Guide** describes the usage of Integrated Development Environment (IDE), a graphical development environment that complements the SAFplus Platform platform. This guide helps you to understand how to use the various features of the IDE to build the application.
* **OpenClovis Log Tool User Guide** provides information about the usage of OpenClovis Log Tool. OpenClovis Log Tool is an interactive utility that allows you to view binary log files in a readable format and hence monitor system errors, warnings, and other log information. Log Tool allows you to format the .log files and filter them to view the required entries.
* **OpenClovis API Reference Guide** is provided for each component. It describes the Application Programming Interface (API), Service Model, and Management Information Model of the various OpenClovis Application Service Platform (SAFplus Platform) services. It helps the developer to understand the capabilities of the SAFplus Platform services and the APIs provided by these services.
* **OpenClovis SAFplus Platform Console Reference Guide** provides details about managing applications built on OpenClovis SAFplus Platform using the SAFplus Platform runtime debug console commands. SAFplus Platform Console commands can be used to manage, monitor, and test your application.
* **Clovis Sample Application** (csa) source code

  For all sample applications provided with this Evaluation System, their source code has been provided within:

  <install_dir>/6.1/sdk/src/examples/eval/src/app/
* **Service Availability Forum** (SAF) - `saforum.org <https://www.associationvoice.com/Page/16627~217631/ErrorNotFoundhttpswwwassociationvoicecom443Service-Availability-Forum-E28093-Frequently-Asked-Questions-FAQ/>`__
  
  Further SA Forum information can be found by clicking
  
  Specifications -> Download Specifications.
  
  Here you will be presented with a number of documents. Further information concerning Components, Service Instances, Service Groups, Component Service Instances can be found within the document 'SA Forum Specification Overview Document'.

When the SDK is installed, these documents can be found within

.. code:: text

    <install_dir>/6.1/sdk/doc

As mentioned previously in the OpenClovis Installation Guide. The default directory for installation is /opt/clovis for root installation 
and $HOME/clovis for non root users. Throughout this document we will use <install_dir> to refer to the installation directory.

References to Linux Distributions
---------------------------------
Throughout this document we refer constantly to the Linux Distribution (distro) or similar. Our SDK works on Ubuntu 7.04 and above, 
and is known to work on a wide range of Linux 2.6 and above distributions. We are committed to supporting any Linux distribution 
that our customers require.

OpenClovis Online Technical Support
-----------------------------------
OpenClovis customers and partners can register on our Web site and receive personalized services and information. If you need any 
support or assistance while working on OpenClovis products, you can access the following: `openclovis.com <https://www.openclovis.com/>`__. 
Send your queries to: support@openclovis.com. Open source community support is available at: `openclovis.org/forum <http://www.openclovis.org/forum/>`__.

Documentation Feedback
----------------------
We are interested in hearing from our customers on the documentation provided with the product. Let us know your comments and 
suggestions on improving the documentation at OpenClovis Inc. Send your comments to: support@openclovis.com. Or even better, 
edit (or comment in) the page on our documentation wiki located at `help.openclovis.com <http://help.openclovis.com/>`__.
