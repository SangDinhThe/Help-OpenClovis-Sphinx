amsDbXMLPrint timeout
=====================

Symptom Statement
-----------------
The safplus_console command "amsdbxmlprint console" can hang.

The safplus_info command "forest" times out.

Diagnosis
---------
These commands can timeout if the rmem_default/max buffer in the kernel gets exceeded which results in packet drops. This will 
happen with a large model since the amsdbxmlprint command dumps the entire cluster configuration as XML data. If the "console" 
modifier is removed, the command should work since it dumps into file on the controller. The default rmem_default/max is around 128k.

Solution
--------
Increase the rmem defaults through a proc write:

.. code-block:: bash

    echo 10000000 > /proc/sys/net/core/rmem_default
    echo 10000000 > /proc/sys/net/core/rmem_max

Now try the amsdbxmlprint console command and see it work. Of course, the cluster has to be up with SAFplus running.

Make it persistent across reboots with a /etc/sysctl.conf entry:

.. code-block:: bash

    net.core.rmem_default = 10000000
    net.core.rmem_max = 10000000
