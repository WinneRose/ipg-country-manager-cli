"""
Type definitions for Country Manager application.
"""
from typing import TypedDict, Optional, List


class Country(TypedDict):
    """Type definition for a country record."""
    iso: str                      # ISO 2-letter code (e.g., "AD")
    iso3: str                     # ISO 3-letter code (e.g., "AND")
    country: str                  # Country name (e.g., "Andorra")
    tld: str                      # Top-level domain (e.g., ".ad")
    currency_code: str            # Currency code (e.g., "EUR")
    currency_name: str            # Currency name (e.g., "Euro")
    phone: str                    # Phone code (e.g., "376")
    postal_code_format: str       # Postal code format (e.g., "AD###")
    postal_code_regex: str        # Postal code regex pattern
    languages: str                # Languages spoken (e.g., "ca")
    geonameid: str                # Geonames ID


# Field names for display and input
COUNTRY_FIELDS = [
    ("iso", "ISO Code (2 letters)"),
    ("iso3", "ISO3 Code (3 letters)"),
    ("country", "Country Name"),
    ("tld", "Top-Level Domain"),
    ("currency_code", "Currency Code"),
    ("currency_name", "Currency Name"),
    ("phone", "Phone Code"),
    ("postal_code_format", "Postal Code Format"),
    ("postal_code_regex", "Postal Code Regex"),
    ("languages", "Languages"),
    ("geonameid", "GeoName ID"),
]


def validate_country(data: dict) -> tuple[bool, str]:
    """
    Validate country data.
    
    Args:
        data: Dictionary with country data
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Required fields
    required = ["iso", "iso3", "country"]
    
    for field in required:
        if not data.get(field):
            return False, f"Field '{field}' is required"
    
    # Validate ISO code length
    if len(data.get("iso", "")) != 2:
        return False, "ISO code must be exactly 2 characters"
    
    if len(data.get("iso3", "")) != 3:
        return False, "ISO3 code must be exactly 3 characters"
    
    return True, ""


def create_empty_country() -> Country:
    """Create an empty country template."""
    return {
        "iso": "",
        "iso3": "",
        "country": "",
        "tld": "",
        "currency_code": "",
        "currency_name": "",
        "phone": "",
        "postal_code_format": "",
        "postal_code_regex": "",
        "languages": "",
        "geonameid": "",
    }
