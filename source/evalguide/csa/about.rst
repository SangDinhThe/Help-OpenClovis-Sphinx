About Sample Applications
=========================
Each sample application demonstrates a different feature of SAFplus Platform, by showing particular APIs and their usage. Some of 
the features demonstrated are Checkpointing, Provisioning, Component Failover, Event Subscription and Publication. These are 
itemized further within Table **Clovis Sample Applications**.

The numbering of the application follows a general guideline. csa101 through csa113 are designed to demonstrate one particular 
feature of SAFplus Platform at a time. In addition higher numbered sample application tend to build on concepts introduced in lower 
numbered applications.

The sample applications are located within:

<project-area_dir>/eval/src/app

SA Forum Compliance
-------------------
Adherence to standards is a critical requirement for Next Generation Network deployments. The Service Availability Forum (SA Forum) 
is the primary standards body in the context of High Availability Middleware and enjoys the participation of over 95% of Tier 1 
TEMs. OpenClovis has been actively participating in the forum and helping to drive the emerging Hardware Platform Interface (HPI) 
and Application Interface Specification (AIS) standards based on its experience.

As a result of the close involvement of OpenClovis with the SA Forum, the OpenClovis product is aligned with the SA Forum standards 
which specifies a Highly Available (HA) Applications Framework. The framework defines various services such as Availability Management 
Framework (AMF), Checkpointing, Group Membership and Event Services.

In this chapter we also introduce a SA Forum compliant variance of the Clovis Sample Applications, using SA Forum APIs rather than 
OpenClovis APIs. These sample applications are labeled as the 200 series and are functionally equivalent to the Clovis Sample 
Application 100 series. The main difference is in using SA Forum APIs rather than OpenClovis APIs. For example csa101 has a SA Forum 
functionally equivalent, labeled csa201, where the only real differences are in function names, eg. clCpmClientInitialize and 
clCpmComponentNameGet have the SA Forum equivalent saAmfInitialize and saAmfComponentNameGet.

Since SA Forum does not cover various services provided by SAFplus Platform we will limit sample applications to only those services 
which SA Forum has defined.

The SA Forum equivalent sample applications are located within:

<project-area_dir>/eval/src/app

Clovis Sample Applications
--------------------------
The following table provides a brief descriptions of the sample applications found within this Evaluation Guide. For a detailed 
description of how to create and build csa101 using OpenClovis IDE and OpenClovis SAFplus Platform, see the OpenClovis Sample 
Application Tutorial.

+-----------+-----------------------------+------------------------------------------------------------+
| App. Ref. | Scope                       | Description                                                |
+===========+=============================+============================================================+
| csa101    | Basic component             | Periodic Hello World message, can be suspended/resumed,    |
|           |                             |                                                            |
|           | management                  | started/shutdown/killed from CPM via the SAFplus           |
|           |                             |                                                            |
|           |                             | Platform Console.                                          |
+-----------+-----------------------------+------------------------------------------------------------+
| csa102    | Basic redundancy            | csa101 plus capable of starting one active and one         |
|           |                             |                                                            |
|           | and failover                | standby instances. Only active prints messages.            |
|           |                             |                                                            |
|           |                             | Once active is killed (emulating a crash or by             |
|           |                             |                                                            |
|           |                             | a manual switch-over), standby becomes active and print    |
|           |                             |                                                            |
|           |                             | messages. standby becomes active and print messages.       |
+-----------+-----------------------------+------------------------------------------------------------+
| csa103    | Failover and                | csa102 plus a incremented sequence number (SN) is          |
|           |                             |                                                            |
|           | checkpointing               | printed with each message. The SN is checkpointed          |
|           |                             |                                                            |
|           |                             | to standby, so standby continues from where the            |
|           |                             |                                                            |
|           |                             | active left off.                                           |
+-----------+-----------------------------+------------------------------------------------------------+
| csa104    | Basic app.                  | csa103 plus the frequency of the print is configurable     |
|           |                             |                                                            |
|           | manageability               | at run-time via a managed attribute. This attribute is     |
|           |                             |                                                            |
|           |                             | exposed by both the SAFplus Platform Console as well as    |
|           |                             |                                                            |
|           |                             | SNMP, and the MIB is provided for this.                    |
+-----------+-----------------------------+------------------------------------------------------------+
| csa105    | Alarm Management            | Demonstrates how provisioning and alarm libraries work     |
|           |                             |                                                            |
|           |                             | together to achieve a simple software alarm management,    |
|           |                             |                                                            |
|           |                             | and how COR change notification is utilized.               |
+-----------+-----------------------------+------------------------------------------------------------+
| csa112    | Event Subscription          | Demonstrates how to use Clovis' event service to subscribe |
|           |                             |                                                            |
|           |                             | to events.                                                 |
+-----------+-----------------------------+------------------------------------------------------------+
| csa113    | Event Publisher             | How to publish events using Clovis' Event Manager API      |
+-----------+-----------------------------+------------------------------------------------------------+

.. raw:: html

    <style>
        .center {text-align: center;} 
    </style>

.. rst-class:: center

**Clovis Sample Applications**

Starting and Stopping SAFplus Platform
--------------------------------------

Starting SAFplus Platform
^^^^^^^^^^^^^^^^^^^^^^^^^
To start SAFplus Platform on System Controller node.

#. Open a shell.
#. ssh into the System Controller node as root.
#. once logged in, at /root run the following commands

   .. code-block:: text

      # cd asp
      # etc/init.d/asp start

.. note::
    If SAFplus Platform fails to start properly it could be due to the machine's firewall being enabled. SAFplus Platform will not 
    run properly with an enabled firewall. See the Environment Related Observation section of the OpenClovis Release Notes for more 
    information.

.. note::
    Only one System Controller can run in an active state, on a subnet at one time.

Repeat steps 1 to 3, for Payload Node 1 and 2, if any.

At this point, we don't have any applications running on these blades. They are available, but not started. We can start/stop the 
sample applications by Unlocking/Locking the Service Group (this is SA Forum terminology) corresponding to each application using 
the OpenClovis SAFplus Platform Console. This method is described further within Section **How to Run csa102 and What to Observe**. The 
start/stop mechanism is to allow us to run 1 application at a time, so we are not flooded with the output from all the applications, 
all intermixed.

As the reader progresses through this chapter, each application will be discussed, various code snippets will be highlighted to 
explain SAFplus Platform capabilities, and you will then be given the commands to start that particular sample running, allowing 
you to examine the output from the sample.

.. note::
    By default SCNode0, SCNode1, PayloadNode0 and PayloadNode1 are configured (see target.conf) to use the eth0 ethernet interface. 
    Within each of the nodes this configuration information is stored within the following two files.

    * /root/asp/etc/clGmsConfig.xml
    * /root/asp/etc/asp.conf

    This is not always the case, for example on one of your nodes you may want to switch to eth1. If you would like to do so without 
    changing target.conf and rebuilding the images and redeploying then use your favourite editor, eg vi, to replace the occurrence 
    of eth0 with the appropriate form, e.g. eth1 in these two files.

Stopping SAFplus Platform
^^^^^^^^^^^^^^^^^^^^^^^^^
To stop SAFplus Platform on the System Controller

#. Open a shell.
#. ssh into the System Controller node as root.
#. once logged in, at /root run the following command

.. code-block:: text

    # cd asp
    # etc/init.d/asp stop

As mentioned within Section **Starting SAFplus**, repeat steps 1 to 3, for the Payload nodes, if any. The steps clean up the SAFplus 
Platform processes and \*.db files.

Sample Application Output
-------------------------
Purely to ease the output from the collection of Sample Applications, Clovis has used an approach to logging output with the use of 
printf(). These files are output with the aid of the "ev" library and the ev.h header file. The header file is located within the 
below directory.

.. code-block:: text

    <project-area_dir>/eval/src/app/ev
