Installation of OpenClovis 6.1 from Github Repository
=====================================================

1. Create a directory (ex: openclovis) and navigate to that directory.
2. Through git download the following repositories from openclovis github.

* SAFplus_IDE.
* SAFplus-Availability-Scalability-Platform.
* 3rdparty.

3. Rename the following repositories.

* SAFplus_IDE to IDE.
* SAFplus-Availability-Scalability-Platform to SAFplus.

4. Navigate to the 3rdparty directory.

* Untar the eclipse-SDK-x.x.x-linux-gtk.tar.gz (for 32-bit) OR
* Untar the eclipse-SDK-x.x.x-linux-gtk-x86_64.tar.gz (for 64-bit)
* Move the eclipse directory to idedev and navigate to idedev  directory.
* Then unzip the fallowing zip files in the current directory (3rdparty directory)

  * emf-runtime-x.x.x.zip
  * GEF-runtime-x.x.x.zip

5. Move the eclipse directory out of 3rdparty directory to openclovis directory.

6. Then unzip the cdt-master-x.x.x.zip file.

7. Navigate to the openclovis directory.

8. If the system is not having openjdk-7, below is url for any more details:

* http://askubuntu.com/questions/55848/how-do-i-install-oracle-java-jdk-7

9. Navigate to 3rdparty directory and then perform make-> generates the 3rdparty-base-x.x.tar

10. Copy the 3rdparty-base-x.x.tar to the openclovis directory.

11. Navigate to IDE directory.

12. export VERSION_TAG=6.1 && export VER=6.1.0 && make -f release.mk

* if it ask PSP, then git clone   SAFplus-Platform-Support-Package and rename it as PSP it generates openclovis-safplus-sdk-6.1-..tar.gz

13. Use install.py file to install OpenClovis to the system.
