.. _switch-tipc-udp-label:

Switch your model/image from TIPC to UDP
========================================
UDP can be run in two modes -- local or cloud. In local mode, the UDP system uses multicast to find members of the cluster and 
auto-assigns non-routable IP addresses onto an alias of your chosen backplane network interface. The advantage of local mode is 
that no IP addresses need to be configured.

In cloud mode, it is assumed that the cluster is potentially running across the entire internet (no multicast) on machines with 
specified IP addresses. Since no initial discovery is possible, every node needs to be configured with the IP addresses of the two 
system controller nodes.

Changing Your Model from TIPC to UDP
------------------------------------

Step 1
^^^^^^
If you have a pre-60 model you will need to upgrade it. Using the IDE open your model, every option will be grey except model->update. 
This update will generate a configuration file called <your model>/config/clTransport.xml that looks something like this:

.. code-block:: mxml

    <?xml version="1.0" encoding="UTF-8"?>
    <openClovisAsp>
        <version v0="4.0.0">
        <multixport xmlns="multixport.ecore">
            <xports>
            <xport>
                <type>TIPC</type>
                <plugin>libClTIPC.so</plugin>
            </xport>
            </xports>
        </multixport>
        </version>
    </openClovisAsp>

Step 2
^^^^^^
Edit the content clTransport.xml with the UDP configuration details, and remove the TIPC details:

.. code-block:: mxml

    <?xml version="1.0" encoding="UTF-8"?>
    <openClovisAsp>
        <version v0="4.0.0">
        <multixport xmlns="multixport.ecore">
            <xports>
            <xport>
                <type>UDP</type>
                <plugin>libClUDP.so</plugin>
            </xport>
            </xports>
            <protocol default="UDP"/>
            <multicast address="226.0.1.1" port="9595" />
            <heartbeat>
                <interval>3000</interval>
                <intervalLocal>3000</intervalLocal>
                <retries>5</retries>
            </heartbeat>
        </multixport>
        </version>
    <openClovisAsp>

Step 3 (Local mode)
^^^^^^^^^^^^^^^^^^^
Add 2 environment variables into <model_dir>/src/target.env, or make sure these variables are defined before starting SAFplus:

.. code-block:: bash

    export ASP_UDP_SUBNET=<IP Range>/Length
    export ASP_UDP_LINK_NAME=<your interface>

Example:

.. code-block:: bash

    export ASP_UDP_SUBNET=192.168.57.0/24
    export ASP_UDP_LINK_NAME=eth0

Step 3 (Cloud mode)
^^^^^^^^^^^^^^^^^^^
To use the UDP transport without node discovery (multicast) or IP address assignment, you must:

* Add these 2 environment variables into <model_dir>/src/target.env, or make sure these variables are defined before starting SAFplus:

  .. code-block:: bash

    ASP_UDP_USE_EXISTING_IP=true

    ASP_UDP_LINK_NAME=<link name, for example 'eth0'>

* Configure UDP peer addresses like this:

  .. code-block:: mxml

    <peerAddresses port="6789">
        <peer addr="192.168.56.101"/>
        <peer addr="192.168.56.102"/>
    </peerAddresses>

  The following is a this complete example of a cloud mode configuration file:

  .. code-block:: mxml

    <?xml version="1.0" encoding="UTF-8"?>
    <openClovisAsp>
        <version v0="4.0.0">
            <multixport xmlns="multixport.ecore">
                <xports>
                    <xport>
                        <type>UDP</type>
                        <plugin>libClUDP.so</plugin>
                    </xport>
                </xports>
                <protocol default="UDP"/>
                <heartbeat>
                    <interval>1000</interval>
                    <intervalLocal>1000</intervalLocal>
                    <retries>4</retries>
                </heartbeat>
                <peerAddresses port="6789">
                    <peer addr="192.168.56.101"/>
                    <peer addr="192.168.56.102"/>
                </peerAddresses>
            </multixport>
        </version>
    </openClovisAsp>

Before or After "make images"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
clTransport.xml and target.env can be changed before the "make images" step so all generated images are UDP by default OR these files 
can be changed on every node after deployment.

FAQ / Troubleshooting
---------------------

Is the SAFplus able to run in UDP local mode as a non-root user?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A: Yes, but you must properly configure the interfaces since SAFplus cannot.

Configure interface name (ASP_UDP_LINK_NAME) with the IP address calculated from your subnet and node address 
(ASP_UDP_SUBNET.DEFAULT_NODEADDR). The node address is the DEFAULT_NODEADDR settings from etc/asp.conf file.

.. code-block:: bash
    :caption: Example

    root:#ifconfig eth0 192.168.57.1
    user:#export ASP_UDP_SUBNET=192.168.57.0/24
    user:#export ASP_UDP_LINK_NAME=eth0
    user:#./etc/init.d/safplus start

In UDP LAN mode, nodes do not discover each other
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can determine this by running bin/safplus_info command "nodes" to see what nodes are alive.

A: UDP broadcast packets are being dropped. This could be a router configuration, but is more likely a configuration in your Linux 
distribution's firewall software. Disable the firewall or add rules to allow UDP broadcast. How do to this depends on your distro:

.. code-block:: text
    :caption: Examples

    Centos 7: systemctl stop firewalld
    Ubuntu:   service iptables stop

In UDP mode, the software still tries to load the TIPC kernel module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A: TIPC is still specified as a backup communications protocol. Edit etc/clTransport.xml (on all nodes) and remove the 
<xport><type>TIPC ... </xport> block. Also edit etc/asp.conf and set "export BUILD_TIPC=0" (rather than =1).



