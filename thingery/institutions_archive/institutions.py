# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Institutions Archive Module
	description: >
		Institutions archive package - institutions founded after 1926 (younger than 100 years)
		Loaded from YAML config in _data_/institutions.yaml
	version: 0.1.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*

from enum import Enum
from typing import Optional, List, Dict, Any
import yaml
from pathlib import Path

# Determine base path for data file
_BASE_PATH = Path(__file__).parent / "_data_" / "institutions.yaml"

class InstitutionType(Enum):
    """Institution type enumeration"""
    CENTRAL_BANK = "central_bank"
    GOVERNMENT = "government"
    GOVERNMENT_LAB = "government_lab"
    UNIVERSITY = "university"
    INTERNATIONAL = "international"
    CORPORATION = "corporation"

class Institution:
    """Represents an institution"""
    
    def __init__(self, key: str, data: Dict[str, Any]):
        self.key = key
        self.name = data.get("name", "")
        self.location = data.get("location", "")
        self.founded = data.get("founded", 0)
        self.type = data.get("type", "")
        self.website = data.get("website", "")
        self.focus_areas = data.get("focus_areas", [])
        self.notable_research = data.get("notable_research", [])
    
    def __repr__(self):
        return f"<Institution {self.key}: {self.name} ({self.founded})>"
    
    def __str__(self):
        return f"{self.name} ({self.founded})"
    
    @property
    def is_established(self) -> bool:
        """Check if institution is established (>100 years)"""
        return self.founded <= 1926
    
    @property
    def age(self) -> int:
        """Calculate age of institution"""
        return 2026 - self.founded

def load_institutions() -> Dict[str, Institution]:
    """Load all institutions from YAML"""
    institutions = {}
    
    if not _BASE_PATH.exists():
        return institutions
    
    with open(_BASE_PATH, "r") as f:
        data = yaml.safe_load(f)
    
    if not data or "Institutions" not in data:
        return institutions
    
    for category, items in data["Institutions"].items():
        if isinstance(items, dict):
            for key, value in items.items():
                institutions[key] = Institution(key, value)
    
    return institutions

def get_institution(key: str) -> Optional[Institution]:
    """Get institution by key"""
    return _INSTITUTIONS.get(key)

def get_institutions_by_type(institution_type: str) -> List[Institution]:
    """Get all institutions of a specific type"""
    return [inst for inst in _INSTITUTIONS.values() if inst.type == institution_type]

def get_institutions_by_founded(min_year: int, max_year: Optional[int] = None) -> List[Institution]:
    """Get institutions founded between min_year and max_year"""
    if max_year is None:
        max_year = 2026
    return [inst for inst in _INSTITUTIONS.values() if min_year <= inst.founded <= max_year]

# Load all institutions at module level
_INSTITUTIONS = load_institutions()

# Convenience accessors
all_institutions = list(_INSTITUTIONS.values())

banks = [inst for inst in all_institutions if inst.type == "central_bank"]
government_labs = [inst for inst in all_institutions if inst.type == "government_lab"]
international_orgs = [inst for inst in all_institutions if inst.type == "international"]
corporations = [inst for inst in all_institutions if inst.type == "corporation"]

# Filter: younger than 100 years (founded after 1926)
younger_than_100 = [inst for inst in all_institutions if inst.founded > 1926]
