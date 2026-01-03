"""
Data Handler Component - Manages CRUD operations for country data.
"""
import json
import os
from typing import List, Optional

from .constants import DATA_FILE

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_countries() -> List[dict]:
    """
    Load all countries from the JSON file.
    
    Returns:
        List of country dictionaries
    """
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("countries", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in data file")
        return []


def save_countries(countries: List[dict]) -> bool:
    """
    Save countries to the JSON file.
    
    Args:
        countries: List of country dictionaries
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"countries": countries}, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False


def get_country(iso: str) -> Optional[dict]:
    """
    Get a single country by ISO code.
    
    Args:
        iso: ISO 2-letter code
        
    Returns:
        Country dictionary or None if not found
    """
    countries = load_countries()
    iso_upper = iso.upper()
    for country in countries:
        if country.get("iso", "").upper() == iso_upper:
            return country
    return None


def add_country(country_data: dict) -> tuple[bool, str]:
    """
    Add a new country to the data file.
    
    Args:
        country_data: Country dictionary
        
    Returns:
        Tuple of (success, message)
    """
    countries = load_countries()
    
    # Check for duplicate ISO
    iso = country_data.get("iso", "").upper()
    for country in countries:
        if country.get("iso", "").upper() == iso:
            return False, f"Country with ISO code '{iso}' already exists"
    
    country_data["iso"] = iso
    countries.append(country_data)
    
    if save_countries(countries):
        return True, f"Country '{country_data.get('country')}' added successfully"
    return False, "Failed to save data"


def update_country(iso: str, updated_data: dict) -> tuple[bool, str]:
    """
    Update an existing country.
    
    Args:
        iso: ISO code of country to update
        updated_data: New data for the country
        
    Returns:
        Tuple of (success, message)
    """
    countries = load_countries()
    iso_upper = iso.upper()
    
    for i, country in enumerate(countries):
        if country.get("iso", "").upper() == iso_upper:
            # Update fields
            for key, value in updated_data.items():
                if value is not None:
                    countries[i][key] = value
            
            if save_countries(countries):
                return True, f"Country '{iso}' updated successfully"
            return False, "Failed to save data"
    
    return False, f"Country with ISO code '{iso}' not found"


def delete_country(iso: str) -> tuple[bool, str]:
    """
    Delete a country by ISO code.
    
    Args:
        iso: ISO code of country to delete
        
    Returns:
        Tuple of (success, message)
    """
    countries = load_countries()
    iso_upper = iso.upper()
    
    for i, country in enumerate(countries):
        if country.get("iso", "").upper() == iso_upper:
            deleted = countries.pop(i)
            
            if save_countries(countries):
                return True, f"Country '{deleted.get('country')}' deleted successfully"
            return False, "Failed to save data"
    
    return False, f"Country with ISO code '{iso}' not found"


def list_countries() -> List[dict]:
    """
    List all countries.
    
    Returns:
        List of all country dictionaries
    """
    return load_countries()
