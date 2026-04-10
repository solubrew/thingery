# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name:
	description: >
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
# ======================================Standard Library Modules======================================================||
from os.path import abspath, dirname, join
import datetime as dt
# ======================================3rd Party Library Modules=====================================================||

# ======================================Solutions Brewer Library Modules==============================================||
from condor import condor
from ogma.logma import Logma

# ====================================================================================================================||
here = join(dirname(__file__), '')  # ||
log = True
logma = Logma(__name__)

# ====================================================================================================================||
pxcfg = join(here, '_data_', 'numerals.yaml')


def calcArabicNumerals(input_):
    """"""
    # Roman numeral to Arabic numeral mapping
    numerals = condor.Instruct(pxcfg).select("extended_roman_numerals").dikt
    numerals = dict(zip(numerals.values(), numerals.keys()))
    arabic_value = 0
    prev_value = 0
    # Loop through the Roman numerals in reverse order
    for char in reversed(input_):
        current_value = int(numerals[char])
        if current_value < prev_value:
            arabic_value -= current_value
        else:
            arabic_value += current_value
        prev_value = current_value
    return arabic_value


def calcExtendedRomanNumerals(input_):
    """Calculate the Extended Roman Numeral Symbol from Arabic Numeral"""
    numerals = condor.Instruct(pxcfg).select("extended_roman_numerals").dikt
    logma.info(f"Numerals: {numerals}")
    keys = [int(x) for x in numerals.keys()]
    keys.sort()
    ern = ""
    while input_ != 0:
        for val in reversed(keys):
            calc = input_ - val
            if calc < 0:
                continue
            input_ = calc
            ern += numerals[str(val)]
            break
    return ern

# ====================================================================================================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
