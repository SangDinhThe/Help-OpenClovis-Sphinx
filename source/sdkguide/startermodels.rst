"Starter" Applications (Models)
===============================
Experts at the OpenClovis IDE can brew a complex redundancy model from scratch in just an hour or two. However building a model from 
scratch is more difficult for a beginner than modifying an existing model. To help new users, the OpenClovis SAFplus Platform provides 
"starter" models that can be used to begin your model. These are different from the ``eval`` kit in that the eval kit is made to showcase 
the features and functionality of the SAFplus Platform and as such are defined to use a very minimal physical (2-3 nodes) layout and 
simple redundancy model. On the other hand, the "Starter" Models are useful models that you may base your model off of.

.. seealso::
    The models are located ``src/examples/ide_workspace`` (IDE model) and ``src/examples/`` (generated code).

The "Starter" Application - IP Address Failover - src/examples/virtualIp
------------------------------------------------------------------------
This starter model implements a commonly-desired feature that is often considered difficult to implement, but becomes very simple on 
top of the OpenClovis SAFplus Platform infrastructure - IP address failover.

The idea behind IP address failover is to have a **virtual IP** address that can be moved from the active blade to another blade when 
the active fails. This is an essential component of many highly available network servers.

The Translation into a SAF/OpenClovis model is very simple. Each Virtual IP address is defined as a **Component Service Instance (CSI)**, 
essentially a **work assignment**. Each ``CSI`` contains the IP Address (e.g. ``192.168.1.2``) and the physical network interface 
(e.g. ``eth0``) on which it should be assigned. When the OpenClovis SAFplus Platform "assigns" the ``CSI`` to a blade, the software 
assigns the IP address to the physical network interface using the standard linux ``ifconfig`` utility. It then issues a **gratituous 
ARP** to notify the larger network of the IP address change. When the OpenClovis SAFplus Platform **removes** the ``CSI`` from a blade, 
the software removes the IP address from the physical network interface using ``ifconfig``.

The only custom code needed is the application-specific code needed to bring up an interface and issue the gratituous ARP.

This model can be packaged with the OpenClovis SAFplus Platform or as an application-only deployable bundle (using SAFplus Platform Web 
Director). To create an application-only bundle, first build SAFplus Platform package normally (i.e. configure; ``make``). Next, go to the 
**virtualIp/bundle** directory and type ``make``. An application tarball will be created.