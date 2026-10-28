.. _tipc-build-gd-label:

TIPC build and install Guide
============================
**TIPC build and install Guide** provides the build and installation procedures for TIPC on Linux Operating System.

Steps
-----

1. login as root
2. install package kernel-devel, gcc, ncurses-devel
3. extract tipc1.7.7.oc.tar.gz to folder tipc1.7.7.oc
4. move to kernel folder(\usr\src\'uname -r') then copy source from tipc to kernel (tipc1.7.7.oc/net, tipc1.7.7.oc/include)
5. copy .h to library header

   .. code-block:: console

    # cp -f tipc-1.7.7.oc/include/linux/tipc.h /usr/include/linux/
    # cp -f tipc-1.7.7.oc/include/linux/tipc_config.h /usr/include/linux/

6. save old config

   .. code-block:: console

    # make oldconfig

7. configure tipc

   .. code-block:: console

    # make menuconfig

..
    this is for breaking code-block
..

     * Main menu then choose -> Network Support -> Networking options -> The TIPC Protocol (EXPERIMENTAL) -> input M 

       * Enter The TIPC Protocol (EXPERIMENTAL) 
       * TIPC: Advanced configuration -> input Y
       * enable debug messages -> input Y
       * other items choose default
       * choose Exit until go to main menu

     * Main menu -> Save an Alternate Configuration File -> save to .config

8. prepare

   .. code-block:: console

    # make modules_prepare (in this step if you see menu, then input-> yes to all)

9. initialization

   .. code-block:: console

    # make init

10. build TIPC module

   .. code-block:: console

    # make M=net/tipc modules

11. install

   .. code-block:: console

    # make M=net/tipc modules_install

12. add path to tipc.conf

   .. code-block:: console

    # echo "install tipc insmod /lib/modules/`uname -r`/extra/tipc.ko" >> tipc.conf

13. copy config tipc

   .. code-block:: console

    # cp -f tipc.conf /etc/modprobe.d/

14. check tipc works or not

   .. code-block:: console

    # modprobe tipc
    # depmod -a -F /boot/System.map-`uname -r` `uname -r`
    # /sbin/modinfo tipc
