Using Github
============

.. note::
    this requires access to OpenClovis private repositories so is only useful for OpenClovis Engineers

Preparation
-----------

* Create a directory "git". "cd" to it.
* Check out SAFplus, IDE, and PSP projects. Rename their subdirectories "SAFplus","IDE", and "PSP".

  * If "PSP" exists, SAFplus will automatically build the chassis manager and AMF will access it.

* Detar "eclipse" 3.7.x "indigo", and the following plugins. You should end up with an "eclipse" directory with all plugins properly 
  placed:

  * cdt-master-7.0.2.zip, emf-xsd-SDK-2.7.1.zip, GEF-SDK-3.7.2.zip
  * These plugins and eclipse are available in the 3rdparty repository, "idedev" subdirectory. Or pull them from their own repositories.

This will create a full SAFplus and IDE development environment.

IDE development
---------------

#. Run eclipse
#. Select import projects
#. Choose IDE as your base directory
#. select all com.* projects
