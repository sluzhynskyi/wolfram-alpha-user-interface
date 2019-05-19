class MyStr:
    def __init__(self, value=""):
        """
        Initializing new data Structure
        :param value: str
        """
        self._value = value

    def __add__(self, other):
        """
        Function to add two texts
        :param other: MyStr
        :return: str
        """
        return MyStr(self._value + other._value)

    def __str__(self):
        """
        value of MyStr
        :return: str
        """
        return self._value
