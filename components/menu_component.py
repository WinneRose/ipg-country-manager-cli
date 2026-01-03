"""
Menu Component - Handles console UI and user interaction.
"""
import os
from typing import List, Optional
from components.constants import APP_NAME, APP_VERSION


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    """Display the application header."""
    print("=" * 60)
    print(f"           {APP_NAME} - Console Application")
    print("=" * 60)
    print()


def display_menu() -> str:
    """
    Display the main menu and get user choice.
    
    Returns:
        User's menu choice
    """
    print(f"\n--- Main Menu ({APP_VERSION}) ---")
    print("1. List all countries")
    print("2. Add new country")
    print("3. Edit country")
    print("4. Delete country")
    print("5. Filter countries")
    print("6. Search countries")
    print("7. Export to PDF")
    print("8. Import from Source")
    print("9. Statistics")
    print("0. Exit")
    print("-" * 30)
    
    return input("Select option: ").strip()


def display_countries(countries: List[dict], detailed: bool = False):
    """
    Display a list of countries.
    
    Args:
        countries: List of country dictionaries
        detailed: If True, show all fields; otherwise show summary
    """
    if not countries:
        print("\nNo countries found.")
        return
    
    print(f"\n{'='*60}")
    print(f"Found {len(countries)} country(ies)")
    print(f"{'='*60}")
    
    if detailed:
        for country in countries:
            print(f"\n--- {country.get('country', 'N/A')} ---")
            print(f"  ISO:             {country.get('iso', 'N/A')}")
            print(f"  ISO3:            {country.get('iso3', 'N/A')}")
            print(f"  TLD:             {country.get('tld', 'N/A')}")
            print(f"  Currency:        {country.get('currency_code', 'N/A')} ({country.get('currency_name', 'N/A')})")
            print(f"  Phone:           {country.get('phone', 'N/A')}")
            print(f"  Postal Format:   {country.get('postal_code_format', 'N/A')}")
            print(f"  Postal Regex:    {country.get('postal_code_regex', 'N/A')}")
            print(f"  Languages:       {country.get('languages', 'N/A')}")
            print(f"  GeoName ID:      {country.get('geonameid', 'N/A')}")
    else:
        print(f"\n{'ISO':<6} {'ISO3':<6} {'Country':<30} {'Currency':<10} {'Phone':<10}")
        print("-" * 65)
        for country in countries:
            print(f"{country.get('iso', ''):<6} "
                  f"{country.get('iso3', ''):<6} "
                  f"{country.get('country', '')[:28]:<30} "
                  f"{country.get('currency_code', ''):<10} "
                  f"{country.get('phone', ''):<10}")


def display_country_detail(country: dict):
    """
    Display detailed information for a single country.
    
    Args:
        country: Country dictionary
    """
    display_countries([country], detailed=True)


def get_country_input(existing: Optional[dict] = None) -> dict:
    """
    Get country data from user input.
    
    Args:
        existing: Existing country data for editing (optional)
        
    Returns:
        Dictionary with country data
    """
    print("\nEnter country details (press Enter to keep existing value):")
    print("-" * 40)
    
    def get_field(field_name: str, display_name: str) -> str:
        current = existing.get(field_name, "") if existing else ""
        prompt = f"{display_name}"
        if current:
            prompt += f" [{current}]"
        prompt += ": "
        
        value = input(prompt).strip()
        return value if value else current
    
    return {
        "iso": get_field("iso", "ISO Code (2 letters)"),
        "iso3": get_field("iso3", "ISO3 Code (3 letters)"),
        "country": get_field("country", "Country Name"),
        "tld": get_field("tld", "Top-Level Domain"),
        "currency_code": get_field("currency_code", "Currency Code"),
        "currency_name": get_field("currency_name", "Currency Name"),
        "phone": get_field("phone", "Phone Code"),
        "postal_code_format": get_field("postal_code_format", "Postal Code Format"),
        "postal_code_regex": get_field("postal_code_regex", "Postal Code Regex"),
        "languages": get_field("languages", "Languages"),
        "geonameid": get_field("geonameid", "GeoName ID"),
    }


def confirm_action(message: str) -> bool:
    """
    Ask user to confirm an action.
    
    Args:
        message: Confirmation message
        
    Returns:
        True if confirmed, False otherwise
    """
    response = input(f"\n{message} (y/n): ").strip().lower()
    return response in ('y', 'yes')


def pause():
    """Pause and wait for user to press Enter."""
    input("\nPress Enter to continue...")


def display_message(message: str, is_error: bool = False):
    """
    Display a message to the user.
    
    Args:
        message: Message to display
        is_error: If True, format as error message
    """
    if is_error:
        print(f"\n[ERROR] {message}")
    else:
        print(f"\n[OK] {message}")
