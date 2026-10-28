Preface
=======
OpenClovis Integrated Development Environment (IDE) User Guide provides information about the usage of OpenClovis IDE, a graphical 
development environment from OpenClovis Inc. that complements the OpenClovis platform. This guide helps you to configure, compile, 
and execute OpenClovis IDE to build the application. OpenClovis IDE is designed to simplify and accelerate the development of 
Telecom application software over OpenClovis platform. It provides a simple and powerful mechanism with easy drag-and-drop features, 
to create Resources and Components, and define the attributes and relationships between them. OpenClovis IDE graphical interface 
enables you to capture the Information Models through UML notations and save them as XML files.

Audience
--------
OpenClovis IDE Guide is designed for system integrator's, designers, and system architects. To use the product, you must be aware of 
the fundamentals of design, development, operation, management and configuration of telecommunication and networking systems. You 
must also be familiar with C programming, UML notations, and have the basic knowledge of Linux.

Document Organization
---------------------
This guide is organized into various chapters to provide information on speci?c areas. The following table introduces the chapter 
names and a brief overview of the content

+-----------------------------------+------------------------------------------------------------------------+
| Chapter                           | Overview                                                               |
+===================================+========================================================================+
| **Chapter 1**, Introduction to    | This chapter helps you understand the conceptual information,          |
|                                   |                                                                        |
| OpenClovis IDE                    | advantages and key features of OpenClovis ASP and IDE.                 |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 2**, Getting Started    | This chapter provides information to launch and access IDE, create     |
|                                   |                                                                        |
|                                   | a workspace and a project.                                             |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 3**, Understanding      | This chapter provides information about the IDE work                   |
|                                   |                                                                        |
| the User Interface                | environment.                                                           |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 4**, Setting Resource   | This chapter provides information about the properties that you        |
|                                   |                                                                        |
| Properties                        | can specify for the chassis, node hardware, hardware, and              |
|                                   |                                                                        |
|                                   | software resources in the Resource Editor.                             |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 5**, Defining Alarm     | This chapter provides information about defining alarms to map to      |
|                                   |                                                                        |
| Profiles                          | the resources.                                                         |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 6**, Setting Component  | This chapter provides information about the parameters that you        |
|                                   |                                                                        |
| Properties                        | can specify for the various components in the Component Editor.        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 7**, Configuring ASP    | This chapter provides information about configuring ASP                |
|                                   |                                                                        |
| Components                        | components within IDE.                                                 |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 8**, Configuring AMF    | This chapter provides information to create the instances of the       |
|                                   |                                                                        |
|                                   | entities defined in a Component Editor using AMF Configuration.        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 9**, Configuring and    | This chapter provides information about configuring and allocating     |
|                                   |                                                                        |
| Allocating Memory                 | memory configuration profiles to the various ASP components and        |
|                                   |                                                                        |
| Configuration Profiles            | the SAF components.                                                    |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 10**, Creating and      | This chapter provides information about creating and using the         |
|                                   |                                                                        |
| Using Template Groups             | template groups to generate the source code.                           |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 11**, Defining IDL      | This chapter provides information about creating the IDL XML file      |
|                                   |                                                                        |
|                                   | that is used by the IOC links to provide communication between         |
|                                   |                                                                        |
|                                   | two or more components.                                                |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 12**, Generating        | This chapter provides information about generating the source          |
|                                   |                                                                        |
| Source Code                       | code after you have completed building the model.                      |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 13**, Building the      | This chapter provides information about configuring and building       |
|                                   |                                                                        |
| Project                           | the project after you have completed generating the source code.       |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 14**, Making Project    | This chapter provides information about generating run-time            |
|                                   |                                                                        |
| Images                            | images for a target system.                                            |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 15**, XML Representation| This chapter describes the organization and content of the XML         |
|                                   |                                                                        |
| of the Model                      | files which are part of the Open Clovis project that can be read       |
|                                   |                                                                        |
|                                   | by the IDE and also Command Line Tools.                                |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 16**, Creating and      | This chapter provides information about how to create and build        |
|                                   |                                                                        |
| Building openSAF Project          | the openSAF project.                                                   |
|                                   |                                                                        |
| in IDE                            |                                                                        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 17**, Creating and      | This chapter provides information to create, use, export, and          |
|                                   |                                                                        |
| Using Model Templates             | import model templates.                                                |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 18**, Application       | This chapter provides information about Application                    |
|                                   |                                                                        |
| Import/Export                     | Import/Export feature provided by OpenClovis IDE.                      |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 19**, Limitations       | This chapter provides information about the limitations of IDE.        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 20**, Glossary of Terms | This provides complete information about all the terms and             |
|                                   |                                                                        |
|                                   | definitions specific to Open Clovis IDE.                               |
+-----------------------------------+------------------------------------------------------------------------+

Related Documents
-----------------
For additional information about OpenClovis products, refer to the following guides:

* **SAFplus Platform Release Notes** provides information about the software and the hardware required to install OpenClovis Application 
  Service Platform (SAFplus Platform) and Integrated Development Environment (IDE). It summarizes the additional features and 
  enhancements of the product since the previous release. It also summarizes the issues and limitations of the product and provides 
  workarounds wherever applicable.
* **SAFplus Platform SA-Forum Compliance** describes the level of compliance of OpenClovis SAFplus Platform and its Application Programming 
  Interface (API) with the relevant Service Availability Forum Specifications.
* **SAFplus Platform Installation Guide** provides the system requirements, installation procedure for OpenClovis SAFplus Platform, IDE, 
  and the Evaluation System.
* **SAFplus Platform Sample Application Tutorial** explains the steps to create and build a sample model using OpenClovis IDE and 
  OpenClovis SAFplus Platform. It also provides troubleshooting information for this process. This provides the logical first step in 
  understanding the SAFplus Platform offering.
* **SAFplus Platform Evaluation System User Guide** provides all the required information to configure and run the sample models packaged 
  within the Evaluation System. This document also provides good understanding of OpenClovis SAFplus Platform's functionality. This is 
  the natural follow on to the OpenClovis Sample Application Tutorial as it builds on the example created in that document.
* **SAFplus Platform SDK User Guide** provides information about SAFplus Availability/Scalability Platform architecture, various SAFplus 
  Platform components, and their interactions. This guide helps you to configure the OpenClovis SAFplus Platform components, compile, 
  and execute the SAFplus Platform code to build your custom application.
* **SAFplus Platform IDE User Guide** describes the usage of Integrated Development Environment (IDE), a graphical development environment 
  that complements the SAFplus Platform. This guide helps you to understand how to use the various features of the IDE to build the 
  application.
* **SAFplus Platform Log Tool User Guide** provides information about the usage of OpenClovis Log Tool. OpenClovis Log Tool is an interactive 
  utility that allows you to view binary log files in a readable format and hence monitor system errors, warnings, and other log 
  information. Log Tool allows you to format the .log files and filter them to view the required entries.
* **SAFplus Platform API Reference Guide** is provided for each component. It describes the Application Programming Interface (API), 
  Service Model, and Management Information Model of the various OpenClovis Application Service Platform (SAFplus Platform) services. 
  It helps the developer to understand the capabilities of the SAFplus Platform services and the APIs provided by these services.
* **SAFplus Platform Console Reference Guide** provides details about managing applications built on SAFplus Platform using the SAFplus 
  Platform runtime debug console commands. SAFplus Platform Console commands can be used to manage, monitor, and test your application.

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
