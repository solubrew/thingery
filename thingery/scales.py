# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Scales
	description: >
		Complete measurement scales database - temperature, pressure, length, mass, electrical, radiation
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import Optional


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================TEMPERATURE SCALES======================================================================||
# ====================================================================================================================||


@dataclass
class Kelvin:
    name: str = "Kelvin"
    symbol: str = "K"
    category: str = "temperature"
    absolute_zero: float = 0.0  # K
    conversion_to_celsius: float = -273.15
    conversion_to_fahrenheit: float = -459.67
    conversion_to_rankine: float = 0.0


@dataclass
class Celsius:
    name: str = "Celsius"
    symbol: str = "°C"
    category: str = "temperature"
    absolute_zero: float = -273.15  # °C
    conversion_to_kelvin: float = 273.15
    conversion_to_fahrenheit: float = 32.0
    conversion_to_rankine: float = 491.67


@dataclass
class Fahrenheit:
    name: str = "Fahrenheit"
    symbol: str = "°F"
    category: str = "temperature"
    absolute_zero: float = -459.67  # °F
    conversion_to_kelvin: float = 255.37
    conversion_to_celsius: float = -17.78
    conversion_to_rankine: float = 0.0


@dataclass
class Rankine:
    name: str = "Rankine"
    symbol: str = "°R"
    category: str = "temperature"
    absolute_zero: float = 0.0  # °R
    conversion_to_kelvin: float = 0.555556
    conversion_to_celsius: float = -273.15
    conversion_to_fahrenheit: float = -459.67


# ===========================PRESSURE SCALES=========================================================================||
# ====================================================================================================================||


@dataclass
class Pascal:
    name: str = "Pascal"
    symbol: str = "Pa"
    category: str = "pressure"
    base_unit: str = "Pa"
    conversion_to_pascal: float = 1.0
    conversion_to_atmosphere: float = 9.8692e-6
    conversion_to_bar: float = 1.0e-5
    conversion_to_psi: float = 0.000145


@dataclass
class Atmosphere:
    name: str = "Atmosphere"
    symbol: str = "atm"
    category: str = "pressure"
    base_unit: str = "Pa"
    conversion_to_pascal: float = 101325.0
    conversion_to_bar: float = 1.01325
    conversion_to_psi: float = 14.696
    conversion_to_torr: float = 760.0


@dataclass
class Bar:
    name: str = "Bar"
    symbol: str = "bar"
    category: str = "pressure"
    base_unit: str = "Pa"
    conversion_to_pascal: float = 100000.0
    conversion_to_atmosphere: float = 0.986923
    conversion_to_psi: float = 14.5038
    conversion_to_torr: float = 750.062


@dataclass
class PSI:
    name: str = "Pounds per Square Inch"
    symbol: str = "psi"
    category: str = "pressure"
    base_unit: str = "Pa"
    conversion_to_pascal: float = 6894.76
    conversion_to_atmosphere: float = 0.068046
    conversion_to_bar: float = 0.0689476
    conversion_to_torr: float = 51.7149


@dataclass
class Torr:
    name: str = "Torr"
    symbol: str = "Torr"
    category: str = "pressure"
    base_unit: str = "Pa"
    conversion_to_pascal: float = 133.322
    conversion_to_atmosphere: float = 0.00131579
    conversion_to_bar: float = 0.00133322
    conversion_to_psi: float = 0.0193368


# ===========================LENGTH SCALES==========================================================================||
# ====================================================================================================================||


@dataclass
class Meter:
    name: str = "Meter"
    symbol: str = "m"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_kilometer: float = 0.001
    conversion_to_centimeter: float = 100.0
    conversion_to_millimeter: float = 1000.0
    conversion_to_mile: float = 0.000621371
    conversion_to_foot: float = 3.28084
    conversion_to_inch: float = 39.3701


@dataclass
class Kilometer:
    name: str = "Kilometer"
    symbol: str = "km"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 1000.0
    conversion_to_centimeter: float = 100000.0
    conversion_to_mile: float = 0.621371
    conversion_to_foot: float = 3280.84


@dataclass
class Centimeter:
    name: str = "Centimeter"
    symbol: str = "cm"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 0.01
    conversion_to_millimeter: float = 10.0
    conversion_to_inch: float = 0.393701


@dataclass
class Millimeter:
    name: str = "Millimeter"
    symbol: str = "mm"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 0.001
    conversion_to_centimeter: float = 0.1
    conversion_to_inch: float = 0.0393701


@dataclass
class Mile:
    name: str = "Mile"
    symbol: str = "mi"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 1609.34
    conversion_to_kilometer: float = 1.60934
    conversion_to_foot: float = 5280.0
    conversion_to_yard: float = 1760.0


@dataclass
class Foot:
    name: str = "Foot"
    symbol: str = "ft"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 0.3048
    conversion_to_inch: float = 12.0
    conversion_to_centimeter: float = 30.48
    conversion_to_yard: float = 0.333333


@dataclass
class Inch:
    name: str = "Inch"
    symbol: str = "in"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 0.0254
    conversion_to_centimeter: float = 2.54
    conversion_to_millimeter: float = 25.4


@dataclass
class Yard:
    name: str = "Yard"
    symbol: str = "yd"
    category: str = "length"
    base_unit: str = "m"
    conversion_to_meter: float = 0.9144
    conversion_to_foot: float = 3.0
    conversion_to_inch: float = 36.0


# ===========================MASS SCALES=============================================================================||
# ====================================================================================================================||


@dataclass
class Kilogram:
    name: str = "Kilogram"
    symbol: str = "kg"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_gram: float = 1000.0
    conversion_to_milligram: float = 1.0e6
    conversion_to_pound: float = 2.20462
    conversion_to_ounce: float = 35.274
    conversion_to_ton: float = 0.00110231


@dataclass
class Gram:
    name: str = "Gram"
    symbol: str = "g"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_kilogram: float = 0.001
    conversion_to_milligram: float = 1000.0
    conversion_to_ounce: float = 0.035274
    conversion_to_grain: float = 15.4324


@dataclass
class Milligram:
    name: str = "Milligram"
    symbol: str = "mg"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_kilogram: float = 1.0e-6
    conversion_to_gram: float = 0.001
    conversion_to_microgram: float = 1000.0


@dataclass
class Pound:
    name: str = "Pound"
    symbol: str = "lb"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_kilogram: float = 0.453592
    conversion_to_gram: float = 453.592
    conversion_to_ounce: float = 16.0


@dataclass
class Ounce:
    name: str = "Ounce"
    symbol: str = "oz"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_kilogram: float = 0.0283495
    conversion_to_gram: float = 28.3495
    conversion_to_pound: float = 0.0625


@dataclass
class Ton:
    name: str = "Metric Ton"
    symbol: str = "t"
    category: str = "mass"
    base_unit: str = "kg"
    conversion_to_kilogram: float = 1000.0
    conversion_to_pound: float = 2204.62
    conversion_to_us_ton: float = 1.10231


# ===========================ELECTRICAL SCALES========================================================================||
# ====================================================================================================================||


@dataclass
class Ampere:
    name: str = "Ampere"
    symbol: str = "A"
    category: str = "electrical"
    base_unit: str = "A"
    conversion_to_milliampere: float = 1000.0
    conversion_to_microampere: float = 1.0e6


@dataclass
class Volt:
    name: str = "Volt"
    symbol: str = "V"
    category: str = "electrical"
    base_unit: str = "V"
    conversion_to_millivolt: float = 1000.0
    conversion_to_microvolt: float = 1.0e6
    conversion_to_kilovolt: float = 0.001


@dataclass
class Ohm:
    name: str = "Ohm"
    symbol: str = "Ω"
    category: str = "electrical"
    base_unit: str = "Ω"
    conversion_to_milliohm: float = 1000.0
    conversion_to_kilohm: float = 0.001
    conversion_to_megohm: float = 1.0e-6


@dataclass
class Watt:
    name: str = "Watt"
    symbol: str = "W"
    category: str = "electrical"
    base_unit: str = "W"
    conversion_to_milliwatt: float = 1000.0
    conversion_to_kilowatt: float = 0.001
    conversion_to_megawatt: float = 1.0e-6


@dataclass
class Coulomb:
    name: str = "Coulomb"
    symbol: str = "C"
    category: str = "electrical"
    base_unit: str = "C"
    conversion_to_millicoulomb: float = 1000.0
    conversion_to_microcoulomb: float = 1.0e6


@dataclass
class Farad:
    name: str = "Farad"
    symbol: str = "F"
    category: str = "electrical"
    base_unit: str = "F"
    conversion_to_microfarad: float = 1.0e6
    conversion_to_nanofarad: float = 1.0e9
    conversion_to_picofarad: float = 1.0e12


@dataclass
class Henry:
    name: str = "Henry"
    symbol: str = "H"
    category: str = "electrical"
    base_unit: str = "H"
    conversion_to_millihenry: float = 1000.0
    conversion_to_microhenry: float = 1.0e6


@dataclass
class Siemens:
    name: str = "Siemens"
    symbol: str = "S"
    category: str = "electrical"
    base_unit: str = "S"
    conversion_to_millisiemens: float = 1000.0
    conversion_to_microsiemens: float = 1.0e6


@dataclass
class Tesla:
    name: str = "Tesla"
    symbol: str = "T"
    category: str = "electrical"
    base_unit: str = "T"
    conversion_to_gauss: float = 10000.0
    conversion_to_millitesla: float = 1000.0


# ===========================RADIATION SCALES========================================================================||
# ====================================================================================================================||


@dataclass
class Becquerel:
    name: str = "Becquerel"
    symbol: str = "Bq"
    category: str = "radiation"
    base_unit: str = "Bq"
    conversion_to_kilobecquerel: float = 0.001
    conversion_to_megabecquerel: float = 1.0e-6
    conversion_to_curie: float = 2.7027e-11


@dataclass
class GrayRadiation:
    name: str = "Gray"
    symbol: str = "Gy"
    category: str = "radiation"
    base_unit: str = "Gy"
    conversion_to_milligray: float = 1000.0
    conversion_to_radiation_absorbed_dose: float = 100.0


@dataclass
class Sievert:
    name: str = "Sievert"
    symbol: str = "Sv"
    category: str = "radiation"
    base_unit: str = "Sv"
    conversion_to_millisievert: float = 1000.0
    conversion_to_microsievert: float = 1.0e6
    conversion_to_rem: float = 100.0


# ===========================TIME SCALES=============================================================================||
# ====================================================================================================================||


@dataclass
class Second:
    name: str = "Second"
    symbol: str = "s"
    category: str = "time"
    base_unit: str = "s"
    conversion_to_millisecond: float = 1000.0
    conversion_to_microsecond: float = 1.0e6
    conversion_to_minute: float = 0.0166667
    conversion_to_hour: float = 0.000277778
    conversion_to_day: float = 1.1574e-5


@dataclass
class Minute:
    name: str = "Minute"
    symbol: str = "min"
    category: str = "time"
    base_unit: str = "s"
    conversion_to_second: float = 60.0
    conversion_to_hour: float = 0.0166667
    conversion_to_day: float = 0.000694444


@dataclass
class Hour:
    name: str = "Hour"
    symbol: str = "h"
    category: str = "time"
    base_unit: str = "s"
    conversion_to_second: float = 3600.0
    conversion_to_minute: float = 60.0
    conversion_to_day: float = 0.0416667


@dataclass
class Day:
    name: str = "Day"
    symbol: str = "d"
    category: str = "time"
    base_unit: str = "s"
    conversion_to_second: float = 86400.0
    conversion_to_hour: float = 24.0
    conversion_to_week: float = 0.142857
    conversion_to_year: float = 0.00273973


# ===========================ENERGY SCALES===========================================================================||
# ====================================================================================================================||


@dataclass
class Joule:
    name: str = "Joule"
    symbol: str = "J"
    category: str = "energy"
    base_unit: str = "J"
    conversion_to_kilojoule: float = 0.001
    conversion_to_calorie: float = 0.239006
    conversion_to_kilocalorie: float = 0.000239006
    conversion_to_electronvolt: float = 6.242e18
    conversion_to_watt_hour: float = 2.7778e-7


@dataclass
class Calorie:
    name: str = "Calorie"
    symbol: str = "cal"
    category: str = "energy"
    base_unit: str = "J"
    conversion_to_joule: float = 4.184
    conversion_to_kilocalorie: float = 0.001


@dataclass
class ElectronVolt:
    name: str = "Electron Volt"
    symbol: str = "eV"
    category: str = "energy"
    base_unit: str = "J"
    conversion_to_joule: float = 1.6022e-19
    conversion_to_kiloelectronvolt: float = 0.001
    conversion_to_megaelectronvolt: float = 1.0e-6


@dataclass
class BTU:
    name: str = "British Thermal Unit"
    symbol: str = "BTU"
    category: str = "energy"
    base_unit: str = "J"
    conversion_to_joule: float = 1055.06
    conversion_to_kilowatt_hour: float = 0.000293071


# ===========================FREQUENCY SCALES========================================================================||
# ====================================================================================================================||


@dataclass
class Hertz:
    name: str = "Hertz"
    symbol: str = "Hz"
    category: str = "frequency"
    base_unit: str = "Hz"
    conversion_to_kilohertz: float = 0.001
    conversion_to_megahertz: float = 1.0e-6
    conversion_to_gigahertz: float = 1.0e-9


@dataclass
class Kilohertz:
    name: str = "Kilohertz"
    symbol: str = "kHz"
    category: str = "frequency"
    base_unit: str = "Hz"
    conversion_to_hertz: float = 1000.0
    conversion_to_megahertz: float = 0.001


@dataclass
class Megahertz:
    name: str = "Megahertz"
    symbol: str = "MHz"
    category: str = "frequency"
    base_unit: str = "Hz"
    conversion_to_hertz: float = 1.0e6
    conversion_to_gigahertz: float = 0.001


# ===========================DATA STORAGE SCALES======================================================================||
# ====================================================================================================================||


@dataclass
class Byte:
    name: str = "Byte"
    symbol: str = "B"
    category: str = "data"
    base_unit: str = "B"
    conversion_to_bit: float = 8.0
    conversion_to_kilobyte: float = 0.001
    conversion_to_megabyte: float = 1.0e-6


@dataclass
class Kilobyte:
    name: str = "Kilobyte"
    symbol: str = "KB"
    category: str = "data"
    base_unit: str = "B"
    conversion_to_byte: float = 1024.0
    conversion_to_megabyte: float = 0.0009765625
    conversion_to_gigabyte: float = 9.5367e-7


@dataclass
class Megabyte:
    name: str = "Megabyte"
    symbol: str = "MB"
    category: str = "data"
    base_unit: str = "B"
    conversion_to_byte: float = 1.048576e6
    conversion_to_kilobyte: float = 1024.0
    conversion_to_gigabyte: float = 0.0009765625


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Temperature
    'Kelvin', 'Celsius', 'Fahrenheit', 'Rankine',
    # Pressure
    'Pascal', 'Atmosphere', 'Bar', 'PSI', 'Torr',
    # Length
    'Meter', 'Kilometer', 'Centimeter', 'Millimeter', 'Mile', 'Foot', 'Inch', 'Yard',
    # Mass
    'Kilogram', 'Gram', 'Milligram', 'Pound', 'Ounce', 'Ton',
    # Electrical
    'Ampere', 'Volt', 'Ohm', 'Watt', 'Coulomb', 'Farad', 'Henry', 'Siemens', 'Tesla',
    # Radiation
    'Becquerel', 'GrayRadiation', 'Sievert',
    # Time
    'Second', 'Minute', 'Hour', 'Day',
    # Energy
    'Joule', 'Calorie', 'ElectronVolt', 'BTU',
    # Frequency
    'Hertz', 'Kilohertz', 'Megahertz',
    # Data
    'Byte', 'Kilobyte', 'Megabyte',
]
