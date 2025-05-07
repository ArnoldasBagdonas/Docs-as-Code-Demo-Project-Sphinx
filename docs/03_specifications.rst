Specifications
========================================================================================

Precise technical description of system behavior, interfaces, and constraints — derived
from high-level requirements and subject to architectural validation.

.. needtable::
   :filter: type == 'spec'
   :columns: id;title;status;tags
   :style: table


Communication Interfaces & Protocols
----------------------------------------------------------------------------------------

.. spec:: USB/UART Protocol Specification
   :id: SPEC_001
   :tags: interfaces, desktop, usb
   :links: REQ_017, REQ_020
   :status: review
   :open_questions: Can this protocol support headless operation?

   - USB/UART interface between the desktop application and LED Controller. Interface with
     the software to set calibration parameters for the LED devices. Allows for configuring
     a device that is plugged into any one of the 4 channels (work with multiple LED panels
     from a single app interface).

   - Available documentation:
   
     - EEPROM flashing guide (Read/write calibration data from/to EEPROM)

     - Communication protocol (for LED panels control and communication with Desktop app)

   - **Review Questions:**

     - Can this protocol support headless operation?


.. spec:: I2C Protocol Specification
   :id: SPEC_002
   :tags: interfaces, led, i2c
   :links: REQ_018, REQ_020
   :status: review
   :open_questions: Should each LED channel have a bus or share one with device addressing?

   - I2C Protocol Specification defines communication between the controller and LED panels.
   
   - **Review Questions:**

     - Should each LED channel have a dedicated I2C bus or share a single bus with addressing?

     - Should the protocol include device addressing, data integrity checks (e.g., CRC), and discovery support?
   

.. spec:: Headless Operation Specification
   :id: SPEC_003
   :tags: interfaces, headless
   :links: REQ_011
   :status: review
   :open_questions: Should this reuse USB/UART or define a new protocol?

   - Unit must also be able to operate headless-ly by receiving serial commands (device control
     without display/buttons) from external devices communicating over the same Client-defined protocol
   
   - **Review Questions:**

     - Should this reuse USB/UART or define a new protocol?


.. spec:: Debug Protocol Specification
   :id: SPEC_004
   :tags: interfaces, debug
   :links: REQ_019
   :status: open

   - The solution shall support the following firmware update mechanism: flashing the firmware with the debugger

Hardware
----------------------------------------------------------------------------------------

.. spec:: LED Controller (MCU) Specification
   :id: SPEC_005
   :tags: hardware, controller
   :status: open

   - 4x I2C (dedicated bus per LED channel)
   - 4x PWM (independent power control per channel)
   - 1x USB Device (desktop interface)
   - 1x USB Host (headless interface)
   - 1x Display interface


.. spec:: Physical Power Switch Specification
   :id: SPEC_006
   :tags: hardware, switch
   :links: REQ_013
   :status: open

   - Physical Power Switch Specification defines power switching capability (e.g., 746W total).

   - Includes mechanical and electrical lifetime specifications.

   - **Note:** The Client will provide guidance as to where on the enclosure any buttons are to be
     located. It is assumed that the documentation of target control logic, user actions, and
     transitions will be provided by the Client.


.. spec:: Controls/Buttons Specification
   :id: SPEC_007
   :tags: hardware, ui
   :links: REQ_014
   :status: review
   :open_questions: Should we prioritize modern UX or industrial-grade components?

  
   - “Channel cycle” button, that will cycle between channels 1, 2, 3, 4, 1, 2... etc. each time it is pressed.

   - Buttons, including the “start” button and/or dial, are the responsibility of the contractor.
   
   - **Note:** The Client will provide guidance as to where on the enclosure any buttons are to be
     located. It is assumed that the documentation of target control logic, user actions, and
     transitions will be provided by the Client.
   
   - **Review Questions:**

     - Should we explore modern UX (e.g., [DIY haptic input knob: BLDC motor + round LCD](https://www.youtube.com/watch?v=ip641WmY4pA)) or
       prioritize industrial-grade components?
     
     - What are the ingress protection (IP) and durability requirements?


.. spec:: Display Specification
   :id: SPEC_008
   :tags: hardware, display
   :links: REQ_008, REQ_009, REQ_010
   :status: review
   :open_questions: What resolution and backlighting specs are required?

  
   - Ability to display conditions for all 4 channels at once (on a “main screen”)
   - Display parameters: wavelength, stage #, power output, timer etc.
   - The color wavelength must be displayed on screen in nanometers (nm) at all times. 
   - Background color of each individual channel should be able to change based on a given wavelength. For example, given a 470nm (blue) wavelength, the channel background on the screen should also be blue with this format applying to each distinct color wavelength and channel.
   - Choose which radiometric power unit is displayed for all channels at once (8 options, all data and calculation formulas provided by the Client). The user should have the ability to select the radiometric power unit they desire via one of the buttons, encoder dial, or other method.
   - **Note:** The Client is responsible for the creation of graphics to be used on the Control Panel screen, including content to be displayed (such as text notifications). 

   - **Review Questions:**

     - What resolution and backlighting specifications are required?
     - Should the display be readable in high-brightness environments, such as direct sunlight?
     
.. spec:: Fan Specification
   :id: SPEC_009
   :tags: hardware, fan
   :links: REQ_012
   :status: review
   :open_questions: Should the controller provide a control signal or only power?

   - The Controller shall provide fan support for the arays which have active cooling.
     The fans should be always ON as long as there is power, no turn on/off logic.

   - **Review Questions:**

     - Should the controller provide a control signal or only power?

     - What are the power requirements for the fans?

     
.. spec:: LED Power Supply Specification
   :id: SPEC_010
   :tags: hardware, waveform, frequency, power
   :links: REQ_004, REQ_005, REQ_006, REQ_020, REQ_022
   :status: review
   :open_questions: Are there flicker, ripple, or EMI constraints to account for?

   - The LED Controller is able to supply 4 devices
   
   - Each channel will carry 3.33A at 56V (~186.5W each channel) resulting in about 746W of total power.
   
   - The contractor will be responsible for selecting the power supply
   
   - 5 power levels/stages per channel (configurable)
   
   - Ability to run all 4 channels simultaneously at max output
   
   - The controller must also be able to accommodate periods of long use at the maximum power outputs on all 4 channels (continuous duty)

   - **Review Questions:**

     - Are there specific requirements for flicker, power ripple, or EMI?

.. spec:: Audio Feedback Specification
   :id: SPEC_011
   :tags: hardware, audio
   :links: REQ_016
   :status: review
   :open_questions: Are tone and volume specs defined or should we use a reference design?

   - Once a channel gets fired, an audible tone is produced. This serves as an audio-visual warning to personnel in the
     vicinity that a high-power light device is about to illuminate.

   - **Review Questions:**

     - Are sound level and tone frequency specifications available, or should we refer to a reference design?


.. spec:: Mechanical Specification
   :id: SPEC_012
   :tags: hardware, audio
   :links: REQ_020
   :status: review
   :open_questions: Can we estimate space/dimensions for new components?

   - All components (main board, display module, power supplies) must fit within enclosure dimensions provided by the Client.

   - All industrial and mechanical design activities are on the Client side.

   - It is assumed that the Client will provide a CAD file boundary (.step file) that indicates maximum product extents as well as placement and maximum component dimensions.

   - **Review Questions:**

     - What is the volume and layout of the existing design?

     - Can we estimate size increases for added functionality?
