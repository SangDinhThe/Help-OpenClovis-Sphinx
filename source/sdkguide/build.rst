.. _build-safplus-label:

Building SAFplus Platform and SAFplus-based Systems
===================================================
This chapter covers features that are related to building SAFplus Platform and SAFplus-based systems.

.. note::
    In the context of this chapter, a target platform is any blade type or architecture that OpenClovis SAFplus Platform can be built 
    for (e.g. WindRiver PNE-LE 1.4 on dual Xeon-based Intel MPCBL0001 blades, or Yellow Dog Linux on PowerPC based blades). OpenClovis 
    provides a variety of cross build toolchains that can optionally be used with the SDK to build SAFplus Platform for these targets.

Working with the OpenClovis SDK involves the following steps:

#. Installing the SDK, which is covered in **OpenClovis Installation Guide**
#. Optionally preparing the SDK for use with the WindRiver Workbench development tools
#. Optionally pre-building SAFplus Platform libraries for a given target platform.
#. Creating a project area (optionally populated with one or more existing SAFplus Platform models)
#. Using the OpenClovis IDE to create a new SAFplus Platform model, generate its code, and modify this code to create desired 
   functionality. This part is covered in **OpenClovis IDE User Guide**
#. Configuring and building the desired model for one or more target platform

Pre-building SAFplus Platform Libraries for a Given Target Platform
-------------------------------------------------------------------
This step builds SAFplus Platform libraries for use with a given platform (i.e. using a specific toolchain). With these in place, it 
is no longer necessary to rebuild SAFplus Platform every time your application is built. When new software is downloaded from github 
or a patch is received from OpenClovis, it is generally not necessary to re-install -- it is only necessary to run this prebuild.

For the purpose of this document, we assume that the SDK is installed at ``/opt/clovis``, by root. Consequently, example steps will be run 
as root. If the SDK is installed as a normal user, that user can run these steps.

By default SAFplus will look in ``/opt/clovis/<sdk version>/prebuild`` for prebuilt libraries, and by default it will have run the prebuild 
in the above directory during installation.

But if you want a separate prebuild, you may create a special project area for the new SAFplus Platform library build, and "cd" to it:

.. code-block:: console

    # mkdir asp_build
    # cd asp_build

Next, this prebuild project area should be initialized with the configure script as:

.. code-block:: console

    # /opt/clovis/<SAFplus version>/src/SAFplus/configure --with-asp-build \
    [--with-sdk-dir=</opt/clovis>] [--with-cross-build=<toolchain>] \ 
    [--prefix=<alternate SAFplus Platform libs installation dir>]

Run ".../configure --help" to see extensive help describing all the available options.

By default, the libraries will ultimately be installed to the SDK installation directory, in this case: ``/opt/clovis/<SAFplus version>/
target/<arch>/<kernel>/lib``, and header files will be available at ``/opt/clovis/<SAFplus version>/include``.

If ``--with-cross-build=<toolchain>`` is unspecified, libraries will be built for the local system.

If ``--prefix=<prefix>`` is specified, libraries will be installed to ``<prefix>/<arch>/<kernel>/lib``, and header files to ``<prefix>/include``

**--with-sdk-dir** is only necessary if the SAFplus source code is not located in the installation directory. In this case ``--with-sdk-dir`` 
is necessary to tell SAFplus where it was installed. This generally only happens if you have placed SAFplus under source code control.

For example:

.. code-block:: console

    # /opt/clovis/sdk-6.0/src/SAFplus/configure --with-asp-build --with-cross-build=i586-wrl-pnele1.4-2.6.14_mpcbl0001

will cause libraries to be built from the i586-wrl-pnele1.4-2.6.14_mpcbl0001 toolchain and installed to ``/opt/clovis/sdk-6.0/target/i386/
linux-2.6.14/lib``, with header files populated at ``/opt/clovis/sdk-6.0/include``, and

.. code-block:: console

    # /opt/clovis/sdk-3.0/src/SAFplus/configure --with-asp-build --prefix=/opt/asplib

on an Ubuntu 7.04 (feisty fawn) system will cause libraries to be installed to ``/opt/asplib/i686/linux-2.6.20/lib``, and header files to be 
populated at ``/opt/asplib/include``.

The following steps build and install the libraries as configured above:

.. code-block:: console

    # make asp-libs
    # make asp-install

Configuring and Building the Model
----------------------------------
In this section, we will configure and build the <model> model. To begin, "cd" to the directory just above the model's directory. This 
directory is called your "project area", and is often named "workspace" or "ide_workspace" by the OpenClovis IDE.

Configure the <model> model for building by running the following:

.. code-block:: console

    $ cd <project_area>
    $ <install_dir>/sdk-6.0/src/SAFplus/configure --with-model-name=<model> \
                                            --with-asp-build

This will configure the <model> model for deployment on the local machine, linking with the "prebuilt" SAFplus libraries (built during 
installation).

To build SAFplus alongside your model use:

.. code-block:: console

    $ <install_dir>/sdk-6.0/src/SAFplus/configure --with-model-name=<model> \
                                            --with-asp-build

You may also "crossbuild" for other CPU Architectures, assuming that you have the compilers, libraries, etc required for that CPU 
(collectively called a "crossbuild toolchain". SAFplus expects the crossbuild toolchain to be located in ``<install_dir>/buildtools/
<toolchain name>``. Please install your toolchain there (or create a symbolic link), and then run:

.. code-block:: console

    $ <install_dir>/sdk-6.0/src/SAFplus/configure --with-model-name=<model> \
                                            --with-asp-build \
                                            --with-cross-build=<toolchain name>

It is possible to configure the model to be built for multiple targets by issuing as many configure commands as necessary. Each run 
sets up a target-specific build location at ``<project_area>/<model>/build``.

If this model is to be deployed on an ATCA-based system with OpenHPI-based shelf management, enable Chassis Manager with:

.. code-block:: console

    $ <install_dir>/sdk-6.0/src/SAFplus/configure --with-model-name=<model> \
                                            --with-asp-build \
                                            --with-cross-build=<crossbuild> \
                                            --with-cm-build=openhpi

.. note::
    Using Chassis Manager requires OpenClovis Platform Support Package, distributed separately from OpenClovis SDK.

For a complete list of options to configure, including a list of available crossbuild toolchains, run:

.. code-block:: console

    $ <install_dir>/sdk-6.0/src/SAFplus/configure --help

The configure step prepares the project area to build the <model> model, with the following directory structure:

.. code-block:: text

    <project_area>
        |ide_workspace
        |+<model>
            |+build
            |   |+local
            |   |   |-Makefile
            |   |+<crossbuild>
            |   |   |-Makefile
            |+src
            |   |+app
            |   |+config
            |   |+doc
            |   |-target.conf
            |+target 
            |-Makefile

Build the configured model by issuing make in ``<project_area>/<model>``:

.. code-block:: console

    $ make

This will build the <model> model for all the targets it has been configured to build. In order to do a target-specific build, issue 
make from the target-specific build location. e.g. for a local build:

.. code-block:: console

    $ cd <project_area>/<model>/build/local
    $ make

For a target supported by the <crossbuild> toolchain:

.. code-block:: console

    $ cd <project_area>/<model>/build/<crossbuild>
    $ make

For a complete list of options to make, run:

.. code-block:: console

    $ make help

The model source is located at ``<project_area>/<model>/src``. If any changes are made to this, rebuild the model by issuing another make 
from either the target-specific build location or the model directory.

.. seealso::
    Model building can also be accomplished in IDE. For more information, see **OpenClovis IDE User Guide**.

Generating tarball archives suitable for deployment on targets
--------------------------------------------------------------
As a development convenience, SAFplus also includes a make target that will create a set of tarballs that can be copied to target 
machines, detared and run. These are created by running

.. code-block:: text

    make images

You may need to edit the ``src/target.conf`` file to describe the tarballs you want produced.

.. note::
    The IDE contains a GUI dialog box that will properly create the target.conf file based on your input.

Using OpenClovis SDK with the WindRiver Workbench
-------------------------------------------------
It is possible to use OpenClovis SDK with the WindRiver Workbench development tools. This section describes an optional step that 
creates a 'virtual' toolchain that allows SAFplus Platform to be built using the WindRiver Workbench development tools for a given 
WindRiver board support package. This also builds the 3rd party prerequisites using the Workbench tools so that they may be deployed 
on the specific platform. It requires both WindRiver Workbench (for the development tools) as well as a WindRiver board support package 
for a specific target platform. Platform specific HPI libraries from Pigeon Point Systems and RadiSys can optionally be built into the 
virtual toolchains using packages supplied by either vendor. It is possible to create as many virtual toolchains as necessary for a 
variety of platforms.

This is done by using the cl-create-wrs-toolchain utility (as root, if OpenClovis SDK was installed as root, or as a normal user if not):

.. code-block:: console

    # cl-create-wrs-toolchain -w <WindRiver Workbench install dir> \
                            -b <bsp name> \
                            [ -l <libhcl_tarball> ] \
                            [ -p <pps_openhpi_tarball> ] \
                            <toolchain_name>

The -l option accepts the full path to a RadiSys-provided libhcl package tarball. If specified, it will be built in to the virtual 
toolchain. The -p option accepts the full path to a Pigeon Point Systems-provided OpenHPI package tarball. If specified, it will be 
built into the virtual toolchain instead of the stock OpenHPI package from the OpenClovis-provided 3rd party package tarball.

e.g.:

.. code-block:: console

    # cl-create-wrs-toolchain -w /opt/WindRiver \
                            -b intel_mpcbl0001 wrs_mpcbl0001

This will create a toolchain called wrs_mpcbl0001 in your existing SDK buildtools directory that is built using the WindRiver 
installation at ``/opt/WindRiver`` for the intel_mpcbl0001 board support package. This toolchain will be visible when using configure 
--help, as will be noted in a following section.

.. note::
    The virtual toolchain requires the WindRiver Workbench installation to be available when it is used, as it merely provides 
    references to the development tools in the Workbench installation. Should the installation be moved or replaced, the virtual 
    toolchain would need to be built again.
