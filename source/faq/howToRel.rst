How To Release SAFplus Platform
===============================

Major Release Checklist
-----------------------

* Migrate all models in SAFplus/src/examples to the latest IDE version

  * Regenerate source, compile and verify

* TAE automated testing passes

Release Procedure
-----------------

#. Check out the TAE project
#. make a working directory for the new release and populate it with Eclipse
#. Edit TAE/packager.xml to reflect the release and the working directory
#. run python packager.py
