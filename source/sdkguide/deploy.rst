.. _deploy-safplus-label:

Deploying SAFplus Platform onto the Target
==========================================
This chapter covers various topics related to deploying SAFplus Platform and the SAFplus-based applications onto a given target 
hardware (cluster).

Deploying and Running OpenClovis SAFplus Platform on a Target System
--------------------------------------------------------------------
In order to deploy an OpenClovis SAFplus-based model on to a run-time target system, we need to specify the model's target system 
configuration, and create the run-time images that will be deployed on the target system.  The target system is configured using the 
``target.conf`` configuration file and the run-time images are created using the ``make images`` command.  This step creates run-time 
images for all types of nodes covered by the model (system controller nodes and worker nodes).

.. note::

   Image generation can also be accomplished in IDE. For more information, see *OpenClovis IDE User Guide*.

Target System Configuration - target.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A model's target system configuration is specified using a configuration file - ``target.conf``.  It is located at ``<project_area>/
<model>/src/target.conf``.  Open this file using your favorite editor (*e.g.* ``vi``):

.. code-block:: console

   $ vi <project_area>/<model>/src/target.conf

This file specifies a number of parameters that need to be defined for a given run-time target:

#. **TRAP_IP** (Mandatory): Specifies where the SNMP SubAgent should send traps at runtime.  If you do not have and SNMP SubAgent in 
   your model specify **127.0.0.1** as the value.  *e.g.*:

   .. code-block:: text

      TRAP_IP=127.0.0.1

#. **CMM_IP** (Mandatory if deployed on an ATCA chassis): Specifies the IP address of the target system's chassis management module or 
   shelf manager *e.g.*:

   .. code-block:: text

      CMM_IP=10.10.4.1

#. **CMM_USERNAME**, **CMM_PASSWORD** and **CMM_AUTH_TYPE** (Mandatory if deployed on an ATCA chassis): Specifies the username, password, 
   and authentication type required for the OpenClovis SAFplus Platform Chassis Manager to connect to the target system's chassis 
   management module. *e.g.*:

   .. code-block:: text

      CMM_USERNAME=root
      CMM_PASSWORD=password
      CMM_AUTH_TYPE=md5

#. **INSTALL_PREREQUISITES=YES|NO** (Mandatory): Specifies whether the target images will include 3rd party runtime prerequisites or 
   not.  Say **YES** if the target nodes do not meet the target host requirements specified in the Installation section of this 
   document.  *e.g.*:

   .. code-block:: text

      INSTALL_PREREQUISITES=YES

#. **INSTANTIATE_IMAGES=YES|NO** (Mandatory): Specifies whether ``make images`` will generate node-instance specific images instead of 
   only generating node-type specific images.  This option is a development optimization for advanced users of OpenClovis SDK.  If 
   unsure, say **YES**. *e.g.*:

   .. code-block:: text

      INSTANTIATE_IMAGES=YES

#. **CREATE_TARBALLS=YES|NO** (Mandatory): Specifies whether the node-instance specific images created will be packaged into tarballs 
   for deployment onto the target system.  If unsure, say **YES**.  *e.g.*:

   .. code-block:: text

      CREATE_TARBALLS=YES

#. **TIPC_NETID** (Mandatory): Specifies a unique identifier used by TIPC to set up interprocess communication across the deployed 
   OpenClovis SAFplus Platform cluster.  This is an unsigned 32-bit integer, and *must* be unique for every model that is deployed. *e.g.*:

   .. code-block:: text

      TIPC_NETID=1337

#. **Node Instance Details**: These specify the node-instance specific parameters required for deploying the model. For each node in 
   the model there is a corresponding entry in the file:

   * **SLOT_<node instance name>** (Mandatory): Specifies which slot the node is located at.  When deployed to an ATCA chassis, this 
      corresponds to the physical slot the blade is situated at.  When deployed to regular (non-ATCA) systems, this is a logical slot, 
      and must be unique for every node in the cluster. *e.g.*:

      .. code-block:: text

         SLOT_SCNodeI0=1

   * **LINK_<node instance name>** (Optional): Specifies the ethernet interface used by the node for OpenClovis SAFplus Platform 
      communication with the rest of the cluster.  If unspecified, this defaults to ``eth0``.  *e.g.*:

      .. code-block:: text

         LINK_SCNodeI0=eth0

   * **ARCH_<node instance name>** (Optional if **ARCH** is specified): Specifies the target architecture of the node as a combination 
      of machine architecture (MACH) and linux kernel version.  This is only required on a per-node basis if the target cluster has 
      heterogeneous architectures across the nodes.  If it is a homogeneous cluster, a single **ARCH** parameter (described below) 
      will suffice.  *e.g.*:

      .. code-block:: text

         ARCH_SCNodeI0=i386/linux-2.6.14

   * **ARCH** (Optional if node-specific **ARCH_** parameters are specified): Specifies the target architecture of all nodes in a 
      homogeneous cluster as a combination of machine architecture (MACH) and linux kernel version.  Note: The build process 
      automatically populates this variable based on the last target the model is built for.\ *e.g.*:

      .. code-block:: text

         ARCH=i386/linux-2.6.14

   For example, if we have a three-node cluster with the following details:

   .. list-table:: Example Node Instance Detail
      :header-rows: 1
      :align: center
      :width: 600px

      * - Node Name
        - Slot Number
        - Link Interface
        - Architecture
      * - SCNodeI0
        - 1
        - eth0
        - i386/linux-2.6.14
      * - PayloadNodeI0
        - 3
        - eth0
        - i386/linux-2.6.14
      * - PayloadNodeI1
        - 4
        - eth0
        - ppc/linux-2.6.9

   we would specify the node instance details as:

   .. code-block:: bash

      SLOT_SCNodeI0=1
      SLOT_PayloadNodeI0=3
      SLOT_PayloadNodeI1=4

      LINK_SCNodeI0=eth0
      LINK_PayloadNodeI0=eth0
      LINK_PayloadNodeI1=eth0

      ARCH_SCNodeI0=i386/linux-2.6.14
      ARCH_PayloadNodeI0=i386/linux-2.6.14
      ARCH_PayloadNodeI1=ppc/linux-2.6.9

#. **AUTO_ASSIGN_NODEADDR=default|physical-slot** (Optional): Specifies the scheme that determines how Node Addresses are assigned at 
   run time.  If ``physical-slot`` is specified, the SAFplus Platform startup script will attempt to determine it's own slot number 
   and utilize that instead of the SLOT\_ number specified above if it is able.  If ``default`` is specified, or the value is 
   unspecified, it will function in the default manner of using the SLOT\_ number defined above.

Generating Run-time Images
^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to generate the run-time images based on the target system configuration specified in ``target.conf``, run the following 
command at the ``<project_area>/<model>`` directory:

.. code-block:: console

   $ make images

If ``target.conf`` has been configured to instantiate images and create tarballs as recommended, these are populated at 
``<project_area>/target/<model>/images``.  Each node-specific image is provided as a directory containing the run-time files 
(binaries, libraries, prerequisites, and configuration files) as well as a tarball with the same content.  *e.g.* For a model 
containing three nodes: ``SCNodeI0``, ``PayloadNodeI0`` and ``PayloadNodeI1``, the following are the files and directories generated 
for deployment on the run-time system.

.. code-block:: text

   <project_area>
      |+target
          |+<model>
              |+images
                  |+SCNodeI0
                  |   |+bin
                  |   |+etc
                  |   |+lib
                  |   |+var
                  |-SCNodeI0.tgz
                  |+PayloadNodeI0
                  |-PayloadNodeI0.tgz
                  |+PayloadNodeI1
                  |-PayloadNodeI1.tgz

Copying Images to Run-time System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The node-specific images are deployed to the nodes in the run-time system at ``/root/asp``.  They can be deployed to the target nodes 
in a variety of ways, for example:

#. Using **rsync**:  This option requires an ssh server running on each target node.  In order to use this option, run the following 
   commands on each target node:

   .. code-block:: console

      # cd /root
      # mkdir asp

   On the development host, switch to the target image directory using the following command:

   .. code-block:: console

      $ cd <project_area>/target/<model>/images

   Then, for each node instance <node_instance>, run the following command to copy the image to its corresponding target node at 
   <node_ip>:

   .. code-block:: console

      $ rsync -avH <node_instance>/* root@<node_ip>:asp/.

#. Using the generated node-specific tarballs:
   Copy the node-specific tarballs from the development host to the target nodes using ftp, scp, or any method that is available.  
   *e.g.* To copy the tarballs using ``scp``, switch to the target image directory on the development host using the following command:

   .. code-block:: console

      $ cd <project_area>/target/<model>/images

   Then, for each node instance <node_instance>, run the following command to copy the image to its corresponding target node at 
   <node_ip>:

   .. code-block:: console

      $ scp <node_instance>.tgz root@<node_ip>:.

   On each target node, run the following commands to finish deploying the image:

   .. code-block:: console

      # mkdir /root/asp
      # cd /root/asp
      # tar xzfm ../<node_instance>.tgz

Running OpenClovis SAFplus Platform on the Deployed Run-time System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To start OpenClovis SAFplus Platform on the run-time system, run the following commands as root on each target node:

.. code-block:: console

   # cd /root/asp
   # etc/init.d/asp start

.. seealso::

   If SAFplus Platform fails to start properly it could be due to the machine's firewall being enabled. SAFplus Platform will not run 
   properly with an enabled firewall. See the **Environment Related Observation** section of the **OpenClovis Release Notes** for more 
   information.

.. note::

   By default SCNodeI0, PayloadNodeI0 and PayloadNodeI1 are configured (see target.conf) to use the eth0 ethernet interface. Within 
   each of the nodes this configuration information is stored within the following two files.

   * ``/root/asp/etc/clGmsConfig.xml``
   * ``/root/asp/etc/asp.conf``

   This is not always the case, for example on one of your nodes you may want to switch to eth1. If you would like to do so without 
   changing target.conf and rebuilding the images and redeploying then use your favourite editor, eg vi, to replace the occurrence of 
   eth0 with the appropriate form, e.g. eth1 in these two files.

Deployment of OpenClovis SAFplus Platform on Production Systems
---------------------------------------------------------------
The deployment mechanism described above is well suited for development environments and will also work for production environments.  
However, sometimes different deployment behavior is desired in production environments.  For example, in the above deployment the node's 
"personality" depends on what software (tar file) is loaded and run on the node.  Another option is to have the node's "personality" 
depend on what slot the node is inserted into.  For example, a project that is using physically different blades or deploying rack 
mount servers (i.e. there is no "slot") will likely want the personality to follow the loaded software.  But a project that uses the 
exact same blade in and ATCA chassis may want the personality to follow the slot for simplicity in FRU replacement (i.e. a spare blade 
will automatically use the correct "personality" when inserted in the dead blade's slot).  Alternately, a project that requires a 
specific pairing of blades due to custom hardware or upstream network redundancy will require that the personality follow the slot.

To change the "personality" of a blade edit the "etc/asp.conf" file on your node after the SAFplus Platform software has been deployed.  
This file defines several environment variables:

* **export NODENAME=\<your node name\>**

  This variable controls the node personality. The NODENAME variable defines the node's personality as you specified in the AMF 
  configuration dialog in the OpenClovis IDE.

* **export SYSTEM_CONTROLLER=\<1 or 0\>**

  This second variable defines whether this node is a system controller or not.  Note that this variable cannot be changed to "toggle" 
  system controller functionality -- whether or not the node is a system controller is defined by the node's personality in the 
  OpenClovis IDE and this variable must be set correctly.  It exists due to the internal design of the SAFplus Platform platform; 
  essentially the SAFplus Platform must act as a system controller (or not) before it gains enough information to know whether a 
  particular NODENAME is supposed to be a system controller.

  Therefore to toggle system controller behavior, you must change both NODENAME and the SYSTEM_CONTROLLER variables.

* **export DEFAULT_NODEADDR=\<a positive integer\>**

  This variable is only used in rack-mount systems or systems where OpenClovis SAFplus Platform cannot determine the slot number.  
  Every node in the cluster must be given a unique node address.  In "slot-based" systems, the slot number will be used as the node 
  address, but in systems where OpenClovis SAFplus Platform cannot determine the slot number then this default will be used.

  As an aside, note that to integrate OpenClovis SAFplus's slot numbering with a custom chassis all that must be done is to set this 
  variable to the actual slot number.

Deployment on Machines that Lack Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The mechanics of deployment on diskless machines (i.e using PXE or tftp to get a linux kernel from another node on the network) is 
node and operating system specific and is beyond the scope of the OpenClovis SDK.  However, commonly these methods require that a 
single image be booted on all nodes.  Therefore, the default OpenClovis deployment where the node "personality" is determined by the 
software image is not appropriate.  Instead, deployment on diskless machines can be accomplished using the same strategy used for 
deployment where the personality is determined by the slot, as described in the prior section.

Note that although this strategy was presented using the slot number as the deterministic value it is not limited in this way.  Any 
accessible data can be used to set the NODENAME, SYSTEM_CONTROLLER, and DEFAULT_NODEADDR variables.  Implementation is left to the 
customer but some options include a byte in the node's non-volatile (CMOS or flash) memory, the node's MAC address, a file in a 
mounted NFS volume, or a boot-time parameter.

Setting Up SAFplus Platform On A Multi-Subnet System
----------------------------------------------------
Clustered environments often assume that all nodes in the cluster are connected via the same Layer-2 subnet, such as an Ethernet subnet, 
or often a redundant pair of such subnets.

Indeed, OpenClovis SAFplus Platform has been designed to exploit the benefits of the single-subnet setup to achieve optimal 
communication and failover performance.

However, in certain systems the cluster must span across multiple layer-2 subnets that are connected directly or indirectly over 
layer-3 (IP) routers. Albeit somewhat more involved, SAFplus Platform can be setup for these networks, as it is explained and 
demonstrated in this section.

Requirements on the Subnet Connectivity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SAFplus Platform uses three types of communications among its nodes, all of which must be working in order to provide its functionality:

* IP (UDP) unicast forwarding, used by the Group Membership Service (GMS) protocol
* IP (UDP) multicast forwarding, used also by GMS
* Layer 2 forwarding, used by TIPC for the rest of the inter-node communication

Hence, in order to provide all 3 types of connectivity between the subnets, the router(s) or switch(es) that connect the subnets must 
provide the following capabilities. These capabilitits are rather common in modern routers and switches, and are also provided by 
standard Linux-based systems:

* IPv4 unicast forwarding (routing)
* IPv4 multicast forwarding (multicast routing)
* Ethernet bridging for selected Ethernet frames, based on Ethernet protocol type field

Example Setup Using a Linux-based Router
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Setting up a router to perform the above services is vendor and model specific. Therefore we illustrate the setup for the case when a 
common Linux-based PC is used as a router between the subnets. This configuration can be directly transposed to other commercial 
router products that have the above 3 capabilities.

We assume that the Linux PC has two Ethernet NICs. The steps involves setting up IP forwarding to allow normal traffic to be routed 
across the subnets, creating an Ethernet bridge to allow TIPC traffic to be bridged across the subnets (i.e. see both subnets as one), 
and setting up multicast routing across the subnets to allow SAFplus Platform GMS traffic across the subnets (i.e., again, to see both 
subnets as one).

In our example we assume that the two subnets are:

* ``10.10.0.0/16`` (gateway ``10.10.0.1``)
* ``10.20.0.0/16`` (gateway ``10.20.0.1``)

and our Linux router will have the following two interfaces:

* ``eth0: 10.10.0.99``
* ``eth1: 10.20.0.1`` (gateway for ``10.20.0.0/16`` subnet)

IP Unicast Forwarding
"""""""""""""""""""""
#. Ensure that IP Forwarding is enabled by setting the following in ``/etc/sysctl.conf``:

   .. code-block:: text

      net.ipv4.ip_forward = 1

#. Run the following to reload ``/etc/sysctl.conf``:

   .. code-block:: console

      # sysctl -p

With the two interfaces configured, ensure that the default route points to ``10.10.0.1`` on ``eth0``:

.. code-block:: console

   # route del default
   # route add default gw 10.10.0.1 dev eth0

Note: Ensure that the gateway for the ``10.10.0.0/16`` subnet (in our case ``10.10.0.1``) has a route in place for the ``10.20.0.0`` 
subnet using the following command:

.. code-block:: console

   # route add -net 10.20.0.0 netmask 255.255.0.0 gw 10.10.0.99

Ethernet Bridging for TIPC traffic
""""""""""""""""""""""""""""""""""
You will need the ``ebtables`` and ``bridge-utils`` packages installed, as well as support for Ethernet bridging (802.1d) and ebtables 
enabled in the kernel.

#. Create a new Ethernet bridge using the following:

   .. code-block:: console

      # brctl addbr br0

#. Add ``eth0`` and ``eth1`` to the bridge:

   .. code-block:: console

      # brctl addif br0 eth0
      # brctl addif br0 eth1

#. Bring the bridge interface ``br0`` up:

   .. code-block:: console

      # ifconfig br0 0.0.0.0 up

#. Next, set the default bridge "brouting" policy to ``DROP`` to ensure that all traffic is routed at Layer-3 via iptables as normal:

   .. code-block:: console

      # ebtables -t broute -P BROUTING DROP

#. Finally, allow TIPC traffic (protocol ``0x88ca``) to be bridged across the subnets, bypassing Layer-3 routing:

   .. code-block:: console

      # ebtables -t broute -A BROUTING -p 0x88ca -j ACCEPT

``0x88ca`` is the Ethernet protocol type value for TIPC Ethernet frames.

Multicast Routing Using mrouted for SAFplus Platform GMS Traffic
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
You will need the ``mrouted`` package installed and support for multicast routing enabled in your kernel. Do not proceed before these 
are installed and your kernel is multicast-enabled.

#. Add the following entries to ``/etc/mrouted.conf``:

   .. code-block:: text

      phyint eth0 rate_limit 0 igmpv1
      phyint eth1 rate_limit 0 igmpv1

#. Add the default multicast route to the routing table with the following command:

   .. code-block:: console

      # route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0

#. Start ``mrouted`` using the following command:

   .. code-block:: console

      # mrouted -c /etc/mrouted.conf

   or using the appropriate service startup script, e.g.:

   .. code-block:: console

      # /etc/init.d/mrouted start

   for Red Hat, Gentoo, Ubuntu and other distributions

For more information, please see the `Linux-Mrouted-MiniHOWTO <http://www.jukie.net/~bart/multicast/Linux-Mrouted-MiniHOWTO.html>`_.

Patching SAFplus Platform to Allow GMS Multicast Packets to Traverse the Router
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
In the current version of SAFplus Platform, when the multicast port is opened by GMS, the default TTL value 1 (Linux default) is 
unchanged. Consequently, the router will drop the GMS multicast packets.

To allow multicast routing, the GMS code must be modified to override the default TTL value. When the two subnets are connected 
directly via a router, the TTL=2 value is sufficient. (In case the connectivity involves tunnels and/or multiple routers, a larger TTL 
value may be needed, depending on the number of hops. In order to prevent multicast traffic "leaking" into neighboring subnets, never 
use a TTL value larger than what you really need.)

Hence, the following patch needs to be applied to the code. In the next release of SAFplus Platform, the TTL value will be configurable 
from the GMS configuration file, so this patch is a temporary fix.

.. code-block:: diff

   Index: 3rdparty/openais/openais-0.80.3/exec/totemnet.c
   ===================================================================
   --- 3rdparty/openais/openais-0.80.3/exec/totemnet.c	(revision 1710)
   +++ 3rdparty/openais/openais-0.80.3/exec/totemnet.c	(working copy)
   @@ -885,6 +885,7 @@
    	int addrlen;
    	int res;
    	int flag;
   +    unsigned char ttl;
    	
    	/*
    	 * Create multicast recv socket
   @@ -1066,16 +1067,23 @@
    	 * Set multicast packets TTL
    	 */
    
   -	if ( bindnet_address->family == AF_INET6 )
   -	{
   +	switch ( bindnet_address->family ) {
   +        case AF_INET:
   +        ttl = 2;
   +        if (setsockopt (sockets->mcast_send, IPPROTO_IP, 
   +                IP_MULTICAST_TTL, &ttl, sizeof(ttl)) < 0) {
   +            perror ("cannot set mcast ttl");
   +            return (-1);
   +        }
   +        break;
   +        case AF_INET6:
    		flag = 255;
   -		res = setsockopt (sockets->mcast_send, IPPROTO_IPV6,
   -			IPV6_MULTICAST_HOPS, &flag, sizeof (flag));
   -		if (res == -1) {
   -			perror ("setp mcast hops");
   +		if (setsockopt (sockets->mcast_send, IPPROTO_IPV6, 
   +			IPV6_MULTICAST_HOPS, &flag, sizeof (flag)) < 0) {
   +			perror ("cannot set mcast ttl");
    			return (-1);
    		}
   -	}
   +        break;
   +    }
    
    	/*
    	 * Bind to a specific interface for multicast send and receive

Please copy the above patch into a file, e.g., ``gms_ttl2.patch``, and apply it to the SAFplus Platform source tree as follows:

.. code-block:: console

   # cd <clovis-sdk-dir>/sdk-3.0/src/SAFplus Platform
   # patch -p0 < gms_ttl2.patch

and rebuild SAFplus Platform.

GMS Multicast IP Address Selection
""""""""""""""""""""""""""""""""""
In order to allow GMS multicast packets traverse the router, don't forget to pick a routable multicast address. Addresses between 
``224.0.0.0`` through ``224.0.0.255`` are not routable, but ``224.0.1.0`` or above are routable. This address can be specified in various 
ways, including:

* by using the IDE
* by modifying the target.conf file manually before packaging for deployment
* by modifying the clGmsConfig.xml file on the target nodes after deployment

Bringing Up SAFplus Platform on the Multi-Subnet Cluster
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
At this point SAFplus Platform can be started on nodes connected to either of the two subnets, they will be able to join the SAFplus 
Platform cluster irrespective of their location. Starting, stopping, and using SAFplus Platform is identical to the single subnet case.
