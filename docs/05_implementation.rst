Implementation
========================================================================================

Actual code, hardware, configuration — realizes the architecture.

- 56Eur, MCU + Display + 2xUSB + 4xPWM + 4xI2C. `STM P/N 32F746GDISCOVERY Discovery kit <https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F746G-DISCO?qs=KuGPmAKtFKV4xEByQ7IKqA%3D%3D>`_

- 240Eur (4x60Eur), LED Power Supply, Dimming Analog, PWM, 3.45A at 54V (expected spec 3.33A at 56V). `MEAN WELL P/N HLG-185H-54B <https://www.digikey.lt/en/products/detail/mean-well-usa-inc/HLG-185H-54B/7703964?s=N4IgjCBcpmBMAGKoDGUBmBDANgZwKYA0IA9lANrgDsAzAKx0BsIxYtjNcL1ALAJyMIrKjyq0QAXWIAHAC5QQAZVkAnAJYA7AOYgAvqxqM6yEGkhY8RUhRA0wNAByMuUkHIXL12vcThgHVCZmFgTEZJCU-owABADqkjLykCAAqhpqsgDy6ACy%2BJi4AK4q%2BHq6ukA>`_

- 16Eur, Fan Power Module is 5A, 12VDC, 60W (most popular for fans, assumption is to consume ~ 10% LED power). `MEAN WELL P/N IRM-60-12 <https://www.digikey.lt/en/products/detail/mean-well-usa-inc/IRM-60-12/7704688>`_

- 7.5Eur, Tabletop Controller Power Module 2A, 5VDC. `MEAN WELL P/N IRM-10-5 <https://www.digikey.lt/en/products/detail/mean-well-usa-inc/IRM-10-5/7704657>`_

- ~50Eur, Custom Arduino Shield PCB with assembled components (AC/DC power modules, circuit protection and level shifter).

