from __future__ import annotations


class Temperature:
    """
    Represents a temperature in Celsius, Fahrenheit, or Kelvin.

    Temperatures can be converted between units and compared
    regardless of their stored unit.
    """

    TOLERANCE = 1e-9
    VALID_UNITS = {"C", "F", "K"}

    @classmethod
    def _validate_unit(cls, unit: str) -> str:
        """
        Validate a temperature unit and return it in uppercase.

        Raises:
            ValueError: If the unit is invalid.
        """

        if not isinstance(unit, str):
            raise ValueError("Unit must be a string")

        unit = unit.upper()

        if unit not in cls.VALID_UNITS:
            raise ValueError("Unit must be C, F, or K")

        return unit

    def __init__(self, value: float, unit: str = "C") -> None:
        """
        Create a Temperature object.

        Raises:
            ValueError: If the unit is invalid or the temperature
            is below absolute zero.
        """

        self._value = float(value)
        self._unit = self._validate_unit(unit)

        if self.to_kelvin() < -self.TOLERANCE:
            raise ValueError("Temperature cannot be below absolute zero")

    @property
    def value(self) -> float:
        """Return the temperature value."""
        return self._value

    @property
    def unit(self) -> str:
        """Return the temperature unit."""
        return self._unit

    def to_celsius(self) -> float:
        """Return the temperature converted to Celsius."""

        if self.unit == "C":
            return self.value

        if self.unit == "K":
            return self.value - 273.15

        return (self.value - 32) * 5 / 9

    def to_fahrenheit(self) -> float:
        """Return the temperature converted to Fahrenheit."""

        if self.unit == "F":
            return self.value

        if self.unit == "C":
            return self.value * 9 / 5 + 32

        return (self.value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """Return the temperature converted to Kelvin."""

        if self.unit == "K":
            return self.value

        if self.unit == "C":
            return self.value + 273.15

        return (self.value - 32) * 5 / 9 + 273.15

    def convert_to(self, target_unit: str) -> "Temperature":
        """
        Return a new Temperature object in the target unit.

        Raises:
            ValueError: If the target unit is invalid.
        """

        target_unit = self._validate_unit(target_unit)

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")

        if target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")

        return Temperature(self.to_kelvin(), "K")

    def __repr__(self) -> str:
        """Return an unambiguous representation."""

        return f"Temperature({self.value!r}, '{self.unit}')"

    def __str__(self) -> str:
        """Return a human-readable temperature string."""

        if self.unit == "K":
            return f"{self.value:.2f} K"

        return f"{self.value:.2f} °{self.unit}"

    def __eq__(self, other: object) -> bool:
        """
        Test equality using Kelvin values and tolerance.
        """

        if not isinstance(other, Temperature):
            return NotImplemented

        return (
            abs(self.to_kelvin() - other.to_kelvin())
            < self.TOLERANCE
        )

    def __ne__(self, other: object) -> bool:
        """
        Test inequality.
        """

        result = self.__eq__(other)

        if result is NotImplemented:
            return NotImplemented

        return not result

    def __lt__(self, other: object) -> bool:
        """
        Test whether this temperature is less than another.
        """

        if not isinstance(other, Temperature):
            return NotImplemented

        return (
            self.to_kelvin()
            < other.to_kelvin() - self.TOLERANCE
        )

    def __le__(self, other: object) -> bool:
        """
        Test whether this temperature is less than or equal.
        """

        if not isinstance(other, Temperature):
            return NotImplemented

        return self < other or self == other

    def __gt__(self, other: object) -> bool:
        """
        Test whether this temperature is greater than another.
        """

        if not isinstance(other, Temperature):
            return NotImplemented

        return other < self

    def __ge__(self, other: object) -> bool:
        """
        Test whether this temperature is greater than or equal.
        """

        if not isinstance(other, Temperature):
            return NotImplemented

        return other < self or self == other