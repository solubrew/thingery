# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery YAML Loader
	description: >
		Centralized YAML data loader for Thingery datasets
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from __future__ import annotations
import yaml
from dataclasses import dataclass, field
from os.path import abspath, dirname, join
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, TypeVar
from functools import lru_cache


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# Get the thingery package directory
THINGERY_DIR = Path(dirname(__file__))
DATA_DIR = THINGERY_DIR / "_data_"


T = TypeVar('T')


@dataclass
class ThingeryLoader:
    """Centralized YAML data loader for Thingery datasets."""
    
    _cache: Dict[str, Any] = field(default_factory=dict, repr=False)
    
    def load(self, filename: str, use_cache: bool = True) -> Dict[str, Any]:
        """
        Load a YAML file from the _data_ directory.
        
        Args:
            filename: Name of the YAML file (e.g., 'scales.yaml')
            use_cache: Whether to cache the loaded data
            
        Returns:
            Parsed YAML data as dictionary
        """
        cache_key = filename
        
        if use_cache and cache_key in self._cache:
            return self._cache[cache_key]
        
        filepath = DATA_DIR / filename
        
        if not filepath.exists():
            raise FileNotFoundError(f"YAML file not found: {filepath}")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if use_cache:
            self._cache[cache_key] = data
        
        return data
    
    def load_category(self, filename: str, category: str) -> List[Dict[str, Any]]:
        """
        Load a specific category from a YAML file.
        
        Args:
            filename: Name of the YAML file
            category: Top-level key to extract
            
        Returns:
            List of items in that category
        """
        data = self.load(filename)
        return data.get(category, [])
    
    def clear_cache(self) -> None:
        """Clear the internal cache."""
        self._cache.clear()
    
    def reload(self, filename: str) -> Dict[str, Any]:
        """Reload a YAML file, bypassing cache."""
        if filename in self._cache:
            del self._cache[filename]
        return self.load(filename, use_cache=True)


# Global singleton instance
_loader: Optional[ThingeryLoader] = None


def get_loader() -> ThingeryLoader:
    """Get the global ThingeryLoader instance."""
    global _loader
    if _loader is None:
        _loader = ThingeryLoader()
    return _loader


def load_yaml(filename: str, use_cache: bool = True) -> Dict[str, Any]:
    """Convenience function to load YAML data."""
    return get_loader().load(filename, use_cache)


def load_category(filename: str, category: str) -> List[Dict[str, Any]]:
    """Convenience function to load a category from YAML."""
    return get_loader().load_category(filename, category)


# ============================================================================
# Dataclass Factory - Create dataclasses from YAML data
# ============================================================================


def create_dataclass_from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
    """
    Create a dataclass instance from a dictionary.
    
    Args:
        cls: Dataclass type to instantiate
        data: Dictionary with field values
        
    Returns:
        Instance of the dataclass
    """
    # Filter to only include fields that exist in the dataclass
    import inspect
    fields = {f.name for f in getattr(cls, '__dataclass_fields__', {}).values()}
    
    filtered_data = {k: v for k, v in data.items() if k in fields}
    return cls(**filtered_data)


def create_dataclasses_from_list(cls: Type[T], data: List[Dict[str, Any]]) -> List[T]:
    """
    Create a list of dataclass instances from a list of dictionaries.
    
    Args:
        cls: Dataclass type to instantiate
        data: List of dictionaries with field values
        
    Returns:
        List of dataclass instances
    """
    return [create_dataclass_from_dict(cls, item) for item in data]


# ============================================================================
# Exported Functions
# ============================================================================


__all__ = [
    'ThingeryLoader',
    'get_loader',
    'load_yaml',
    'load_category',
    'create_dataclass_from_dict',
    'create_dataclasses_from_list',
    'DATA_DIR',
    'THINGERY_DIR',
]
