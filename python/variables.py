class Variable:
    def __init__(self, value):
        self.type = type(value)
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if type(new_value) is not self.type:
            raise TypeError(
                f"Variable ist vom Typ {self.type.__name__}, "
                f"nicht {type(new_value).__name__}"
            )

        self._value = new_value

variablen = {}