Platform Management
===================

Overview
--------
OpenClovis ASP integrates with OpenHPI to receive information about your platform. This module is called the Chassis Manager and is 
delivered as an ASP add-on called the Platform Support Package (PSP). The PSP is installed into the ASP tree, overlaying APIs that 
by default are not implemented.

ASP will automatically start and monitor the openhpid binary, but users are expected to set up the openhpi.conf file correctly for 
their system.

The CM will receive OpenHPI events and automatically forward them to the AMF so it can make switchover decisions based on hardware 
conditions. No application intervention is required.

Users are expected to use the HPI APIs directly if hardware configuration information is needed by applications.

FAQ
---

What are the effects of exceeding Critical, Major, and Minor event severity levels?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

HPI Critical events generally cause a shelf manager action (such as powering off the blade -- but note this may depend on your shelf 
manager configuration), major events cause a middleware action (generally the effect is to move services away from the blade), and 
minor events are for the application to handle (if desired).

What hardware events are supported?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All hardware events of severity Major or greater are interpreted by the AMF as an indication to move services away from that blade. 
To disable a

What specific hardware events exist?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The specific events depend entirely on what sensors exist on a particular FRU. You will need to ask your board manufacturer for the 
list. But in general the most valuable and commonly included sensors are for temperature and voltage.

Can non-HPI, 3rdparty, or custome hardware events be integrated to trigger AMF failovers or other actions?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Absolutely! Any entity can call either directly call AMF APIs or issue events to inform the AMF of FRU failure (or recovery). In this 
situation the customer needs to write an application that detects the condition and then calls the AMF API.
