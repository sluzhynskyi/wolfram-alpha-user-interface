class MyStr:
    def __init__(self, value=""):
        """
        Initializing new data Structure
        :param value: str
        """
        self._value = value

    def __str__(self):
        return self._value
