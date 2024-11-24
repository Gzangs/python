class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize with status off, mute off, channel at minimum, and volume at minimum
        """
        self.__status: bool = False
        self.__mute: bool = False
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME

    def power(self) -> None:
        """
        If status is on, change power to opposite state
        """
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        If status is on, change mute to opposite state
        """
        if self.__status == True:
            if self.__mute == True:
                self.__mute = False
            else:
                self.__mute = True

    def channel_up(self) -> None:
        """
        If status is on, increase channel by 1 and wrap around if at maximum value
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1

    def channel_down(self) -> None:
        """
        If status is on, decrease channel by 1 and wrap around if at minimum value
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1

    def volume_up(self) -> None:
        """
        If status is on, unmute and increase by 1 while not going above minimum volume
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__mute = False
                self.__volume = self.__volume + 1

    def volume_down(self) -> None:
        """
        If status is on, unmute and decrease by 1 while not going below minimum volume
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__mute = False
                self.__volume = self.__volume - 1

    def __str__(self) -> str:
        """
        str: current status, channel, and volume.
        If muted volume = 0
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0" if self.__mute else f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

