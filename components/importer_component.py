"""
Importer Component - Parse and import country data from source file.
"""
import os
from typing import List, Tuple
from .constants import SOURCE_FILE, CSV_MAPPING
from country_types import Country, create_empty_country

def parse_source_file() -> Tuple[List[dict], List[str]]:
    """
    Parse the countryInfo.txt file.
    
    Returns:
        Tuple of (valid_countries, errors)
    """
    valid_countries = []
    errors = []
    
    if not os.path.exists(SOURCE_FILE):
        return [], [f"Source file not found: {SOURCE_FILE}"]
        
    try:
        with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith('#') or line.startswith('ISO'):
                continue
                
            parts = line.split('\t')
            
            # Basic validation of column count (max index in mapping is 16)
            if len(parts) <= 16:
                errors.append(f"Line {i+1}: Insufficient columns")
                continue
                
            try:
                country: Country = create_empty_country()
                
                # Map fields from CSV columns to Country dict
                for idx, field in CSV_MAPPING.items():
                    if idx < len(parts):
                        country[field] = parts[idx].strip()
                
                valid_countries.append(country)
                
            except Exception as e:
                errors.append(f"Line {i+1}: Error parsing - {e}")
                
    except Exception as e:
        errors.append(f"File read error: {e}")
        
    return valid_countries, errors
