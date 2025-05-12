Implementation
========================================================================================

Work Breakdown Structure (WBS)
----------------------------------------------------------------------------------------
1. **Hardware**

- Requirements analysis
- Power circuit design
- MCU and peripheral selection
- Schematic and PCB design
- Prototype assembly
- Functional and thermal validation (LED Power Module, Fan Power Module)

2. Firmware

- Bootloader & debugging interface
- Channel control interface
- EEPROM communication
- Display UI logic
- Timer and waveform generation
- Arming/firing logic
- Audio feedback
- Serial protocol implementation
- Headless mode implementation

3. Desktop App

- Requirements finalization
- Tech stack selection
- UI development (Client provides designs)
- Serial communication layer
- EEPROM interface
- Feature implementation (Color, current, flashing)
- Compatibility testing (Windows 8+)

4. Documentation & Training

- Firmware architecture docs
- Low/high-level operation training guide


Preliminary Effort Estimates
----------------------------------------------------------------------------------------

+--------------------------+--------------+--------------------------------------------------------------------------------+
| Component                | Time (Weeks) | Notes                                                                          |
+--------------------------+--------------+--------------------------------------------------------------------------------+
| Hardware Design & PCB    |  4           |  Includes review iterations                                                    |
+--------------------------+--------------+--------------------------------------------------------------------------------+
| Firmware Development     |  8           |  In parallel with hardware                                                     |
+--------------------------+--------------+--------------------------------------------------------------------------------+
| Desktop Application      |  4           |  With mock hardware                                                            |
+--------------------------+--------------+--------------------------------------------------------------------------------+
| Integration & Validation |  2           |  With provided LED panels                                                      |
+--------------------------+--------------+--------------------------------------------------------------------------------+
| Documentation & Handover |  2           |  Including training                                                            |
+--------------------------+--------------+--------------------------------------------------------------------------------+
|                          |  20          |  800 Hours                                                                     |
+--------------------------+--------------+--------------------------------------------------------------------------------+

**Total estimated duration**: ~12-14 weeks
(Parallel streams reduce total calendar time)


Preliminary Bill of Materials
----------------------------------------------------------------------------------------

+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| Price             | Specs                                        | Notes                                                                          |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 56 Eur            | MCU + Display + 2xUSB + 4xPWM + 4xI2C        | `STM P/N 32F746GDISCOVERY Discovery kit <https://eu.mouser.com/ProductDetail/  |
|                   |                                              | STMicroelectronics/STM32F746G-DISCO?qs=KuGPmAKtFKV4xEByQ7IKqA%3D%3D>`_         |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 240Eur (4x60Eur)  | LED Power Supply, Dimming PWM, 3.45A at 54V  | `MEAN WELL P/N HLG-185H-54B <https://www.digikey.lt/en/products/               |
|                   |                                              | detail/mean-well-usa-inc/HLG-185H-54B/7703964?s=N4IgjCBcpmBMAGKo               |
|                   |                                              | DGUBmBDANgZwKYA0IA9lANrgDsAzAKx0BsIxYtjNcL1ALAJyMIrKjyq0QAXWIAHA               |
|                   |                                              | C5QQAZVkAnAJYA7AOYgAvqxqM6yEGkhY8RUhRA0wNAByMuUkHIXL12vcThgHVCZmF              |
|                   |                                              | gTEZJCU-owABADqkjLykCAAqhpqsgDy6ACy%2BJi4AK4q%2BHq6ukA>`_                      |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 16 Eur            | Fan Power Module is 5A, 12VDC                | `MEAN WELL P/N IRM-60-12 <https://www.digikey.lt/en/products/detail/           |
|                   |                                              | mean-well-usa-inc/IRM-60-12/7704688>`_                                         |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 7.5 Eur           | Tabletop Controller Power Module 2A, 5VDC    | `MEAN WELL P/N IRM-10-5 <https://www.digikey.lt/en/products/detail/            |
|                   |                                              | mean-well-usa-inc/IRM-10-5/7704657>`_                                          |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 50 Eur            | Custom Arduino Shield PCB with assembly      | (power modules, circuit protection and level shifter)                          |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| TDB Eur           | Encoder Knob (alt. Display touch feature)    | `GRAYHILL TOUCH ENCODER <https://grayhill.com/touch-encoder/>`_                |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+
| 369.5 Eur         |                                              |                                                                                |
+-------------------+----------------------------------------------+--------------------------------------------------------------------------------+


Key Milestones & Dependencies
----------------------------------------------------------------------------------------

+---------------------------------+-----------------------------------+
| Milestone                       | Dependency                        |
+---------------------------------+-----------------------------------+
| Hardware Schematic Finalized    | Completion of requirements review |
+---------------------------------+-----------------------------------+
| Firmware Prototype on Dev Board |  MCU selection                    |
+---------------------------------+-----------------------------------+
| Tabletop LED Controller MVP     |  MCU, LED Power Module selection  |
+---------------------------------+-----------------------------------+
| Desktop App MVP                 |  Protocol documentation           |
+---------------------------------+-----------------------------------+
| First Integrated Test (Bench)   |  Assembled prototype              |
+---------------------------------+-----------------------------------+
| Final Feature Freeze            |  Functional validation            |
+---------------------------------+-----------------------------------+
| Documentation Delivered         |  Final firmware build             |
+---------------------------------+-----------------------------------+


Risks & Mitigation
----------------------------------------------------------------------------------------

+---------------------------------------+--------------------------------------------------+
| Risk                                  | Mitigation Strategy                              |
+---------------------------------------+--------------------------------------------------+
| LED Power Module specifications       | Early access and clarification loop with Client  |
+---------------------------------------+--------------------------------------------------+
| I2C communication errors              | Read EEPROM several times to confirm             |
+---------------------------------------+--------------------------------------------------+
| USB enumeration errors                | Logging and diagnostics built into firmware      |
+---------------------------------------+--------------------------------------------------+
| UART/USB communication errors         |  Logging and diagnostics built into firmware     |
+---------------------------------------+--------------------------------------------------+
| High power design causing overheating | Conservative thermal design + fan support        |
+---------------------------------------+--------------------------------------------------+
| Incomplete protocol documentation     |  Early access and clarification loop with Client |
+---------------------------------------+--------------------------------------------------+
| Hardware/firmware iteration delays    |  Rapid prototyping + emulation using dev kits    |
+---------------------------------------+--------------------------------------------------+
