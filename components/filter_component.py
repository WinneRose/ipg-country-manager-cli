"""
Filter Component - Provides filtering and search functionality for countries.
"""
from typing import List


def filter_by_field(countries: List[dict], field: str, value: str) -> List[dict]:
    """
    Filter countries by a specific field value.
    
    Args:
        countries: List of country dictionaries
        field: Field name to filter by
        value: Value to match (case-insensitive)
        
    Returns:
        Filtered list of countries
    """
    value_lower = value.lower()
    return [
        country for country in countries
        if value_lower in str(country.get(field, "")).lower()
    ]


def search_countries(countries: List[dict], query: str) -> List[dict]:
    """
    Search countries across all fields.
    
    Args:
        countries: List of country dictionaries
        query: Search query (case-insensitive)
        
    Returns:
        List of matching countries
    """
    query_lower = query.lower()
    results = []
    
    for country in countries:
        for field, value in country.items():
            if query_lower in str(value).lower():
                results.append(country)
                break
    
    return results


def get_filterable_fields() -> List[tuple[str, str]]:
    """
    Get list of fields that can be used for filtering.
    
    Returns:
        List of (field_key, field_display_name) tuples
    """
    return [
        ("iso", "ISO Code"),
        ("iso3", "ISO3 Code"),
        ("country", "Country Name"),
        ("tld", "Top-Level Domain"),
        ("currency_code", "Currency Code"),
        ("currency_name", "Currency Name"),
        ("phone", "Phone Code"),
        ("languages", "Languages"),
    ]
