TIPC Configuration
==================

Overview
--------
OpenClovis uses the `TIPC Linux kernel <https://tipc.sourceforge.net/>`__ module to provide low latency communications between nodes 
in the cluster. However, as configured out-of-the-box, TIPC sometimes has trouble handling the bandwidth required for telecom applications.

This can result in link "flapping" (several rapid link-level drops and reconnects) or dropped packets.

FAQ
---
**How can the TIPC configuration be changed to support higher bandwidth?**

You need to recompile the TIPC module. Directions on compiling kernel modules are all over the internet so shall not be repeated here. 
Increase/modify the following macros in the tipc source code before recompiling tipc module:

* TIPC_DEF_LINK_WIN

  to 250

  in include/net/tipc/tipc_bearer.h

* TIPC_MAX_LINK_WIN

  to 300

  in include/net/tipc/tipc_bearer.h

* BCLINK_WIN_DEFAULT

  to 150 (from 20)

  in net/tipc/bcast.c

**Optional and nice to have in case receiver/machine is running slow to avoid packet drops from tipc (flow control)**

* OVERLOAD_LIMIT_BASE.

  Change the default from 5000 to say 8000 (some tweaking may be necessary based on the difference in performance of your machines)

  in net/tipc/socket.c

* TIPC_FLOW_CONTROL_WIN

  from 512 to say 3000

  in include/net/tipc/tipc_port.h

  This will also alleviate the condition for the reliable or SOCK_STREAM tipc topology notification socket which can also be impacted.

  .. note::
    Make sure that TIPC_FLOW_CONTROL_WIN*2 <= OVERLOAD_LIMIT_BASE

  Then recompile and after reloading tipc and establishing both the links, confirm link window shows 250 instead of the default of 50 with tipc-config -ls=<link-name>

UDP configuration
-----------------

:ref:`Switch your model/image from TIPC to UDP <switch-tipc-udp-label>`


.. toctree::
    :hidden:

    tipcToUdp
