Building your Model
===================

Make
----

How can I add custom targets?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Custom targets can be added into any of your model's makefiles. Please see the makefile for details, and be sure to use the variables 
we define instead of hard-coded paths. Here is an example of adding a target that simply copies a file into the target binary directory:

.. code:: basemake

    all: $(BIN_DIR)/simulation.data

    $(BIN_DIR)/simulation.data: ../simulation.data
        $(MKDIR) $(BIN_DIR)
        $(CP) $< $@

Make Images
-----------

How can I customize tarball creation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a script called <model src>/build/scripts/instantiate.sh. If this script exists, it will be called during "make images" before 
and tarballs are created. This script should utilize shell environment variables defined in the ASP parent "instantiate.sh" file that 
describe paths and locations. Please refer to this file for information, or

How to add custom env variables to the tarball?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a file called <model src>/target.env that contains exactly what you want to appear in the asp.conf file on each node.

How to add custom configuration files to "etc" in the tarball?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Place and .xml, .conf. or .txt custom config files in <model>/configs. These files will end up in <asp_install_dir>/etc.

How to add custom files to any directory in the tarball?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a directory <model>/extras and populate it with your custom files and directories. For example, all files in 
<model>/extras/lib will appear in <asp_install_dir>/lib on the target.

None of the above works for me. What should I do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sorry, we cannot fix everybody's specific customization problem. In your overarching makefile or build script, please detar our tarball 
into a temp directory, make the changes you need, and then tar it back up!
