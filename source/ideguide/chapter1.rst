Chapter 1: Introduction to OpenClovis IDE
=========================================
**OpenClovis Integrated Development Environment (IDE)** is designed to simplify and accelerate the development of application service 
platforms for the telecommunication market place. Coupled with the OpenClovis ASP,this intuitive software solution streamlines the 
process of specifying the information model, High Availability (HA) aspects and the communication infrastructure of a system. 
OpenClovis IDE stores all information describing a project in well defined XML files that can be modified by the user. Modeling of 
system resources and relationships are specified using a graphical UML editor. This chapter familiarizes you with the main concepts 
and features of OpenClovis IDE.

* Basic Concepts
* OpenClovis IDE Features
* OpenClovis Value Proposition

Basic Concepts
--------------
OpenClovis IDE is an Integrated Development Environment (IDE) designed to simplify and accelerate the development of Telecom application 
software over OpenClovis platform. It provides a simple and powerful mechanism with easy drag-and-drop features, to create Resources 
and Components and define their attributes and relationships between them. OpenClovis IDE enables you to capture this model through 
UML notations and then save them as XML files.

Openclovis IDE is built using the Eclipse platform, hereby it inherits some functionality from it. It has a modeling framework and 
code generation facility for building tools and other applications based on a structured data model, from a model specification 
described in XML.

.. note::
    This document refers only to the features of the OpenClovis IDE product and not those of the Eclipse platform.

OpenClovis IDE enables you to rapidly create a model of the Resources and generates customized code for OpenClovis. Apart from enabling 
to easily generate code, it also provides the capability to compile and deploy the code to the target system under development.

OpenClovis IDE allows you to model the following elements:

* **Physical Resources**
* **Logical Entities**

OpenClovis IDE provides two basic views of the system; physical (or resource) view and logical (or component) view. These two views 
are linked with each other.

* **Physical (or resource) view:** The physical (or resource) view allows the modeling of the physical containment aspects of the system, 
  working with chassis, blades, daughter cards, network ports, other physical devices, and software entities running on such cards and 
  devices. The physical containment hierarchy is used to define the Managed Object(MO)tree and to derive the MO path (addressing) 
  information.
* **Logical (or component) view:** The logical (or component) view is a service availability view of the system, using concepts such as 
  cluster, nodes, service units, service groups, service instances, component service instances, proxy components, non-proxy components, 
  and proxied components.

Information Modeling Using IDE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The OpenClovis Information Model is a generic framework or an abstract representation of the entities in a managed environment. The 
OpenClovis IDE enables you to build an Information Model using UML notation.

An Information Model (IM) presents a unified view of different components of a system and abstracts hardware and software running on 
a system, from an end user. IM provides a unified view and association of all the physical and logical objects in the managed 
environment.

The advantages of Information Modeling are:

* **Managed Objects:** Allows the definition of MOs for a OpenClovis-based system covering chassis management, devices, alarms, faults, 
  component states, and provisioned attributes of OpenClovis components and customer applications.
* **Strong integration with system model:** Information model is created as the user is working on the system model. For instance, 
  when an alarm is defined for a physical or logical component, the related alarm MO attributes are automatically added to the 
  information model. *
* **SNMP MIB import:** To speed up MO definition and/or to design an information model that is compliant with existing models,one or 
  more SNMP MIB files can be imported in to a OpenClovis IDEproject. The user can select one or more objects from the MIB tree and add 
  them to an MO class definition. MIB attributes will become MO attributes with the same name, type, and access mode. To maintain 
  compatibility with the MIB, SNMP OIDs are preserved and attribute names, type, and access modifiers can be locked to prevent 
  deviation from the imported model. SNMP traps can be added as alarms. If needed,proprietary attributes can be added to an imported 
  object, resulting in a new object class.
* **SNMP MIB export:** Parts of or the entire newly defined information model can be exported as new, proprietary MIB(s).
* **OID/MOIDmapping:** OpenClovisIDE generates the necessary bi-directional mapping between the OIDs used by the SNMP agent and the 
  MOIDs used by OpenClovis COR OpenClovis IDE.

For information about building a sample model using OpenClovisIDE,see OpenClovis Sample Application Tutorial.

OpenClovis IDE Features
-----------------------
OpenClovis IDE provides the following important features:

* **Modeling:** Modeling is performed using the Resource Editor and Component Editor pane, along with the definition of the relationship, 
  and its validation. The properties of each of these resources are also set during the development of the Information Model.
* **Configuration:** Configuration is related to the configuration of modeled entities, OpenClovis components, alarms set for the 
  resources, generated source code,and the generation of the configuration files needed for OpenClovis ASP customization, including 
  build-time, boot-time, and run-time configuration files.
* **Boot and run-timeconfiguration:** OpenClovis IDE generates the various XML files used by OpenClovis. Boot-time configuration includes 
  boot-levels, services to start per boot level, and node role profiles (personalities).
* **Code generation for OpenClovis customization:** To facilitate build-time customization for OpenClovis, OpenClovis IDE generates C 
  header files to be linked with OpenClovis libraries to result in customized OpenClovis server executables. During code generation, 
  the correct files are generated in the predefined directories and file structures.
* **Application stub generation:** OpenClovis IDE also generates application skeletons (stub code) for EOnized customer applications.
* **Eclipse based IDE for System and Information Modeling:** Powerful,Eclipse based graphical user interface for system modeling, 
  information modeling, and ASP-based product development.
* **UML Based:** Model components and their relationship such as containment, aggregation, and inheritance, are edited using a graphical 
  UML editor.
* **Projects Based:** Modeling work files are organized into projects. Many model artifacts are reusable across projects.
* **XMI import:** UML models (if satisfying certain restrictions) can be imported from other tools using XML Metadata Interchange (XMI) 
  compliant files.
* **Integrate with other IDE Tools:** Due to its Eclipse based nature, IDE can be integrated with other Eclipse based IDEs.
* **Template support:** A library of pre-defined model fragments (templates) are provided, jump-starting the system modeling work when 
  working with common objects such as standard chassis, system controller cards, line cards. For specific hardware models (chassis and 
  cards) a palette of fully detailed and complete object models are available.

The following are a few additional features provided by the OpenClovis IDE:

* Facilitates easy drag and drop of resources and components.
* Validation of a model. View the existing projects in the OpenClovis IDE Workspace.
* Importing OpenClovis IDE Projects.
* View a MIB File through the OpenClovis MIB explorer.
* Generation of source code and configuration files.
* Outline view for editors.

OpenClovis IDE Value Proposition
--------------------------------
OpenClovis solution offers the following benefits to its customers.

* Enhances developer productivity.
* Reduces time-to-market.
* Ensures re-usability of core development efforts.
* Offers platform-independent modeling and implementation.
* Increases development process consistency.
* Facilitates Platform component integration.
* Minimizes software footprint for optimized performance.
* Supports a broad range of industry standards such as,
* Advanced Telecom Computing Architecture (ATCA), Carrier Grade Linux (CGL), and SA Forum Application Interface Specification (AIS).
