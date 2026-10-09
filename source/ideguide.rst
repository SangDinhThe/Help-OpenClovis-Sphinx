.. _ide-usr-gd-label:

IDE User Guide
==============

Preface
-------
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
| **Chapter 2**, Getting Started    | This chapter provides information to launch and access IDE, create a   |
|                                   |                                                                        |
|                                   | workspace and a project.                                               |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 3**, Understanding      | This chapter provides information about the IDE work environment.      |
|                                   |                                                                        |
| the User Interface                |                                                                        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 4**, Setting Resource   | This chapter provides information about the properties that you can    |
|                                   |                                                                        |
| Properties                        | specify for the chassis, node hardware, hardware, and software         |
|                                   |                                                                        |
|                                   | resources in the Resource Editor.                                      |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 5**, Defining Alarm     | This chapter provides information about defining alarms to map to the  |
|                                   |                                                                        |
| Profiles                          | resources.                                                             |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 6**, Setting Component  | This chapter provides information about the parameters that you can    |
|                                   |                                                                        |
| Properties                        | specify for the various components in the Component Editor.            |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 7**, Configuring ASP    | This chapter provides information about configuring ASP components     |
|                                   |                                                                        |
| Components                        | within IDE.                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 8**, Configuring AMF    | This chapter provides information to create the instances of the       |
|                                   |                                                                        |
|                                   | entities defined in a Component Editor using AMF Configuration.        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 9**, Configuring and    | This chapter provides information about configuring and allocating     |
|                                   |                                                                        |
| Allocating Memory                 | memory configuration profiles to the various ASP components and the    |
|                                   |                                                                        |
| Configuration Profiles            | SAF components.                                                        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 10**, Creating and      | This chapter provides information about creating and using the         |
|                                   |                                                                        |
| Using Template Groups             | template groups to generate the source code.                           |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 11**, Defining IDL      | This chapter provides information about creating the IDL XML file      |
|                                   |                                                                        |
|                                   | that is used by the IOC links to provide communication between two     |
|                                   |                                                                        |
|                                   | or more components.                                                    |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 12**, Generating        | This chapter provides information about generating the source code     |
|                                   |                                                                        |
| Source Code                       | after you have completed building the model.                           |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 13**, Building the      | This chapter provides information about configuring and building       |
|                                   |                                                                        |
| Project                           | the project after you have completed generating the source code.       |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 14**, Making Project    | This chapter provides information about generating run-time images     |
|                                   |                                                                        |
| Images                            | for a target system.                                                   |
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
| **Chapter 18**, Application       | This chapter provides information about Application Import/Export      |
|                                   |                                                                        |
| Import/Export                     | feature provided by OpenClovis IDE.                                    |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 19**, Limitations       | This chapter provides information about the limitations of IDE.        |
+-----------------------------------+------------------------------------------------------------------------+
| **Chapter 20**, Glossary of Terms | This provides complete information about all the terms and definitions |
|                                   |                                                                        |
|                                   | specific to Open Clovis IDE.                                           |
+-----------------------------------+------------------------------------------------------------------------+
