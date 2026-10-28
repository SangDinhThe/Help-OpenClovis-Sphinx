Preface
=======
**OpenClovis Applications Service Platform (SAFplus Platform)** is a modular, high-performance, scalable software platform (sometimes 
also referred to as middleware) to facilitate the speedy development and run-time operation of highly-available and manageable 
communications systems. SAFplus Platform has been primarily designed for complex, multi-processor, distributed systems, consisting 
of multiple processor cards or chassis, using heterogeneous CPU types and operating system versions. SAFplus Platform has been 
fine-tuned for software applications that not only demand reliability and manageability, but also scalability and high performance.

In a typical SAFplus-enabled communication device, SAFplus Platform resides on every (or most) processor entities that need to be 
involved in the manageability and configuration of the device, or which need to perform redundant services in order to provide high 
availability. On each of such processors SAFplus Platform is present in the form of a few run-time processes (daemons), while 
application-specific components that need to use any of the SAFplus Platform services communicate with these daemons using SAFplus 
Platform client libraries. For most SAFplus Platform services, the SAFplus Platform middleware takes care of all needed 
inter-processor communication and data replication among the various processor entities, effectively tying these into one seamless 
cluster, hiding the inter-processor aspects from the SAFplus-based custom applications.

During development of an SAFplus-enabled communication system, system architects and software designers work with the **OpenClovis 
Software Development Kit (SDK)**. The SDK includes the **OpenClovis Integrated Development Environment (IDE)**, a graphical user 
interface to define, model, and configure the system, as well as all the relevant source files, header files, run-time libraries, 
build tools that are needed to create, test, and debug the target system.

With this product, OpenClovis provides Original Equipment Manufactures (OEMs), Telecommuncations Equipment Manufacturers (TEMs) with 
an efficient and cost-effective solution for creating highly available, manageable products with short time-to-market.

This **OpenClovis SDK User Guide** provides system architects and software developers with further information about the OpenClovis 
SAFplus Platform and its companion SDK. It provides an overview of the SAFplus Platform architecture, the various SAFplus Platform 
components, and their interactions. This guide also helps you to understand how to work with the OpenClovis Software Development 
Kit (SDK) when modeling, configuring, building, and deploying SAFplus Platform and SAFplus Platform based applications on target 
systems.

Audience
--------
**OpenClovis SDK User Guide** is written for system architects, software designers, developers, and system integrators. To use this 
OpenClovis product, you must be aware of the fundamentals of operation, management, and configuration of telecommunication and 
networking systems. You must also be familiar with basic high availability concepts, C programming, UML notations, and have the 
basic knowledge of Linux.

Document Organization
---------------------
OpenClovis SDK User Guide is organized into various chapters to provide information on specific areas. The following table 
introduces the chapter names and a brief overview of the content.
                                     
+---------------------------------------+---------------------------------------------------------------------+
| Chapter                               | Overview                                                            |
+=======================================+=====================================================================+
| **Chapter 1**, Overview               | This chapter helps you understand the conceptual information,       |
|                                       |                                                                     |
|                                       | advantages and key features of OpenClovis SAFplus Platform and      |
|                                       |                                                                     |
|                                       | IDE.                                                                |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 2**, High Availability (HA) | This chapter provides an introduction to the basic concepts of HA   |
|                                       |                                                                     |
|                                       | and the relevant SAFplus Platform features and SAFplus Platform     |
|                                       |                                                                     |
|                                       | components, namely: Availability Management Framework (AMF),        |
|                                       |                                                                     |
|                                       | Checkpointing Service, and Group membership Service (GMS).          |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 3**, System Management      | This chapter provides information about the various SAFplus         |
|                                       |                                                                     |
|                                       | Platform features and components for system management, such        |
|                                       |                                                                     |
|                                       | as: Clovis Object Registry (COR), Mediation Library, Transaction    |
|                                       |                                                                     |
|                                       | Service, Provisioning Library, Alarm Service, Chassis Management,   |
|                                       |                                                                     |
|                                       | and SNMP Sub-Agents.                                                |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 4**, Communications         | This chapter provides an overview of the features, services and     |
|                                       |                                                                     |
| Infrastructure                        | relevant components of SAFplus Platform in the domain of            |
|                                       |                                                                     |
|                                       | inter-process and inter-processor data communication.               |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 5**, Basic Infrastructure   | OpenClovis SAFplus Platform is built on a number of basic           |
|                                       |                                                                     |
|                                       | infrastructure elements, which are described in this chapter.       |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 6**, Hardware Platform      | The specific benefits of the Platform Support Package, and its      |
|                                       |                                                                     |
| Support                               | realization are described in this chapter.                          |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 7**, Development Lifecycle  | This chapter describes how the various SDK features fit in          |
|                                       |                                                                     |
| and OpenClovis SDK                    | the workflow of a typical development life-cycle, and provides      |
|                                       |                                                                     |
|                                       | detailed information about the key phases, such as configuring,     |
|                                       |                                                                     |
|                                       | building, and deploying SAFplus-enabled systems.                    |
+---------------------------------------+---------------------------------------------------------------------+
| **Chapter 8**, "Starter" Models       | This chapter summarizes the so-called starter models provided by    |
|                                       |                                                                     |
|                                       | OpenClovis to jump-start the development of your own                |
|                                       |                                                                     |
|                                       | application, as an alternative to starting from scratch.            |
+---------------------------------------+---------------------------------------------------------------------+
| Appendix A, Glossary of Terms         | This provides complete information about all the terms and          |
|                                       |                                                                     |
|                                       | definitions specific to OpenClovis SAFplus Platform and its         |
|                                       |                                                                     |
|                                       | components.                                                         |
+---------------------------------------+---------------------------------------------------------------------+

Related Documentation
---------------------
For additional information about the OpenClovis SAFplus Platform, SDK, and IDE, please refer to the following companion documents:

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

All the above document are available in both Portable Document Format (PDF) as well as a set of cross-referenced, browsable HTML pages. They can be found under the /doc subdirectory of the installed SDK (under the /pdf and /html subdirectories, respectively). Please refer to the installation guide for further information.

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
