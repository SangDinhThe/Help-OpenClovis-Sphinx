.. _saf-compl-label:

SAF Compliance
==============

Introduction
------------
Adherence to standards is a critical requirement for Next Generation Network deployments. The Service Availability Forum (SA Forum) is 
the primary standards body in the context of High Availability Middleware and enjoys the participation of over 95% of Tier 1 TEMs. 
OpenClovis has been actively participating in the forum and helping to drive the emerging Hardware Platform Interface (HPI) and 
Application Interface Specification (AIS) standards based on its experience.

As a result of the close involvement of OpenClovis with the SA Forum, the OpenClovis SAFplus Platform product has been aligned with SA 
Forum AIS architecture and functional partitioning from its inception and has kept pace with the evolution in the specifications and 
in many cases, anticipated new features and functionality.

Even as the specifications are evolving, the SA Forum is in the process of defining a test suite that will establish compliance of a 
product to the specifications. While this activity is in an advanced state for the HPI specifications, it has not yet taken off for 
AIS specifications. Partial compliance test suites are expected to be available for HPI by end of the 2006 calendar year.

It should be noted that where a specification is 'A' level (example: SAI-AIS-NTF-A.01.01 for the Notification Service), SAF is not 
obligated to preserve backward compatibility while going to a 'B' level version of the specification. On the other hand, backward 
compatibility with respect to API's will be preserved between different versions of the 'B' level specifications (Example: between 
SAI-AMF-B01.01 and SAI-AMF-B02.01)

OpenClovis expects to formally establish the compliance of SAFplus Platform to the SA Forum AIS standards as and when these compliance 
test suites become available. This document details the level of alignment of OpenClovis SAFplus Platform with the SA Forum 
specifications.

Standards Referenced
--------------------
The SA Forum specifications referred to in this document are available at `saforum.org <https://www.associationvoice.com/Page/16627~217631/ErrorNotFoundhttpswwwassociationvoicecom443Service-Availability-Forum-E28093-Frequently-Asked-Questions-FAQ/>`__. 
The versions of the specifications referred to are

* SAI-Overview-B.02.01
* SAI-AIS-AMF-B.02.01
* SAI-AIS-MSG-B.02.01
* AIS-CKPT-B.01.01
* AIS-EVT-B.01.01
* AIS-CLM-B.01.01
* SAI-AIS_LOG-A.01.01
* SAI-AIS-IMM-A.01.01
* SAI-AIS-NTF-A.01.01
* SAI-AIS-NAM-A.01.01
* Hardware Platform Interface Specification B.01.01

Compliance with Service Availability Forum AIS Architecture
-----------------------------------------------------------
OpenClovis SAFplus Platform complies with the Service Availability Forum (SAF) Hardware Platform Interface (HPI) and Application 
Interface Specification (AIS) specifications. OpenClovis Inc. is actively participating in the SA Forum and helping to drive the 
emerging HPI and AIS standards based on its experience.

Programming Model and Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Section 3.1 of SAI-AIS-Overview-B.02.01 describes the SAF Application Interface programming model and the generally intended usage of 
the interfaces.

It introduces the area server as an abstraction that represents the server providing services for a specification area, for instance, 
Availability Management Framework, Group Membership Service and so on. The interface is defined as occurring between a user application 
that needs the services of the area server and an area implementation library.

OpenClovis SAFplus Platform adheres to the SAF area server-area implementation library abstraction and the SAF programming and usage 
model in providing various services.

Availability Management Framework (AMF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Availability Management Framework (AMF) is the most important software entity of the SAF AIS Specification. It provides service 
availability by coordinating redundant resources within a cluster to deliver a system without a single point of failure. AMF prescribes 
a way to model applications that needs to be highly available. In addition, AMF provides a set of APIs that must be used by these 
applications to be managed for high availability.

OpenClovis SAFplus Platform is implemented in complete accordance with the SAF AMF model and interfaces. This may be considered as the 
core of the SAF solution for high availability. The only limitation in the current release with respect to the AMF component model is 
that SAF defines a flexible mapping between components, processes and threads whereas OpenClovis SAFplus Platform supports only a 
single process per component. OpenClovis Inc. offers to support one-to-one relationship between a component and a process. However, a 
component can have multiple threads of execution within it.

Application Interface Specification (AIS) Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following OpenClovis SAFplus Platform components provide services that are functionally equivalent to SAF AIS specifications:

* Availability Management Framework (AMF)
* Checkpoint Service (CPS)
* Event Manager (EM)
* Group Membership Service (GMS)
* Messaging Service (MSG)

SAFplus Platform AMF Features
"""""""""""""""""""""""""""""

* **HA model supported**

  * 2N
  * M+N

* **Auto Adjust**

  SAF SG auto adjust feature to adjust the SG based on the SU ranking giving preference to higher ranked ones for active assignments

* **SI Dependency**

  SAF SI dependency across service groups

* **CSI Dependency**

  SAF CSI dependency within the same SI for work assignments

* **Component instantiation dependency**

  SAF component instantiation dependency for components within the same Service Unit configurable through instantiationLevel attribute.

* **Reduction Procedure**

  SAF SG reduction procedure applied when the SG is running under reduced potential for computing and removing less optimal standby 
  assignments to assign Service Instances.

* **AMF NOTIFICATIONS**

  SAF HAStateChangeNotify and SIAssignmentStateChangeNotify notifications for applications to subscribe for AMF state transitions

* **Preferred SI assignment**

  Preferred SI assignment that could be configured for SUs to control SI assignments. Coupled with the delayed SG startup configuration 
  through restartDuration to control instantiation of all the preferred SUs, SI preference could be enforced during initial cluster 
  startup for the Service units in the cluster.

* **Proxy-Proxied support**

  Allow HA control of legacy application (non-SAF awared) via proxy

SAFplus Platform Cluster/Group Membership Service (GMS) Features
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The SA-Forum CLM API is fully supported.

* **Cluster Membership**

  CLM service manages the membership of the nodes. It manages the cluster formation during node joins and leaves.

* **Tracking Cluster Membership**

  Any application can register for Cluster Track callback through which it can get the notification for any node joins and leaves in 
  the cluster

* **Getting Cluster Member information**

  API interface are available to get the information such as Address, node name etc, for any given cluster member node.

* **Cluster node eviction/ejection**

  A cluster node can be administratively ejected from the cluster.

SAFplus Platform Checkpointing Service (CPS) Features
"""""""""""""""""""""""""""""""""""""""""""""""""""""
* **Checkpoint/Section creation/deletion**

  CPS provides APIs for users to create/delete checkpoints and sections within the checkpoints.

* **Granularity at Section level**

  CPS allows user to create a checkpoint and inside a checkpoint user can create any number of sections and read/write each sections 
  independently.

* **Checkpoint Status**

  CPS provides API to retrieve checkpoint status.

* **Locking at Section level**

  CPS provides read/write locks at section level due to which multiple sections can be accessed simultaneously.

* **Update options**

  CPS allows both Synchronous and Asynchronous update of the checkpoint replicas across the cluster

* **Replica Management**

  CPS allows both collocated and non-collocated mode of checkpoint replicas

* **Choosing replica at run time**

  User can use ActiveReplicaSet() APIs to set the active replica at run time.

* **Retention time**

  CPS provides users to specify a retention time for which the checkpoint is retained even when no one is accessing the checkpoint

* **Section Expiration Time**

  User can set an absolute expiration time for a section after which the section is deleted irrespective of its usage at that time.

* **Section Iteration**

  Users can iterate through the sections of a checkpoint.

SAFplus Platform Event Service features
"""""""""""""""""""""""""""""""""""""""
* **Publish/Subscribe multipoint-to-multipoint communication mechanism**

  * Based on concept of event channels
  * Publisher communicates asynchronously with one or more subscribers over an event channel
  * Multiple publishers and subscribers can communicate over the same event channel; publishers can be subscribers on the same event 
    channel
  * Individual publishers and individual subscribers can communicate over multiple channels

* **Events consist of standard header and one or more bytes of payload data**

  i.e. Event Service does not impose any specific transfer syntax for the data

* **Event channel management**

  Event service provides APIs for opening, closing and deleting event channels

* **Event operations**

  Event service provides APIs for managing the event payload data, publishing the event, subscribing for the event etc

Additional SAFplus Platform Services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis SAFplus Platform also provides various components that were implemented earlier than its implementation with SAF specifications. These components provide services that are functional equivalent to SAF AIS services as listed below:

+--------------------------------------+--------------------------------------+---------------------+
| OpenClovis SAFplus Platform          | Functionally Equivalent AIS Service  | AIS Specification   |
| Components                           |                                      |                     |
+======================================+======================================+=====================+
| Clovis Object Repository (COR)       | Information Model Management Service | SAI-AIS-IMM-A.01.01 |
+--------------------------------------+--------------------------------------+---------------------+
| Alarm Manager (AM)                   | Notification Service                 | SAI-AIS-NTF-A.01.01 |
+--------------------------------------+--------------------------------------+---------------------+
| Log Service                          | Logging Service                      | SAI-AIS-LOG-A.01.01 |
+--------------------------------------+--------------------------------------+---------------------+
| Naming Service                       | Naming Service                       | SAI-AIS-NAM-A.01.01 |
+--------------------------------------+--------------------------------------+---------------------+
| Platform Management Service          | Platform Management Service          | SAI-AIS-PLM-A.01.01 |
+--------------------------------------+--------------------------------------+---------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**SAFplus Platform Services Equivalent to SA Forum AIS Services**

IMM (OpenClovis Object Repository - COR) Features
"""""""""""""""""""""""""""""""""""""""""""""""""
The OpenClovis Object Repository(COR) implements the IMM features. We are progressing on having API level compliance which will be 
available in R5.0.

The following are the IMM compliant features of COR:

* **Object Mananger and Object Implementer**

  COR provides a rich set of APIs to make configuration changes on a Managed Object (MO). It provides service to implement a MO by multiple Object Implementers (OI), so that the configuration changes on the MO can be validated by all the OIs. It provides APIs to make or remove an application as a OI for a MO.

* **Runtime Attributes Management**

  COR provides service to implement the runtime attributes of an object or all the object instances of a class. The Runtime attributes values can be cached or non-cached in COR. The cached runtime attributes values has to be updated by Primary Object Implementer (POI) periodically in COR. The value of non-cached runtime attributes will be updated by POI on request by COR. The values of cached runtime attributes can be persisted into storage devices.

* **Configuration Attributes Management**

  The Configuration attributes are always cached and persisted by COR. Any configuration change on these attributes by a OM will be implemented by all the OIs.

* **Attribute Characteristics**

  * COR supports the following attribute characteristics.

    * CONFIG - Indicates that the attribute is a configuration type attribute.
    * RUNTIME - Indicates that the attribute is a runtime attribute.
    * WRITABLE - Indicates that the configuration attribute can be modified.
    * INITIALIZED - Indicates that value for the configuration attribute must be specified when the object is created.
    * CACHED - Indicates that the value of the attribute is cached in COR.
    * PERSISTENT - Indicates that the value of the attribute must be stored in a permanent manner by COR

* **Object Class Management**

  COR provides APIs to create, delete and modify the classes, and to make hierarchical relationship between the classes. It also provides service to inherit the existing class to create a new class.

* **Tree organization of Objects**

  COR organizes the MOs in a hierarchical manner supporting parent-child relationship, inheritance, association and containment relationships.

* **Search Operations**

  * The search operations can be performed on a single MO, or a MO and its children, or a sub tree rooted from the given MO.
  * We can either retrieve all the attributes in the MO matching the given criteria or only the matching attributes.

* **Object Access**

  COR bundle GET APIs can be used to retrieve the attributes values in a efficient manner by grouping the GET requests belonging 
  different MOs into one single request to COR. The values of runtime non-cached attributes will be updated by POI on request by COR.

* **Class Implementer**

  COR provides APIs for the application to implement all the Object instances of a class, for both Configuration and Runtime attributes.

SAF Notification Features
"""""""""""""""""""""""""
OpenClovis SAFplus Platform is compliant with the following Notification features :

* **Notification Types**

  * Alarm
  * State Change
  * Object Create/Delete
  * Attribute Change

* **Alarm Notification**

  An alarm report is a notification of a specific event that may or may not represent an error. OpenClovis Alarm notification is fully 
  compliant with ITU-T X.733 standard (which is recommended by SAF-NTF).

* **State Change Notification**

  * OpenClovis AMF provides services for the following state change notifications to the Management Applications

    * HA state of the SU changed
    * SI partially/fully assigned
    * Component arrived/departed
    * Node arrived/departed

* **Object Create/Delete and Attribute Change Notifications**

  OpenClovis SAFplus Platform provides services for the notification of Managed Object Creation, Deletion and Attribute changes. It 
  also supports the Management Applications to filter the attribute change notifications based on attribute identifiers.

* **Notification Delivery Characteristics**

  * Guaranteed delivery
  * At most once delivery
  * Ordered delivery
  * Persisted (Alarm notifications).

* **Notification Filtering**

  OpenClovis SAFplus Platform provides service for filtering the notifications based on one or more filter criteria which is particular 
  to the notification type. It also provides the ability to correlate with the other notifications.

Support for SAF AIS Interfaces
------------------------------
OpenClovis SAFplus Platform complies with the SAF AIS interfaces for the following components:

Availability Management Framework (AMF)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis Availability Management Framework (AMF) supports the following SAF AIS interfaces as mentioned in ``SAI-AIS-AMF-B.02.01``.

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| Library Lifecycle Management             | - saAmfInitialize()                                |
|                                          | - saAmfSelectionObjectGet()                        |
|                                          | - saAmfDispatch()                                  |
|                                          | - saAmfFinalize()                                  |
+------------------------------------------+----------------------------------------------------+
| Component Health Monitoring              | - saAmfHealthCheckStart()                          |
|                                          | - saAmfHealthCheckStop()                           |
|                                          | - SaAmfHealthCheckCallbackT                        |
|                                          | - saAmfHealthCheckConfirm()                        |
+------------------------------------------+----------------------------------------------------+
| Component Registration and               | - saAmfComponentRegister()                         |
| Un-registration                          | - saAmfComponentUnregister()                       |
|                                          | - saAmfComponentNameGet()                          |
+------------------------------------------+----------------------------------------------------+
| Component Service Instance Management    | - saAmfHAStateGet()                                |
|                                          | - SaAmfCSISetCallbackT                             |
|                                          | - SaAmfCSIRemoveCallbackT                          |
|                                          | - saAmfCSIQuiescingComplete()                      |
+------------------------------------------+----------------------------------------------------+
| Component Lifecycle Management           | - SaAmfComponentTerminateCallbackT                 |
|                                          | - SaAmfProxiedComponentInstantiateCallbackT        |
|                                          | - SaAmfProxiedComponentCleanupCallbackT            |
+------------------------------------------+----------------------------------------------------+
| Protection Group Management              | - saAmfProtectionGroupTrack()                      |
|                                          | - SaAmfProtectionGroupTrackCallbackT               |
|                                          | - saAmfProtectionGroupTrackStop()                  |
+------------------------------------------+----------------------------------------------------+
| Component Error Reporting                | - saAmfComponentErrorReport()                      |
+------------------------------------------+----------------------------------------------------+
| Component Response                       | - saAmfResponse()                                  |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**Supported API's of AMF**

+----------------------------------------------------+---------------------------------------------------+
| Brief                                              | Unsupported APIs                                  |
+====================================================+===================================================+
| Passive Monitoring of processes is not supported   | - saAmfPmStart()                                  |
|                                                    | - saAmfPmStop()                                   |
+----------------------------------------------------+---------------------------------------------------+
| Freeing the memory allocated by the                | - saAmfProtectionGroupNotificationFree()          |
| saAmfProtectionGroupTrack()                        |                                                   |
+----------------------------------------------------+---------------------------------------------------+
| Component Error Clear API is not supported.        | - saAmfComponentErrorClear()                      |
+----------------------------------------------------+---------------------------------------------------+

.. rst-class:: center

**Unsupported API's of AMF**

Checkpointing Service (CPS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis Checkpointing Service (CPS) supports the following SAF AIS interfaces as mentioned in ``SAI-AIS-CKPT-B.01.01``.

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| Library Lifecycle Management             | - saCkptInitialize()                               |
|                                          | - saCkptSelectionObjectGet()                       |
|                                          | - saCkptDispatch()                                 |
|                                          | - saCkptFinalize()                                 |
+------------------------------------------+----------------------------------------------------+
| Checkpoint Management                    | - saCkptCheckpointOpen()                           |
|                                          | - saCkptCheckpointOpenCallabackT                   |
|                                          | - saCkptCheckpointOpenAsync()                      |
|                                          | - saCkptCheckpointClose()                          |
|                                          | - saCkptCheckpointUnlink()                         |
|                                          | - saCkptActiveReplicaSet()                         |
|                                          | - saCkptCheckpointRetentionDurationSet()           |
|                                          | - saCkptCheckpointStatusGet()                      |
+------------------------------------------+----------------------------------------------------+
| Section Management                       | - saCkptSectionIterationInitialize()               |
|                                          | - saCkptSectionIterationNext()                     |
|                                          | - saCkptSectionIterationFinalize()                 |
|                                          | - saCkptSectionCreate()                            |
|                                          | - saCkptSectionExpirationTimeSet()                 |
|                                          | - saCkptSectionDelete()                            |
|                                          | - saCkptCheckpointWrite()                          |
+------------------------------------------+----------------------------------------------------+
| Data Management                          | - saCkptSectionOverwrite()                         |
|                                          | - saCkptCheckpointRead()                           |
|                                          | - saCkptCheckpointSynchronize()                    |
|                                          | - saCkptCheckpointSynchronizeAsync()               |
|                                          | - SaCkptCheckpointSynchronizeCallbackT             |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**Supported API's of CPS**

Event Manager (EM)
^^^^^^^^^^^^^^^^^^
OpenClovis Event Manager supports the following SAF AIS interfaces as mentioned in ``SAI-AIS-EVT-B.01.01``.

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| Library Lifecycle Management             | - saEvtInitialize()                                |
|                                          | - saEvtFinalize()                                  |
|                                          | - saEvtSelectionObjectGet()                        |
|                                          | - saEvtDispatch()                                  |
+------------------------------------------+----------------------------------------------------+
| Event Operations                         | - saEvtEventAllocate()                             |
|                                          | - saEvtEventFree()                                 |
|                                          | - saEvtEventAttributesSet()                        |
|                                          | - saEvtEventAttributesGet()                        |
|                                          | - saEvtEventDataGet()                              |
|                                          | - saEvtEventPublish()                              |
|                                          | - saEvtEventSubscribe()                            |
|                                          | - SaEvtEventDeliverCallbackT                       |
|                                          | - saEvtEventUnsubscribe()                          |
+------------------------------------------+----------------------------------------------------+
| Event Channel Operations                 | - saEvtChannelOpen()                               |
|                                          | - saEvtChannelOpenAsync()                          |
|                                          | - SaEvtChannelOpenCallbackT                        |
|                                          | - saEvtChannelUnlink()                             |
|                                          | - saEvtChannelClose()                              |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**Supported API's of EM**

+----------------------------------------------------+-----------------------------------+
| Brief                                              | Unsupported APIs                  |
+====================================================+===================================+
| Event Retention Time is not supported              | - saEvtEventRetentionTimeClear()  |
+----------------------------------------------------+-----------------------------------+

.. rst-class:: center

**Unsupported API's of EM**

Group Membership Service (GMS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis Group Membership Service (GMS) supports the following SAF AIS interfaces as mentioned in ``AIS-CLM-B.01.01``.

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| Library Lifecycle Management             | - saClmInitialize()                                |
|                                          | - saClmSelectionObjectGet()                        |
|                                          | - saClmDispatch()                                  |
|                                          | - saClmFinalize()                                  |
+------------------------------------------+----------------------------------------------------+
| Group Membership Operations              | - saClmClusterTrack()                              |
|                                          | - SaClmClusterTrackCallbackT                       |
|                                          | - saClmClusterTrackStop()                          |
|                                          | - saClmClusterNodeGet()                            |
|                                          | - saClmClusterNodeGetAsync()                       |
|                                          | - SaClmClusterNodeGetCallbackT                     |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**Supported API's of GMS**

Messaging Service (MSG)
^^^^^^^^^^^^^^^^^^^^^^^
OpenClovis Messaging Service (MSG) supports the following SAF AIS interfaces as mentioned in ``SAF-AIS-MSG-B.02.01``.

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| Library Lifecycle Management             | - saMsgInitialize()                                |
|                                          | - saMsgSelectionObjectGet()                        |
|                                          | - saMsgDispatch()                                  |
|                                          | - saMsgFinalize()                                  |
+------------------------------------------+----------------------------------------------------+
| Message Queue Operations                 | - saMsgQueueOpen()                                 |
|                                          | - saMsgQueueOpenAsync()                            |
|                                          | - SaMsgQueueOpenCallbackT                          |
|                                          | - saMsgQueueClose()                                |
|                                          | - saMsgQueueStatusGet()                            |
|                                          | - saMsgQueueRetentionTimeSet()                     |
|                                          | - saMsgQueueUnlink()                               |
+------------------------------------------+----------------------------------------------------+
| Management of Message Queue Groups       | - saMsgQueueGroupCreate()                          |
|                                          | - saMsgQueueGroupInsert()                          |
|                                          | - saMsgQueueGroupRemove()                          |
|                                          | - saMsgQueueGroupDelete()                          |
|                                          | - saMsgQueueGroupTrack()                           |
|                                          | - SaMsgQueueGroupTrackCallbackT                    |
|                                          | - saMsgQueueGroupTrackStop()                       |
|                                          | - saMsgQueueGroupNotificationFree()                |
+------------------------------------------+----------------------------------------------------+
| Message Send and Receive Operations      | - saMsgMessageSend()                               |
|                                          | - saMsgMessageSendAsync()                          |
|                                          | - SaMsgMessageDeliveredCallbackT                   |
|                                          | - saMsgMessageGet()                                |
|                                          | - saMsgMessageDataFree()                           |
|                                          | - SaMsgMessagedReceivedCallbackT                   |
|                                          | - saMsgMessageCancel()                             |
+------------------------------------------+----------------------------------------------------+
| Request and Reply Operations             | - saMsgMessageSendReceive()                        |
|                                          | - saMsgMessageReply()                              |
|                                          | - saMsgMessageReplyAsync()                         |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**Supported API's of MSG**

Software Management Framework (SMF)
-----------------------------------
SMF Aligned In Service Software Upgrade (ISSU). Supports application and OpenClovis SAFplus Platform middleware upgrade in a rolling 
(in-service) or single-step mode.

* **Single-Step** For deployment of non-backwards compatible software, or rapid deployment of software. This method stops the relevant 
  services on all nodes (causing an outage) and then upgrades that software and restarts. Note that services are stopped at various 
  granularity levels depending on what is being upgraded. In other words, application A can be taken out-of-service and upgraded across 
  the cluster without affecting application B running on the same nodes.

* **Inservice Rolling** This is the most commonly known telecom quality upgrade method. For deployment of backwards-compatible software 
  across the cluster, this method stops service in one "upgrade unit" at a time, upgrades the software and restarts before stopping the 
  next "upgrade unit". This process continues iteratively until the entire cluster is upgraded. Since the available redundant capacity 
  takes over for the unit being upgraded service will be unaffected.

Hardware Platform Interface (HPI)
---------------------------------
SAFplus Platform has been integrated and tested with the following implementations of ``HPI B.01.01`` specification.

* OpenHPI 2.8.1, 2.10.2, 2.16.0
* Radisys HPI 1.4

The following sections lists out the SAF HPI APIs that are used by SAFplus Platform. Platform provider shall provide at these HPI 
services in order to integration with OpenClovis SAFplus Platform

+------------------------------------------+----------------------------------------------------+
| Services                                 | Supported APIs                                     |
+==========================================+====================================================+
| General APIs                             | - saHpiVersionGet()                                |
+------------------------------------------+----------------------------------------------------+
| Domain APIs                              | - saHpiSessionClose()                              |
|                                          | - saHpiSessionOpen()                               |
|                                          | - saHpiDiscover()                                  |
|                                          | - saHpiRptEntryGet()                               |
|                                          | - saHpiRptEntryGetByResourceId()                   |
|                                          | - saHpiSubscribe()                                 |
|                                          | - saHpiUnsubscribe()                               |
|                                          | - saHpiEventGet()                                  |
+------------------------------------------+----------------------------------------------------+
| Resource APIs                            | - saHpiRdrGet()                                    |
|                                          | - saHpiAutoExtractTimeoutSet()                     |
|                                          | - saHpiAutoInsertTimeoutSet()                      |
|                                          | - saHpiHotSwapPolicyCancel()                       |
|                                          | - saHpiResourceActiveSet()                         |
|                                          | - saHpiResourceInactiveSet()                       |
|                                          | - saHpiHotSwapStateGet()                           |
|                                          | - saHpiHotSwapActionRequest()                      |
|                                          | - saHpiHotSwapIndicatorStateGet()                  |
|                                          | - saHpiResourceResetStateSet()                     |
|                                          | - saHpiResourcePowerStateSet()                     |
+------------------------------------------+----------------------------------------------------+

.. rst-class:: center

**SAF HPI APIs used by SAFplus**

In addition to the above APIs SAFplus Platform also depends on the following events generated by HPI:

* Hot Swap events (``SAHPI_ET_HOTSWAP``)
* Sensor events (``SAHPI_ET_SENSOR``)
* Resource Events (``SAHPI_ET_RESOURCE``)

Modifications to SAF AIS Header files
-------------------------------------
In a few instances, OpenClovis engineers found that the standard SAF-supplied header files caused errors and warnings on certain 
compilers. In these cases OpenClovis modified the standard SAF header file to work with these compilers. All of these changes broaden 
the set of compatible compilers. None of these changes modify the SAF APIs.

For example, in saAis.h, the following constant is defined:

.. code-block:: c

    #define SA_TIME_ONE_MINUTE      60000000000

However, the number defined is greater than a 32-bit integer, so it is actually required to append a size suffix:

.. code-block:: c

    #define SA_TIME_ONE_MINUTE      60000000000LL
