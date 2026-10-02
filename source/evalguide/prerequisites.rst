Hardware and Software Prerequisites
===================================
The OpenClovis SAFplus Platform SDK allows the modeller to define exactly what kind of hardware configuration a model runs on. This 
Evaluation Model has been set up to allow a variety of hardware configurations. You should match your hardware as best as possible 
with one of the configurations described below.

This chapter initially summarizes the configurations you may recreate, followed by a description of the hardware and software specifications.

The hardware set up you wish to choose depends upon two factors:

* whether you wish to use ATCA blades or PCs/laptops/Virtual Machines
* number of PCs/laptops/blades/Virtual Machines you have available

The following table helps you decide which setup you can recreate. For example, if you wish to use an ATCA chassis and have 3 blades 
available, then you may wish to create Hardware Setup 1.2.

+-------------------------------+------------------------------------------------------------------------+
|                               | Hardware Setup                                                         |
|                               +----------------------+------------------------+------------------------+
|                               | Single Node          | 3 Node - Distributed   | 4 Node - Distributed   |
+===============================+======================+========================+========================+
| **Chassis/Blades**            | Hardware Setup 1.1   | Hardware Setup 1.2     | Hardware Setup 1.3     |
+-------------------------------+----------------------+------------------------+------------------------+
| **PCs/Laptops/Virtual         | Hardware Setup 2.1   | Hardware Setup 2.2     | Hardware Setup 2.3     |
| Machines**                    |                      |                        |                        |
+-------------------------------+----------------------+------------------------+------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Hardware Setups**

.. note::
    The word Node here represents either a PC, laptop or blade or Virtual Machine.

Development Environment
-----------------------
The Development Machine is the primary machine where the SAFplus Platform SDK and Evaluation System is installed and built. As 
discussed within this document, the development machine plays an important role in moving System Controller and Payload Node images 
to the runtime environment.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| Development Machine | PC or Laptop or Virtual Machine          | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
|                     |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
|                     |                                          |                                                      |
|                     | Processor - Intel Pentium II (or better) |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Development Machine Environment**

.. note::
    Although a distinction is made throughout this document to separate the two functions of the Development Machine and Management 
    Station Machine, they can in fact be the same PC/Laptop/Virtual Machine.

Runtime Environment
-------------------
A distinction is made between the Development and Runtime Environment as SAFplus Platform will most likely run within an environment 
made up of chassis, blades, shelf managers, switches etc. and be monitored remotely. Hence we have attempted to make this Evaluation 
System simulate the environment it will be used in, as represented in Runtime Hardware Setup 1.1, 1.2 and 1.3 (see Chapter **Runtime 
Hardware Setup**). An alternative setup is also provided, using PCs/Virtual Machines, as discussed in Runtime Hardware Setup 2.1, 2.2 
and 2.3 (again see **Chapter Runtime Hardware Setup**).

Runtime Setup 1.1, 1.2 and 1.3
------------------------------
Runtime Hardware Setup 1.1, 1.2 or 1.3 requires a Chassis and 1, 3 or 4 blade(s) respectively and one PC or laptop or Virtual Machine 
to act as the Management Station Machine. Below is listed the equipment required.

Chassis
^^^^^^^
ATCA chassis with a Shelf Manager.

Management Station Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^
A Management Station is necessary for Runtime Hardware Setup 1.1, 1.2 and 1.3.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| Development Station | PC or Laptop or Virtual Machine          | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
| Machine             |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
|                     |                                          |                                                      |
|                     | Processor - Intel Pentium II (or better) |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Management Station Environment**

.. note::
    It is possible to use a single PC/laptop/Virtual Machine as both host for the development and management machines. Virtual 
    machine environments can also be used with some limitations to the hardware exercises.

System Controller
^^^^^^^^^^^^^^^^^
Runtime Hardware Setup 1.1 and 1.2 required one System Controller.

Runtime Hardware Setup 1.3 requires two System Controllers.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| System Controller   | ATCA Intel (MPCBL0001) Blade             | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
|                     |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**System Controller**

Payload (Blades) Node
^^^^^^^^^^^^^^^^^^^^^
Two Payload nodes are necessary for Runtime Hardware Setup 1.2 and 1.3.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| Two Payload Blades  | ATCA Intel (MPCBL0001) Blade             | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
|                     |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Payload Nodes**

Switch
^^^^^^
10/100Mbps or Gigabit Ethernet switch.

See Chapter **Building the Evaluation System and Deploying Runtime Images** for further installation details.

Runtime Setup 2.1, 2.2 and 2.3
------------------------------
Runtime Hardware Setup 2 is a simpler hardware set up, only requiring PC(s)/laptop(s)/Virtual Machine(s) and a switch. Runtime 
Hardware Setup 2.1, 2.2 or 2.3 requires 1, 3 or 4 PC(s) or laptop(s) or Virtual Machine(s) respectively. In addition a PC or laptop 
or Virtual Machine is needed to act as the Management Station Machine. Below is listed the equipment required.

Management Station Machine
^^^^^^^^^^^^^^^^^^^^^^^^^^
One Management Station is necessary for Runtime Hardware Setup 2.1, 2.2 and 2.3.

+------------------------+------------------------------------------+------------------------------------------------------+
|                        | Hardware                                 | Software                                             |
+========================+==========================================+======================================================+
| Management/Development | PC or Laptop or Virtual Machine          | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                        |                                          |                                                      |
| Station Machine        |                                          |                                                      |
|                        | Hard disk - 10 GB or more                |                                                      |
|                        |                                          |                                                      |
|                        | RAM - 512 MB or more                     |                                                      |
|                        |                                          |                                                      |
|                        | Processor - Intel Pentium II (or better) |                                                      |
+------------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Development Management Machine**

.. note::
    It is possible to use a single PC as the development machine, management machine and simultaneously as the target for a single 
    node. Distributed node exercises will require a second machine. Virtual machine environments can also be used with some 
    limitations to the hardware exercises.

System Controller
^^^^^^^^^^^^^^^^^
Runtime Hardware Setup 2.1 and 2.2 required one System Controller.

Runtime Hardware Setup 2.3 requires two System Controllers.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| System Controller   | PC or Laptop or Virtual Machine          | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
|                     |                                          |                                                      |
|                     | Processor - Intel Pentium II (or better) |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**System Controller**

Payload Node
^^^^^^^^^^^^
Two Payload PCs /laptops/Virtual Machines are required for Runtime Hardware Setup 2.2 and 2.3.

+---------------------+------------------------------------------+------------------------------------------------------+
|                     | Hardware                                 | Software                                             |
+=====================+==========================================+======================================================+
| Two Payload Nodes   | PC or Laptop or Virtual Machine          | Linux Distribution (Ubuntu 7.04 and above preferred) |
|                     |                                          |                                                      |
|                     | Hard disk - 10 GB or more                |                                                      |
|                     |                                          |                                                      |
|                     | RAM - 512 MB or more                     |                                                      |
|                     |                                          |                                                      |
|                     | Processor - Intel Pentium II (or better) |                                                      |
+---------------------+------------------------------------------+------------------------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**Payload Nodes**

Switch
^^^^^^
10/100 Mbps or Gigabit ethernet switch.

See Chapter **Building the Evaluation System and Deploying Runtime Images** for further runtime installation details.

Summary
-------
This chapter provided a list of the equipment required for the development and runtime environment. See Chapter Runtime Hardware 
Setup, for further information concerning setting up the hardware environment. This is followed by Chapter Building the Evaluation 
System and Deploying Runtime Images, which provides information concerning the installation of target images onto the runtime 
environment.
