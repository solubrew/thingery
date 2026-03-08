# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Institutions
	description: >
		Curated institutions database - only government institutions, 
		established banks, and prestigious universities/labs (founded <= 1926)
	version: 0.0.1.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from thingery.models import Institution, InstitutionType
from thingery._loader import load_yaml


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================YAML LOADER==========================================================================||
# ====================================================================================================================||


def _get_type_from_category(category: str) -> str:
    """Map YAML category to InstitutionType enum value."""
    mapping = {
        'BANKS': InstitutionType.BANK.value,
        'GOVERNMENT': InstitutionType.GOVERNMENT.value,
        'INTERNATIONAL': InstitutionType.INTERNATIONAL.value,
        'UNIVERSITIES': InstitutionType.UNIVERSITY.value,
        'CORPORATIONS': InstitutionType.COMPANY.value,
    }
    return mapping.get(category, InstitutionType.INTERNATIONAL.value)


def load_institutions() -> List[Institution]:
    """
    Load all institutions from YAML config.
    
    Returns:
        List of Institution dataclass instances
    """
    data = load_yaml('institutions.yaml')
    institutions = []
    
    for category, items in data.get('Institutions', {}).items():
        if not isinstance(items, dict):
            continue
            
        inst_type = _get_type_from_category(category)
        
        for key, values in items.items():
            if isinstance(values, dict):
                institutions.append(Institution(
                    name=values.get('name', ''),
                    institution_type=inst_type,
                    location=values.get('location', ''),
                    founded=values.get('founded'),
                    website=values.get('website'),
                    focus_areas=values.get('focus_areas', []),
                    notable_research=values.get('notable_research', [])
                ))
    
    return institutions


def get_institutions_by_type(institution_type: str) -> List[Institution]:
    """Get institutions filtered by type."""
    all_inst = load_institutions()
    return [i for i in all_inst if i.institution_type == institution_type]


def get_institutions_by_founded(min_year: int = 1926) -> List[Institution]:
    """Get institutions founded before a given year (default: >100 years old = before 1926)."""
    all_inst = load_institutions()
    return [i for i in all_inst if i.founded and i.founded <= min_year]


def get_institution(name: str) -> Optional[Institution]:
    """Get a specific institution by name."""
    all_inst = load_institutions()
    for inst in all_inst:
        if inst.name.lower() == name.lower():
            return inst
    return None


# ===========================CONVENIENCE ACCESSORS===============================================================||
# ====================================================================================================================||


# All institutions
all_institutions: List[Institution] = load_institutions()

# By category
banks = get_institutions_by_type(InstitutionType.BANK.value)
government = get_institutions_by_type(InstitutionType.GOVERNMENT.value)
universities = get_institutions_by_type(InstitutionType.UNIVERSITY.value)
international_orgs = get_institutions_by_type(InstitutionType.INTERNATIONAL.value)
corporations = get_institutions_by_type(InstitutionType.COMPANY.value)

# Filtered: founded <= 1926 (>100 years old)
established = get_institutions_by_founded(1926)


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    'Institution', 'InstitutionType',
    'load_institutions', 'get_institutions_by_type', 'get_institutions_by_founded', 'get_institution',
    'all_institutions', 'banks', 'government', 'universities', 'international_orgs', 'corporations', 'established',
]
