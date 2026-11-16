import pytest

from temperature import Temperature


REFERENCE_POINTS = [
    (-273.15, -459.67, 0.0),      # absolute zero
    (-40.0, -40.0, 233.15),       # celsius-fahrenheit crossover
    (0.0, 32.0, 273.15),          # freezing point of water
    (37.0, 98.6, 310.15),         # human body temperature
    (100.0, 212.0, 373.15),       # boiling point of water
]


def test_default_unit():
    """Test that Celsius is the default unit."""

    temp = Temperature(25)

    assert temp.unit == "C"


@pytest.mark.parametrize(
    "unit, expected",
    [
        ("c", "C"),
        ("f", "F"),
        ("k", "K"),
    ]
)
def test_case_insensitive_units(unit, expected):
    """Test that units are handled case-insensitively."""

    temp = Temperature(25, unit)

    assert temp.unit == expected


def test_read_only_attributes():
    """Test that value and unit cannot be modified."""

    temp = Temperature(25)

    with pytest.raises(AttributeError):
        temp.value = 50

    with pytest.raises(AttributeError):
        temp.unit = "F"


@pytest.mark.parametrize(
    "value, unit",
    [
        (25, "X"),
        (25, "ABC"),
        (25, ""),
        (25, 5),
    ]
)
def test_invalid_units(value, unit):
    """Test invalid temperature units."""

    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize(
    "value, unit",
    [
        (-273.15, "C"),
        (-459.67, "F"),
        (0, "K"),
    ]
)
def test_absolute_zero_is_allowed(value, unit):
    """Absolute zero should be accepted."""

    Temperature(value, unit)


@pytest.mark.parametrize(
    "value, unit",
    [
        (-273.16, "C"),
        (-500.0, "F"),
        (-1.0, "K"),
    ]
)
def test_below_absolute_zero(value, unit):
    """Temperatures below absolute zero should raise ValueError."""

    with pytest.raises(ValueError):
        Temperature(value, unit)


@pytest.mark.parametrize("c, f, k", REFERENCE_POINTS)
def test_conversions(c, f, k):
    """Test all reference points in all units."""

    temps = [
        Temperature(c, "C"),
        Temperature(f, "F"),
        Temperature(k, "K"),
    ]

    for temp in temps:
        assert temp.to_celsius() == pytest.approx(c)
        assert temp.to_fahrenheit() == pytest.approx(f)
        assert temp.to_kelvin() == pytest.approx(k)


def test_convert_to_returns_new_temperature():
    """Test convert_to conversion."""

    temp = Temperature(0, "C").convert_to("f")

    assert temp.unit == "F"
    assert temp.value == pytest.approx(32)


def test_convert_to_invalid_unit():
    """Test invalid target unit."""

    with pytest.raises(ValueError):
        Temperature(0, "C").convert_to("X")


@pytest.mark.parametrize(
    "value",
    [
        25,
        -40,
        98.6,
        0.001,
    ]
)
def test_round_trip_conversion(value):
    """C -> F -> K -> C should recover original temperature."""

    original = Temperature(value, "C")

    result = (
        original
        .convert_to("F")
        .convert_to("K")
        .convert_to("C")
    )

    assert result == original


def test_cross_unit_equality():
    """Test equality across units."""

    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(100, "C") == Temperature(373.15, "K")


def test_cross_unit_ordering():
    """Test all comparison operators."""

    assert Temperature(0, "C") < Temperature(100, "C")

    assert (
        Temperature(32, "F")
        <= Temperature(0, "C")
    )

    assert (
        Temperature(373.15, "K")
        > Temperature(0, "C")
    )

    assert (
        Temperature(212, "F")
        >= Temperature(373.15, "K")
    )

    assert (
        Temperature(0, "C")
        != Temperature(0, "F")
    )


def test_compare_with_non_temperature():
    """Test comparisons with non-Temperature objects."""

    assert Temperature(0, "C").__eq__(0) is NotImplemented

    assert Temperature(0, "C") != 0

    with pytest.raises(TypeError):
        Temperature(0, "C") < 0


def test_string_formatting():
    """Test __str__ formatting."""

    assert str(Temperature(25, "C")) == "25.00 °C"
    assert str(Temperature(300, "K")) == "300.00 K"


def test_string_rounding():
    """Test rounding in __str__."""

    assert str(Temperature(36.666, "C")) == "36.67 °C"


def test_repr_formatting():
    """Test __repr__ formatting."""

    assert (
        repr(Temperature(25, "C"))
        == "Temperature(25.0, 'C')"
    )
