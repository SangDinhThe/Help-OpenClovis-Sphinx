Compilation of components Outside IDE
=====================================

Steps
-----

#. After generating code in IDE or Customized code in IDE
#. Goto command-line and Navigate to the Project directory
#. Execute the following command

.. code-block:: console

    #/opt/clovis/6.1/configure 
                or
    #/opt/clovis/6.1/configure --with-model-name=ProjectName 
                or
    #/opt/clovis/6.1/configure --help

#. Navigate to bulid/local directory and do make
#. Finally do make images
