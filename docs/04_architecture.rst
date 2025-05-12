Architecture
========================================================================================
High-level system structure and how components interact.

.. needtable::
   :filter: type == 'arch' or type == 'feat'
   :columns: id;title;status;tags
   :style: table


LED Controller
----------------------------------------------------------------------------------------

Logical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. arch:: LED Controller - Logical View
   :id: ARCH_001
   :tags: controller, interfaces, ui, hardware
   :links: ARCH_004, ARCH_005
   :status: review
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/LEDControllerLogicalView.drawio.png
      :width: 800
      :align: center
      :alt: Logical View


Process View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. arch:: LED Controller - Process View
   :id: ARCH_004
   :tags: actors,user
   :links: REQ_003, SPEC_003, REQ_007, SPEC_007, SPEC_008, SPEC_009, SPEC_010, SPEC_011, FEAT_001, FEAT_002, FEAT_003
   :status: open

   
   .. image:: _static/images/diagrams/LEDControllerProcessView.drawio.png
      :width: 800
      :align: center
      :alt: Development View


Development View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. arch:: LED Controller - Development View
   :id: ARCH_003
   :tags: actors,user
   :links: ARCH_001
   :status: open

   
   .. image:: _static/images/diagrams/LEDControllerDevelopmentView.drawio.png
      :width: 800
      :align: center
      :alt: Development View


Physical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. arch:: LED Controller - Physical View
   :id: ARCH_005
   :tags: actors,user
   :links: SPEC_006, SPEC_001, SPEC_002, SPEC_004, SPEC_012, REQ_001, REQ_002, SPEC_010
   :status: open


   .. image:: _static/images/diagrams/LEDControllerPhysicalView.drawio.png
      :width: 800
      :align: center
      :alt: Physical View


Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. feat:: LED Controller - Channel setup
   :id: FEAT_001
   :tags: actors,user
   :links: REQ_035
   :status: open


   .. needuml::

      ' === Global Style Settings ===
      ' skinparam backgroundColor transparent
      ' skinparam shadowing false
      ' skinparam monochrome false

      ' === Font Styling ===
      skinparam defaultFontName "Consolas, Courier New, monospace"
      skinparam defaultFontSize 14
      
      actor System #E1EAFF
      participant InputTask  #E1EAFF
      participant ControllerTask  #E1EAFF
      participant "LEDChannel[n]Task" as LEDChannelTask   #E1EAFF
      participant ViewTask  #E1EAFF
      participant "Timer[n]" as Timer  #E1EAFF
      participant "DMA/PWM Driver[n]" as DMA  #E1EAFF
      participant "I2C Driver[n]" as I2CDriver #E1EAFF
      participant "Display Driver" as Display  #E1EAFF
      participant Buzzer  #E1EAFF
      
      System -> LEDChannelTask : systemInitCompleted event

      LEDChannelTask -> Timer : LEDChannel[n].startSettingsTimer()

      note right of LEDChannelTask
         Initial state DISCONNECTED
      end note

      loop#Gold While in DISCONNECTED state and LEDChannel[n].hasMissingSettings()
         Timer -> LEDChannelTask : settingsRequest event
         LEDChannelTask -> I2CDriver: LEDChannel[n].tryReadSettings()
         alt#Gold #BFD8D2 Successful case
            I2CDriver -> LEDChannelTask: settings(calibration, stage)
            note right of LEDChannelTask
               State changed to IDLE
            end note
            
            LEDChannelTask -> ControllerTask: cableConnected event
            ControllerTask -> ControllerTask: LEDChannelTask[n].applySettingsFrom(LEDChannel[n])
            note right of ControllerTask
               Provide settings. Settings (waveform, frequency, stage,
               timer/count up) are specified PRIOR to arming sequence
            end note

            LEDChannelTask -> ControllerTask : stateChanged event
            ControllerTask -> ViewTask : renderView event
            ViewTask -> Display : Render Screen
            note right of ViewTask
               Recolor the channel window with LED wavelength color used
            end note
         else #FEDCD2 Failure
            I2CDriver -> LEDChannelTask: not connected
         end
         
      end


.. feat:: LED Controller - Channel arming
   :id: FEAT_002
   :tags: actors,user
   :links: REQ_024, REQ_035
   :status: open


   .. needuml::

      ' === Global Style Settings ===
      ' skinparam backgroundColor transparent
      ' skinparam shadowing false
      ' skinparam monochrome false

      ' === Font Styling ===
      skinparam defaultFontName "Consolas, Courier New, monospace"
      skinparam defaultFontSize 14
      
      actor User #E1EAFF
      participant InputTask  #E1EAFF
      participant ControllerTask  #E1EAFF
      participant "LEDChannel[n]Task" as LEDChannelTask   #E1EAFF
      participant ViewTask  #E1EAFF
      participant "Timer[n]" as Timer  #E1EAFF
      participant "DMA/PWM Driver[n]" as DMA  #E1EAFF
      participant "I2C Driver[n]" as I2CDriver #E1EAFF
      participant "Display Driver" as Display  #E1EAFF
      participant Buzzer  #E1EAFF
      
      == Channel Arming Sequence ==

      
      User -> InputTask : press ARM button
      InputTask -> ControllerTask : armingRequest event
      group#Gold While LEDChannel[n] in READY state
         ControllerTask -> LEDChannelTask : armingRequest event
         note right of LEDChannelTask
            State changed to ARMING
         end note
      end

      LEDChannelTask -> ControllerTask : stateChanged event
      ControllerTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen


      LEDChannelTask -> Timer : LEDChannel[n].startArmingTimer()
      note right of LEDChannelTask
         Armed state timeout (10s)
      end note
      LEDChannelTask -> DMA : LEDChannel[n].startArmingWaveform()
      note right of LEDChannelTask
         Execute arming sequence (blinking should be
         done al lowest possible amperage at 1.5Hz)
      end note
      
      loop#Gold While LEDChannel[n].hasIncompleteArming()
         Timer -> LEDChannelTask: tick event
         LEDChannelTask -> LEDChannelTask: armingUpdate()
         note right of LEDChannelTask
            Once a channel gets fired, an audible tone is produced
         end note
         LEDChannelTask -> Buzzer
         note right of LEDChannelTask
            Indicate arming (1.5Hz, yellow color on the display)
         end note
         LEDChannelTask -> ControllerTask : stateChanged event
         ControllerTask -> ViewTask : renderView event
         ViewTask -> Display : Render Screen
      end
      
      ... after arming complete ...

      Timer -> LEDChannelTask : armingCompleted event
      note right of LEDChannelTask
         State changed to READY
      end note

      LEDChannelTask -> ControllerTask : stateChanged event
      ControllerTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen


.. feat:: LED Controller - Channel firing
   :id: FEAT_003
   :tags: actors,user
   :links: REQ_024, REQ_035
   :status: open


   .. needuml::

      ' === Global Style Settings ===
      ' skinparam backgroundColor transparent
      ' skinparam shadowing false
      ' skinparam monochrome false

      ' === Font Styling ===
      skinparam defaultFontName "Consolas, Courier New, monospace"
      skinparam defaultFontSize 14
      
      actor User #E1EAFF
      participant InputTask  #E1EAFF
      participant ControllerTask  #E1EAFF
      participant "LEDChannel[n]Task" as LEDChannelTask   #E1EAFF
      participant ViewTask  #E1EAFF
      participant "Timer[n]" as Timer  #E1EAFF
      participant "DMA/PWM Driver[n]" as DMA  #E1EAFF
      participant "I2C Driver[n]" as I2CDriver #E1EAFF
      participant "Display Driver" as Display  #E1EAFF
      participant Buzzer  #E1EAFF
      
      == Change stage settings, if needed ==

      
      loop#Gold While user using controls changes LEDChannel[n] settings
         User -> InputTask : adjusts LEDChannel[n] settings.
         InputTask -> ControllerTask : update event
         ControllerTask -> LEDChannelTask : update event
         group#Gold While LEDChannel[n] not in FIRE state
            LEDChannelTask -> LEDChannelTask : LEDChannel[n].updateFireSettings()
            LEDChannelTask -> ControllerTask : stateChanged event
            ControllerTask -> ViewTask : renderView event
            ViewTask -> Display : Render Screen
         end
      end

      == Channel fire sequence ==

      
      User -> InputTask : press FIRE button
      InputTask -> ControllerTask : fireRequest event
      group#Gold While LEDChannel[n] in READY state
         ControllerTask -> LEDChannelTask : fireRequest event
         note right of LEDChannelTask
            State changed to FIRE
         end note
      end
      
      
      LEDChannelTask -> ControllerTask : stateChanged event
      ControllerTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen

      LEDChannelTask -> Timer : LEDChannel[n].startTimers()
      LEDChannelTask -> DMA : LEDChannel[n].startWaveform()
      LEDChannelTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen
      loop#Gold While LEDChannel[n].hasTimerRunning() or LEDChannel[n].hasIncompleteWaveform()
         Timer -> LEDChannelTask: tick event / stageUpdate()
         LEDChannelTask -> ControllerTask : stateChanged event
         ControllerTask -> ViewTask : renderView event
         ViewTask -> Display : Render Screen
      end
      
      ... after timer/cycles complete ...

      Timer -> LEDChannelTask : fireCompleted event
      note right of LEDChannelTask
         State changed to READY
      end note

      LEDChannelTask -> ControllerTask : stateChanged event
      ControllerTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen

      == Channel stop sequence ==

      
      User -> InputTask : press STOP button
      InputTask -> ControllerTask : stopRequest event
      group#gold While LEDChannel[n] in READY state
         ControllerTask -> LEDChannelTask : stopRequest event
         note right of LEDChannelTask
            State changed to IDLE
         end note
      end
      LEDChannelTask -> ControllerTask : stateChanged event
      ControllerTask -> ViewTask : renderView event
      ViewTask -> Display : Render Screen


Desktop Application
----------------------------------------------------------------------------------------

Logical View
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Describes functionality — what the system should do.
(Example: modules - UI handling, LED PWM control, Fan management, Settings storage)

.. arch:: Desktop Application - Logical View
   :id: ARCH_002
   :tags: controller, interfaces, ui, hardware
   :links: FEAT_100, REQ_031
   :status: open
   :open_questions: Headless operation lacks definition!


   .. image:: _static/images/diagrams/DesktopApplicationLogicalView.drawio.png
      :align: center
      :alt: Logical View


.. raw:: latex
  
   \newpage



Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Shows use cases or sequences that validate and illustrate the other views.
(Example: sequence diagrams for "user presses power button" or "desktop app changes settings")


.. feat:: Desktop Application - Features
   :id: FEAT_100
   :tags: actors,user
   :status: open


   TBD
