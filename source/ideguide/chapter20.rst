chapter 20: Glossary of Terms
=============================
**Alarm** An alarm is a warning about the abnormal conditions of Managed Object (MO).

.. note::
    An alarm always does not represent an error.

**Alarm Lifecycle** The Alarm Managed Service Object (MSO) associated with an MO depicts the lifecycle of an alarm as:

* An alarm is raised by the alarm service, if the abnormal condition relating to the alarm persists for a time, at least equal to the soaking interval specified. This alarm may be cleared by:

  * The alarm service, when it gets a notification from the MO that the abnormal condition which caused the alarm has been cleared.
  * An explicit command from an operator using the management interface.
  * RESET, if the MO is hardware, and RESTART, if the MO is software Execution Object (EO).

**Alarm Manager** The alarm manager enables configuring and handling of alarms. It provides support for alarm soaking, masking, alarm hierarchies, retrieving previous alarm conditions, and correlation of the alarms before publishing.

**Alarm Masking** Multiple alarms can be raised in a system. Alarm-masking is a procedure that enables the alarm service to publish the alarms with high priority for fault recovery.The current alarm-masking logic implies that all MOs are organized in a fault containment hierarchy which represents the relationship "is physically contained in" for hardware and "runs on" for software. The alarm-masking algorithm masks all alarms of the same or lesser severity level within any sub-tree in the hierarchy.

**Alarm Service** The OpenClovis alarm service implements a generic engine to process abnormal conditions reported by managed resources. The process includes identifying the alarm type and its severity level and determining whether an alarm has to be raised after running it through soaking and masking procedures. Potential subscribers for alarm events are - OpenClovis Fault Management Service, OpenClovis Availability Management Service and other agents like SNMP, CLI, and so on for reporting alarms to external managers.

**Alarm Severity** The alarm severity specifies the condition of the service provided by the MO. The severity levels can be critical, major, minor, warning, or cleared and indeterminate (CCITT X.733). The cleared and indeterminate level indicates clearing of one or more previously reported alarms. The critical and major alarms are service-affecting alarms.

**Alarm Soaking** Soaking is the time defined for extreme conditions before reporting as an alarm. Alarm soaking is possible when a managed resource provides a pair of notifications - one for the occurrence of an extreme condition and another for clearing of the extreme condition. Soaking avoids raising an alarm unless the extreme condition of the alarm persists for a period of time. Sometimes, you may not get a notification for clearing of an extreme condition. In such cases, a poll mechanism can be used to see if the alarm condition is still present after the soaking interval.

**Application** An Application is customer software built using OpenClovis infrastructure that provides services to the end users. For instance: A SIP server customer application.

**ASP Console** A command-line Interface for debugging allows access to the managed object repository for creating, deleting and otherwise manipulating objects. ASP Console also provides viewers for system log and trace data as well as interfaces to individual EOs to view and modify their private (non-persistent) data.

**Attributes** Attributes are the characteristics or parameters of a Managed Object.

**Availability Management Framework (AMF)** AMF is a software entity that provides a framework for high availability of applications in a system. It is responsible for instantiating and managing all the OpenClovis ASP services. It executes configured recovery actions on the failure of application components. The AMF is built with the close association of two OpenClovis ASP components: Component Manager and the Availability Management Service (AMS).

**Blade** A blade is a single board computer that is a Field Replaceable Unit (FRU). It can be plugged into a chassy.

**Boot Level** OpenClovis ASP services and customer applications are mapped to different Boot Levels. The Boot Management Service starts these services (applications) when it reaches the specified BOOT LEVEL. The BMS can be constrained to boot-up only to a specified BOOT LEVEL.

.. note::
    BOOT_LEVEL is conceptually similar to the run_level concept in Unix.

**Boot Management Service** OpenClovis Boot Management Service provides the support for starting or shutting down of the OpenClovis ASP services and customer applications on a OpenClovis ASP managed platform. The Boot service assumes that an OS has already been booted-up in the target environment. While starting or shutting down a system, the BMS has several BOOT LEVELS in sequence. At each level, certain services (applications) are started or shutdown.

**Boot Profile** The boot profile defines a particular type or a particular mode of boot configuration. The list of services performed can be different for different profiles. This helps in obtaining different configurations containing different set of boot levels and different Service Units assigned to them.For Instance, a profile named debug can define a boot configuration, which can be helpful in debugging the boot up process, whereas a profile named production can be used when the desired configuration for normal deployment boot needs to be specified.

**Chassis Management Service** OpenClovis Chassis Management Service provides support for resource discovery, sensors, and controls on chassis-based hardware platforms. The platforms can be standard-based (ATCA, BladeCenter and so on) or proprietary. The Chassis Management Service can be customized for any platform by providing the platform specific plug-ins.

**Checkpoint Service (CPS)** CPS provides synchronization of run-time data and context to ensure a seamless failover or switchover of applications. It allows the application to store its internal state and retrieve the information. It also provides a facility for processes to record checkpoint data incrementally and supports nontransparent mode of Checkpointing.

**Clovis Object Repository (COR)** Clovis Object Repository (COR) is an inmemory object-oriented hierarchical distributed repository of Managed Objects (MO). COR contains the description of each MO and relationships between different MOs. Multiple relationships - hierarchical containment and inheritance - are supported. COR provides Object lifecycle management, transactions on multiple objects, object change notification, object change propagation and other services. The OpenClovis ASP instances on the System Directors has an instance of the Clovis Object Repository associated with it. The CORs on both the System Directors are always in-sync to provide high availability.

**Cluster** A cluster is a collection of cluster nodes that may change dynamically as nodes join or leave the cluster.

**Cluster Node** A cluster node is the logical representation of a physical node.

**Component** A component is the logical entity that represents a set of resources to the Availability Management Framework. The resources represented by the component encapsulate specific application functionality. This set can include hardware resources, software resources or a combination of the two.A component is the smallest logical entity on which the Availability Management Framework performs error detection and isolation, recovery, and repair.

**Configuration Attributes** Configuration attributes are the means by which system management applications provide input on the desired sets of attributes and their handling that an Object Implementer (OI) should implement.

**COR Persistence** The Clovis Object Repository may be persisted using a persistent database. The effect of this is as follows: When a OpenClovis ASP instance boots up, COR reads the database and restores the persisted state to each MO. This state is used, for example, by the provisioning service to provision all objects on boot-up.

**DBAL** Provides a standard interface for any OpenClovis ASP infrastructure component or application to interface with the commonly used relational. DBAL currently supports GNU Database Manager.

**Default Boot Level** During startup, the Component Manager boots the components to a boot level called default boot level as specified in the deployment configuration file. All the components specified up to and including the default boot level are started.

**EO Management service** The OpenClovis Execution Object (EO) Management Service monitors the health and controls the state of all Execution Objects in the system. State control includes the ability to start, stop, suspend, resume, kill and restart an EO.

**EOID** Identifier for execution object (EOID is unique within a OpenClovis ASP instance).

**Error Error** is the deviation in the system state or behavior as a result of the use of incorrect data or signal.

**Erroneous Condition** A condition which the application needs to notify the north bound entity.

**Event Events** are means by which data may be exchanged between event publishers and event subscribers. An event is characterized by an event channel and event ID.

**Event Filter** These are filters used by an EO to specify the events it is interested in.

**Event Manager** The Event Manager provides a distributed service infrastructure for event notification across multiple blades. It is based on the publisher subscriber programming model, which decouples senders and receivers both in space and time. An event dispatcher resides on each node, which handles local subscriptions and forwards all events to the respective clients and all peer event dispatchers.

**Event publisher** An EO that publishes an event.

**Event Service** A OpenClovis ASP service that provides a mechanism to publish or subscribe communication based on event channels and asynchronous communication between publishers and subscribers.

**Execution Object** The motivation for the OpenClovis EO is to provide execution contexts independent of process architecture in any OS.Execution objects are programs that implement management interfaces (mandated by OpenClovis ASP).

* These programs allow them to be managed in a OpenClovis ASP environment. (Refer to EO Management Service, for details of management functions).EOs may use services provided by other EOs (For example, Checkpointing service). If so, they need to implement client interfaces for the service in question.EOs may provide services to other EOs. In this case they need to implement the service interface.EOs may be made visible to an external manager by representing them as MOs.

**Failure** A failure in a system occurs when the consumer (human or non-human) of a service is affected by the fact that the system has not delivered the expected service. It is a reflection of unacceptable or incorrect results delivered by a system with respect to a specification. It is an unexpected behavior perceived by the consumer or user of a service.

**Fault** A fault is a Physical or algorithmic cause of a malfunction. Faults manifest themselves as errors.

**Fault Diagnosis** Fault Diagnosis is the process of determining the cause of a fault. Fault diagnosis is provided to the granularity of an FRU to support maintainability or serviceability.

**Fault Management Service** OpenClovis FMS provides a framework for fault management, including fault diagnosis and progressive recovery. Standard recovery methods for software exceptions are available. You can plug-in custom fault recovery methods.

**Fault Manager** The Fault Manager manages faults in a system and initiates actions. It can handle various user-defined run-time faults, including hardware and software faults. It can prioritize faults to ensure that the critical faults are addressed before the normal or the low-priority faults.The Fault Manager client library notifies alarms to the Fault Manager server located on the same node. The actions to be taken on receiving a fault are controlled by the FM policy associated with the faults.

**Field Replaceable Unit (FRU)** Field Replaceable Unit is the hardware element of a system that can be replaced by a similar element in the field.

**Group Membership Service (GMS)** Group membership service provides the facility of leader election. Any application or OpenClovis ASP service can register with GMS to keep track of information such as leader change and cluster membership change.

**Hardware Abstraction Layer (HAL)** Provides a uniform management interface to hardware peripheral devices via their respective device drivers. Device types include Framer, NP, ASIC, LIU, Switch chip, DSP, and so on. HAL supports the following interfaces: Access, Init, Open, Close, Control, Retrieve, Send, Receive, Download OpenClovis ASP. Customer applications are made entirely transparent to configuration changes in the underlying devices by the HAL.

**Hardware Resource** A hardware resource is a MO class corresponding to hardware objects present on the blade (example, port). Hardware resource can be within another hardware resource. For example, port on a blade.

**Heartbeat** Heartbeat is a message exchanged at regular intervals between two OpenClovis ASP instances. A missed heartbeat is the non-arrival of a heartbeat within a timeout period. A configurable number of missed heartbeats are taken to indicate that one of the two instances in question is no longer running or is incommunicable.

**Heartbeat Service** A service that runs on every OpenClovis ASP instance and monitors the health of other OpenClovis ASP instances using the heartbeats.

**High Availability (HA)** High Availability (HA) is used when referring to a system that is capable of providing service most of the time.

**Intelligent Object Communication (IOC)** OpenClovis Intelligent Object Communication (IOC) provides a transport and OS neutral, fault tolerant communication between OpenClovis Execution Objects using physical links available and user defined transports (E.g.: UDP, TCP, or Ethernet).

**Interface Definition Language (IDL)** IDL is a library used by all EOs to communicate efficiently across nodes. Using IDL, OpenClovis ASP services can communicate across endian machines and mixed mode (32-bit and 64-bit architecture).

**IOC Address** Address of a OpenClovis ASP (IOC) instance that maps to a transport address for each transport or physical link provided.

**Link** A link is a physical interconnection between nodes. Also referred to as physical medium.

**Local Managed Object** A managed object abstracting a local resource.

**Local Resource** A resource that is contained from a fault-containment point of view within a physical node. (Local resources can be software abstractions implemented by programs running on the node, or hardware attached to the node, or the node itself)

.. note::
    The definition is SA Forum defined.

**Log service** Log service collects, translates, and publishes log messages to record any significant event in the system. For example, operational state change of a component, managed object attribute value change, and so on.

**Managed Object (MO)** Managed Object provides an abstraction for the manageable properties of a resource in the system. MOs have attributes, support management operations, exhibit behavior and can emit notifications (CCITT X.700).Operations on an MO can be Create or Delete Instances; Get or Modify attributes; Action.Notifications emitted by an MO instance are instance created/deleted; report attribute change; class specific notification such as alarms.Attributes can be single valued, multivalued or grouped in an attribute group (Ex; Chassis attributes relating to blades may be grouped).

**Managed Service** Managed Services are the services or capabilities that are available within an MO, and provided either by MO, or by an MSP, which is a member of the MO. An MSP is an execution context that hosts the Managed Service and processes the service request.For example, the Blade MO can provide Configuration, Fault, and Performance Managed Services. And, the actual MSPs can be the Provision/Configuration Manager, Fault manager and Performance manager respectively. Managed Services include FCAPS (Fault, Configuration, Accounting, Performance, and Security), and other services such as Heartbeat and HA service.

**Managed Service Object (MSO)** MSOs encapsulate the attributes of a Managed Object specific to the particular service (MSP) they are associated with. (Ex: Alarm severity is an attribute related to the alarm service; it is a part of the Alarm MSO associated with any MO desiring an alarm service).

**Managed Service Provider (MSP)** The execution context that provides a managed service to an object is called the Managed Service Provider (MSP).The lifecycle of managed objects (creation, deletion...) is handled in the execution context of the COR EO. However, when an MO state is to be changed, the MSP interested in this change runs (prevalidate, update, post-validate) methods in a different execution context.

**Management Information Base (MIB)** Management Information Base is a data structure that holds information on how a system is configured or functioning.

**Management Interfaces** Methods available for managing a system at the boundary of the system and management middleware. In OpenClovis ASP, management interfaces (for different management protocols) are provided by the Mediation manager.

**Mediation Library** The Mediation Library mediates between management agents implementing standard protocols (such as CISCO CLI or SNMP) and the OpenClovis ASP to service management requests from respective (CLI, SNMP) management stations. Requests from outside the system are translated to requests on MOs and forwarded to the appropriate MO.

**Message** A message is a byte array of a certain size. In addition to the data contained in the byte array, a message also has a type, version, and priority.

**Message Queue** A message queue is a software abstraction for buffering messages. A message queue consists of a collection of separate data areas that are used to store messages of different priorities. Messages are read from, and written to, a message queue.

**Message Queue Group** A message queue group is a collection of message queues that are addressed as a single entity. A message queue group is global to a cluster, and it is identified by a unique name in the same name space used for the names of message queues. A message queue can be a member of different message queue groups. Messages sent to a message queue group are directed to one or more of the message queues in the group.

**Middleware** OpenClovis ASP is often referred to as a middleware. This is to reflect that OpenClovis ASP is a layer over the OS, providing system services and APIs to user applications. Applications must be written to OpenClovis ASP API’s (rather than directly to OS API’s) in order to be OS, database and hardware independent and to be manageable and available.

**MO (Instance) Tree** Managed Object Instance Naming Tree - The MO fault containment hierarchy (see OpenClovis Information Model) is used to name instances of objects. For example, in a chassis based system, an instance of a port could be located as follows: Chassis (0)/Blade (3)/Port (2).

**MOID** Managed Object Identifier - The MOs have unique global handles associated with them within the system, and using these handles one can address the MOs. The COR handle uses a pair of object class index and object instance index. Object class index uniquely identifies a managed object class and managed object instance index uniquely identifies an instance of a managed object within that class.

**Name Service** The name service facilitates location transparency to the communicating objects by allowing use of object name instead of location specific address. The name service provides name to IOC address translation. A name is userdefined data.

**Node** A node is a blade, a stand-alone PC, or a daughter card that runs the AIS services and can become a member of the cluster.

**Node Class** The following types of node class are available:

* **SAF Class A:** (System Controller) These cards act as chassis managers or system controllers, and are either standalone or run only OpenClovis controller functions. Customer applications will typically not run on a Class-A card as the intent is to keep them stable and working in a system over a long interval. The Class-A cards are the primary physical link for any external management entity such as EMS. A Class-A blade can assume access to persistent storage on the blade or within the system.
* **SAF Class B:** (System Controller) There are two subtypes within this profile. They are Class-B1 and Class-B2. Class-B1 cards support only OpenClovis master functions. OpenClovis controller functions are located on a separate Class-A card. Class-B2 cards contain both master and controller functions and there is no separate Class-A card in the system. Class B1 blades may or may not have access to local persistent storage and hence must not assume the same while Class-B2 cards may assume access to local persistent storage. Class-B cards may also contain application functions.
* **SAF Class C:** (Payload) This actually defines a set of card profiles, each of which can contain a different set of OpenClovis functions. However, the common link between all is that they cannot have OpenClovis master or controller functions and are only participants in a OpenClovis system. Class-C blades may or may not have local persistent storage and hence must not assume the same.
* **SAF Class D:** (Non-ASP Node) OpenClovis is aware of these blades in the system and must manage them, whereas no OpenClovis components run on this blade.

**Node Profile** Node Profile describes the list of services that can be run on this node and the various attributes of these services. It also describes the characteristics of the node with respect to its role in the chassis. A node can either behave as a Controller Node for the complete chassis or as a normal processing node in the chassis.

**Notification** Managed Objects emit notifications. Notifications emitted by an MO instance are instance created/ deleted; report attribute-change; class-specific notification such as Alarm (Also referred to as COR notification).

**OAMP** Refers to Operations, Administration, Maintenance and Provisioning.

**Object Implementer** Services and applications that implement the Information Model Management (IMM) objects are called Object Implementers.

**Object Manager** Object Manager (OM) is a library which provides some of the object oriented features like inheritance and function overriding to be used by OpenClovis ASP services or user applications in C language. Using Object Manager library one can create a class, which has data members and member functions. A base class can be inherited to form a derived class. The derived class has data members as well as the member functions of the base class. The functions can be overridden in the derived class. Object manager library provides functionality to create such base classes, derived classes and create instances of such classes. The object manager library also provides APIs to maintain association between these OM objects and COR objects.

**OM Objects** Managed Objects encapsulate data and behavior (have attributes and methods). The public attributes of an MO associated with a specific (service) capability of the managed object are segregated into MSOs. Behavior and private data associated with the capability is encapsulated in a corresponding OM Object.While the MO and the MSOs are persistent in the COR database, associated OM Objects are created by the interested MSPs and follow the MSP lifecycle. (For example, if the alarm service is brought down for some reason, the Alarm OM objects will also be deleted).

**OpenClovis ASP Services** OpenClovis ASP services are Execution Objects that provide core-underlying services for OpenClovis ASP and applications.

**OpenClovis IDE** This Is a Graphical User Interface (GUI) tool designed to simplify and accelerate the development of System Infrastructure Software for Telecom and other networking products. It enables the customer to rapidly create an information model of the Resources that will be required to manage. It generates customized code for OpenClovis ASP, a flagship product of OpenClovis Inc.The OpenClovis IDE is built on the Eclipse Modeling Framework (EMF). It provides two important features: Modeling and Configuration. It allows you to model the following elements: Physical Resources and Logical Entities.

**OpenClovis Information Model** The OpenClovis Information Model (IM) is a generic framework or an abstract representation of the entities in a managed environment. It provides a way of describing the characteristics of the network element for which the infrastructure software is being implemented. IM provides a unified view and association of all the physical and logical objects in the managed environment. Information Modeling transports the current content or state of a OpenClovis Object such as a blade, port, or any other logical object between different Execution Objects.

**Operating System Abstraction Layer (OSAL)** The OpenClovis Operating System Abstraction Layer provides commonly used APIs to abstract OS services for OpenClovis EOs and customer applications.The basic OS services include the following:

* Memory Management, Timer Management, Executive Task/Process/thread Management, Signal/Event Management, Resource Management, Messaging services, RTOS task profiling services, synchronization and semaphore management.
* OSAL enables one to easily port the OpenClovis ASP and OpenClovis ASPenabled customer applications onto new RTOS environments.

**Physical Node** A physical node is a particular type of resource that can run a single instance of the operating system and OpenClovis ASP software. (Example, a blade with a general purpose CPU). Physical nodes may be interconnected via some form of communication medium (Example, multiple blades via a chassis backplane).

.. note::
    This is consistent with SA Forum definition Process Model. The process model describes how OpenClovis ASP service EO’s and user application EO’s map to processes in a specific operating system. (Example: in the multi-process version of Release 1.0 for Linux, all OpenClovis ASP EOs run in a single Unix process and user application EOs may be combined in one or more processes).

**Pre-provisioning** Normally, the provisioning of an object corresponding to an FRU occurs when that FRU is present. However, pre-provisioning takes place when an MO exists and the FRU is absent. Scenarios where this occurs:

* A blade lost power or was extracted from the chassis after being provisioned.
* A user pre-provisioned a blade in the Provision Manager’s database in the absence of a blade.
* When the blade becomes active, the provisioning service on the System Controller verifies the provisioned data against the properties of the blade and pushes the data down to the blade if the blade’s properties match; otherwise, an identity mismatch alarm will be raised and no data will be pushed down.

**Provisioning Service** The Provisioning service is an Engine that provisions any type of equipment and facility, virtual or physical in the most generic way. Provisioning is accomplished using the Provisioning EOs and provisioning MSOs.

**Reboot** Cold reboot occurs when a system is powered off and then powered on. In a warm reboot, the hardware remains powered on and provisioning is not disturbed; the OS is re-started.

**Remote Method Dispatch** Remote Method Dispatch is the foundation for all OpenClovis ASP client APIs. It implements remote procedure call semantics using both synchronous and asynchronous methods.

**Resource** A resource is any entity that can be managed by the OpenClovis ASP. A resource is either hardware equipment (for example, a blade) or a software abstraction implemented by programs running on that hardware (for example, a software process).

.. note::
    The OpenClovis resource definition corresponds to the SA Forum definition of resource.

**Routing Table** Based on the information in this table, IOC module selects a transport and the next IOC hop, to send a message towards its destination. Multiple routes (to the same destination) are required for fault tolerance.

**Rule-Based Engine (RBE)** Rule-Based Engine (RBE) provides a mechanism to create rules to be applied to the system instance databased on simple expressions. An expression consists of a mask and a value. These expressions are evaluated on user data and generate a boolean value for the decision.

**Run Level** Mechanism used to synchronize and order the execution of EOs within and across different OpenClovis ASP instances.OpenClovis EOs are configured to execute at some run-level; therefore, they can be controlled by the Boot Manager’s Run-Level Controller (RLC). For example, the Alarm Agent is configured at Level-2 after the Provisioning Agent, which is at Level 1. This implies that the Alarm Agent has some execution dependency on the Provisioning Agent and that there is some critical section in the Provisioning Agent’s initialization code that needs to execute first before the Alarm Agent can continue its execution.

**Runtime Attributes** Runtime attributes are the means by which Object Implementer (OI) reflect the current state of the attribute they implement in the information model. Run-time attributes are typically under the control of Object Implementer's.

**SA-Aware Component** An SA-aware component is a local component that supports the SA functionality provided by the Availability Management Framework and are under direct control of the Availability Management Framework. The Availability Management Framework directs operations to the component as to what it should do and when to do it. The component then reacts appropriately to these operations.

**Service** Service is the output of a system that meets the specification for which the system is devised.

**Service ID** Uniquely references a service (OpenClovis ASP or customer designed). Shelf It is a structure/frame where one or more chassis are mounted.

**Simple Network Management Protocol (SNMP)** Simple Network Management Protocol (SNMP) is a sub-agent, which provides the flexibility to manage platform and non-platform hardware, the OpenClovis ASP model, and the alarms present in the system. Using SNMP, you can manage the attributes of an MO that includes run a get, set, or notification.

**Software Resource** A software abstraction implemented by programs running on a hardware resource (example, a software process) is called a software resource.

**System** The system consists of a collection of physical nodes and programs running on those nodes (Ex: A chassis with multiple blades and running software programs).

**System Log** A persistent file that records the significant events occurring in the system. Typical entries include events related to boot-up, shutdown, errors, recovery, operator commands, operator log-on and log-off. Each log entry contains a timestamp, reporting entity, affected entity, and severity code and operator identity (if applicable).

**Transaction Manager** Transaction Manager provides a library for resource managers to use transaction semantics to manage distributed data. Any component, that needs to be part of transactions can link with this library and act as a resource manager. The transaction manager automatically tracks participants and provides ACID semantics to ensure that all participants are updated properly, or will rollback to previous state assuring data integrity despite component failures.

**Transactions** OpenClovis ASP supports transactions in the following sense:

* Any service that changes the state of managed objects may provide three methods: pre-validate (), update () and post-validate (). All these methods must be successfully executed for the transaction to be complete. The affected MO state is also updated in the persistent COR database as part of the transaction. (Rollback is currently not supported).
* OpenClovis ASP also supports nested transactions. A list of EOs (called station list) may be associated with each MO/MSO. Each EO in the list may provide the three methods listed above. The nested transaction is implemented as follows: The list is traversed top down and the pre-validate method of each successive EO is executed. When the last EO in the list is reached, the update and post validate methods of that EO are executed and now control returns to successive EO’s up the list with the update and post methods being executed in each case. The transaction is considered successful if no error is reported by any method executed as part of the transaction.

**Transport** OpenClovis term for user (system developer) provided communication facility, which provides IOC access to the physical medium.
