"""
Controller module for a dummy 4-channel LED controller.

This example is used only to demonstrate Sphinx autodoc features.
"""

class LEDController:
    """
    Dummy implementation of a 4-channel LED controller.

    Parameters
    ----------
    channels : int
        Number of available channels (default: 4).
    """

    def __init__(self, channels: int = 4):
        if channels <= 0:
            raise ValueError("Number of channels must be positive.")
        self.channels = channels
        self.power_levels = [0] * channels

    def set_power(self, channel: int, power: int):
        """
        Set power level for a channel.

        Parameters
        ----------
        channel : int
            Channel index (0-based)
        power : int
            Power level from 0 to 100

        Raises
        ------
        ValueError
            If channel or power level is invalid.
        """
        if not (0 <= channel < self.channels):
            raise ValueError("Invalid channel index.")
        if not (0 <= power <= 100):
            raise ValueError("Power must be between 0 and 100.")

        self.power_levels[channel] = power

    def get_power(self, channel: int) -> int:
        """Return the current power level of a channel."""
        if not (0 <= channel < self.channels):
            raise ValueError("Invalid channel index.")
        return self.power_levels[channel]
