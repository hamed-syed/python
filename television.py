class Television:
    """A simple television model with power, mute, channel, and volume controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the TV to powered off, unmuted, at the minimum channel and volume."""
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the TV's power state between on and off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the TV's mute state if the TV is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel by 1, wrapping to MIN_CHANNEL after MAX_CHANNEL."""
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Decrease the channel by 1, wrapping to MAX_CHANNEL before MIN_CHANNEL."""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume by 1, up to MAX_VOLUME. Unmutes if currently muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by 1, down to MIN_VOLUME. Unmutes if currently muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the current power, channel, and volume settings as a string."""
        power_status: str = "True" if self.__status else "False"
        return f"Power = {power_status}, Channel = {self.__channel}, Volume = {self.__volume}"