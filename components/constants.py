"""
Constants for Country Manager application.
"""
import os

# Base directory setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "dados.json")
SOURCE_FILE = os.path.join(BASE_DIR, "countryInfo.txt")
USERS_FILE = os.path.join(BASE_DIR, "users.json")

# Date/Time format
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# App Info
APP_NAME = "Country CRM Manager"
APP_VERSION = "1.1.0"
CREATORS = ["Burak", "Duarte", "Gökalp", "Ceren"]
APP_INTRO = """A console application for managing country data with:
- CRUD operations (Create, Read, Update, Delete)
- City management for each country  
- Filtering and searching capabilities
- PDF report generation
- Data import from external sources
- Role-based access control (Super User / Guest)"""

# CountryInfo.txt parsing configurations
# Mapping column indices (from countryInfo.txt) to Country TypedDict keys
# Based on the file header:
# ISO(0) ISO3(1) ... Country(4) ... tld(9) CurrencyCode(10) CurrencyName(11) 
# Phone(12) Postal Code Format(13) Postal Code Regex(14) Languages(15) geonameid(16)
CSV_MAPPING = {
    0: "iso",
    1: "iso3",
    4: "country",
    9: "tld",
    10: "currency_code",
    11: "currency_name",
    12: "phone",
    13: "postal_code_format",
    14: "postal_code_regex",
    15: "languages",
    16: "geonameid"
}
