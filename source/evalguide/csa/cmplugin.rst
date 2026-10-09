CM Plug-in Guide
================

Objective
---------
CM-Plugin is an event controlling policy in Platform-Support-Package(PSP) to allow, restrict, or modify the events received from 
HPI and forwarded to the Application during run-time. The policy is defined by the Application programmer and is loaded into the 
Chassis Manager and called whenever a hardware event is received.

The purpose of this plugin is to allow the application programmer to intercept events that may be miscategorized by the hardware 
and transform them. For example, if a voltage loss event is reported as MAJOR in a dual power supply system, this even should not 
cause system shutdown so can be reduced to a MINOR level event.

What you can learn
------------------
How to define a policy to control the events in the CM, so that only interested events are forwarded to the Application and unintended 
events are discarded.

Building the CM-Plugin model and controlling Events in run-time
---------------------------------------------------------------
The example code containing Application and CM-Policy is available in `PSP/src/example <https://github.com/OpenClovis/SAFplus-Platform-Support-Package/tree/master/src/example/CmPlugin>`__

Usage of CM-Plugin
------------------
The policy to control the events is defined in cmPolicy.c and is available in the location: .../CmPlugin/src/app/common/plugins/cmPolicy.c 
in specified example.

* HpiEventFilter() will be contain the details of specific event to be handled and specific modification for that event.
* We shall show the usage of the filter for a SENSOR Event.

.. code-block:: c
    :caption: cmPolicy.c

    ClRcT HpiEventFilter(SaHpiSessionIdT session, SaHpiEventT* event, SaHpiRdrT* rdr, SaHpiRptEntryT* rpt)
    {
        /* Define the policy to Allow, Block or Change the events here */
        if ((event->EventType == SAHPI_ET_SENSOR) && (event->Severity==SAHPI_MAJOR))
        {
             event->Severity = SAHPI_MINOR; /* Changing event severity to minor */
        }
        else if ((event->EventType == SAHPI_ET_SENSOR) && (event->Severity==SAHPI_MINOR))
        {
             event->Severity = SAHPI_MAJOR; /* Changing event severity to minor */
        }    
        return CL_OK;
    }
  
In the above example, the Sensor Events from high severity is changed to lower severity, so that the event is given lower importance 
or can be ignored and other events which are of importance can be received and processed by Application.

How to Run cmPlugin model
-------------------------
Copy the image to new directory (/root/SAFplus/).

* Start the SAFplus Platform on deployed node

  .. code-block:: console

    # cd /root/SAFplus/
    # ./etc/init.d/safplus start

* Generate event using HPI Event Simulator OR through actual hardware

  .. code-block:: console

    # cd /root/SAFplus/bin
    # ./hpithres

The logs are available in var/log/sys.latest and application_name.latest.

Advanced Usage
--------------
The Shelf Manager in AdvancedTCA/MicroTCA is notified about health and management status changes in the shelf via standard IPMI event 
messages that are forwarded to the active Shelf Manager. IPM Controllers are configured to generate event messages when they detect 
a significant condition getting asserted or deasserted in the system. This includes messages for events such as 'temperature threshold 
exceeded', 'voltage threshold exceeded', 'power fault', 'watchdog expired', etc. IPMI event messages are typically associated with a 
Sensor. The type and event type of the Sensor associated with an event helps the Shelf Manager and HPI User decide on actions to be 
taken on account of that event.

HPI layer can handle events for various kinds which can be originated for Resource Details, Domain events, Sensor, Hot-Swap, Watchdog, 
Software-Events, OEM, User events, Dimi, Fumi events. While developing any event specific change either in Middleware or in Application, 
the specific event is allowed from PSP and is received by Application and rest of events are suppressed.

The event received is containing fields which indicate

* Source  : ResourceId of FRU

* EventType : Sensor Type

* TimeStamp : Time when the HPI Server receives the event.

* Severity  : SAHPI_MINOR, SAHPI_MAJOR, SAHPI_CRITICAL

Details in Event Union
----------------------
+--------------------+-------------------------------------+
| Field              | Description                         |
+====================+=====================================+
| SensorEventT       | Event Request Message               |
+--------------------+-------------------------------------+
| SensorNum          | Sensor #                            |
+--------------------+-------------------------------------+
| SensorType         | Type of Sensor (Ex: Voltage, Temp.) |
+--------------------+-------------------------------------+
| EventState         | * SAHPI_ES_LOWER_MINOR              |
|                    |                                     |
|                    | * SAHPI_ES_LOWER_MAJOR              |
|                    |                                     |
|                    | * SAHPI_ES_LOWER_CRITICAL           |
|                    |                                     |
|                    | * SAHPI_ES_UPPER_MINOR              |
|                    |                                     |
|                    | * SAHPI_ES_UPPER_MAJOR              |
|                    |                                     |
|                    | * SAHPI_ES_UPPER_CRITICAL           |
+--------------------+-------------------------------------+
| SensorSpecific     | Event Specific Data.                |
+--------------------+-------------------------------------+

.. raw:: html

   <style>
      .center {text-align: center;} 
   </style>

.. rst-class:: center

**SA Forum APIs with the SAFplus Platform equivalent**

Code Build and Execution details
--------------------------------
The file cmPolicy.c contain the details of policies to inhibit/change the event details is available in location 
.../CmPlugin/src/app/common/plugins/cmPolicy.c in function HpiEventFilter(). For including this file, the make file in location 
.../src/app/common/plugins/Makefile needs to be changed so that the libraries are included as defined by Application while creating 
the image and executed by PSP during the handling of events.

.. code-block:: basemake
    :caption: Makefile in location .../src/app/common/plugins/

    # change PLUGIN_NAME to LIB_NAMES and assign cmPolicy
    LIB_NAMES := cmPolicy

    # ...

    # add cpp flags
    # List any third party libs needed to get this server built (or None):
    CPPFLAGS += -I$(ASP_CONFIG) 
                -I$(CLOVIS_ROOT)/../../PSP/src/cm/include 
                -I$(CLOVIS_ROOT)/../../buildtools/local/include/openhpi

Example Code
------------

.. code-block:: c
    :caption: Sensor Event: Temperature

    ClRcT HpiEventFilter(SaHpiSessionIdT session, SaHpiEventT* event, SaHpiRdrT* rdr, SaHpiRptEntryT* rpt)
    {
        if ((event->EventType == SAHPI_ET_SENSOR) && \
            (event.EventDataUnion.SensorEvent.Assertion == SAHPI_TRUE))
        {
            return CL_ERR_OP_NOT_PERMITTED; /* Event is skipped and is not forwarded to application */
        }
        else
        {    
             event->Severity = SAHPI_MINOR; /* Changing event severity to minor */
        }
        return CL_OK;
    }
  
The Sensor Event is received for a temperature raise is for one of the blades in chassis, which was a false-alarm. To suppress this, 
the severity of that event is reduced to minor, so as to prevent from slot reboot/ shutdown. The same can be extended for false alarms 
in voltage.

.. code-block:: c
    :caption: HOT SWAP Event:

    ClRcT HpiEventFilter(SaHpiSessionIdT session, SaHpiEventT* event, SaHpiRdrT* rdr, SaHpiRptEntryT* rpt)
    {
        if ((event->EventType == SAHPI_ET_HOTSWAP) && \
            (event.EventDataUnion.HotSwapEvent.HotSwapState != event.EventDataUnion.HotSwapEvent.PreviousHotSwapState))
        {
             event->Severity = SAHPI_MAJOR; /* Changing event severity to major */
        }
        else
        {
             event->Severity = SAHPI_MINOR; /* Changing event severity to minor */
        }    
        return CL_OK;
    }
  
When a FRU event is generated which is a false-alarm, these kind of events are blocked by checking whether there is an actual change 
in states by comparing its current state with previous state. If there is a real change in FRU, then only forward this to application 
else block the event.
