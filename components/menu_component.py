"""
Menu Component - Handles console UI and user interaction.
"""
import os
from typing import List, Optional
from components.constants import APP_NAME, APP_VERSION, CREATORS, APP_INTRO
from components.colors import (
    header, success, error, warning, info, highlight, dim, bold,
    menu_item, table_header, field_label, field_value,
    separator, box_top, box_bottom, banner, Colors, colorize
)


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
    """Display the application header with creators and intro."""
    print()
    print(box_top())
    print(banner(APP_NAME))
    print(banner(f"Version {APP_VERSION}"))
    print(box_bottom())
    print()
    
    # Show creators
    creators_str = ", ".join(CREATORS)
    print(dim(f"Created by: {creators_str}"))
    print()
    
    # Show intro
    print(info("About this application:"))
    for line in APP_INTRO.strip().split("\n"):
        print(dim(f"  {line}"))
    print()


def display_login_menu() -> str:
    """
    Display the login menu and get user choice.
    
    Returns:
        User's menu choice
    """
    print()
    print(header("--- Login ---"))
    print()
    print(menu_item("1", f"Super User {highlight('(Full Access)')}" ))
    print(menu_item("2", f"Guest {dim('(View Only)')}"))
    print(menu_item("0", "Exit"))
    print(separator("-", 30))
    
    return input(f"{info('>')} Select option: ").strip()


def display_setup_screen():
    """Display the super user setup header."""
    print()
    print(box_top())
    print(banner("FIRST TIME SETUP"))
    print(box_bottom())
    print()
    print(warning("No super user found. Please create one to manage countries."))
    print(separator("-", 50))


def display_menu(is_super_user: bool = False) -> str:
    """
    Display the main menu based on user role.
    
    Args:
        is_super_user: True if logged in as super user
        
    Returns:
        User's menu choice
    """
    role = highlight("Super User") if is_super_user else dim("Guest")
    print()
    print(header(f"--- Main Menu ({APP_VERSION}) [{role}] ---"))
    print()
    
    print(menu_item("1", "List all countries"))
    
    if is_super_user:
        print(menu_item("2", "Add new country"))
        print(menu_item("3", "Edit country"))
        print(menu_item("4", "Delete country"))
    
    print(menu_item("5", "Filter countries"))
    print(menu_item("6", "Search countries"))
    print(menu_item("7", "Export to PDF"))
    
    if is_super_user:
        print(menu_item("8", "Import from Source"))
    
    print(menu_item("9", "Statistics"))
    
    if is_super_user:
        print(separator("-", 30))
        print(menu_item("C", "Manage Cities"))
    
    print(separator("-", 30))
    print(menu_item("0", "Exit / Logout"))
    print()
    
    return input(f"{info('>')} Select option: ").strip()


def display_countries(countries: List[dict], detailed: bool = False):
    """
    Display a list of countries.
    
    Args:
        countries: List of country dictionaries
        detailed: If True, show all fields; otherwise show summary
    """
    if not countries:
        print(warning("\nNo countries found."))
        return
    
    print()
    print(header(f"━━━ 🌍 Found {len(countries)} country(ies) ━━━"))
    
    if detailed:
        for country in countries:
            print()
            print(highlight(f"── {country.get('country', 'N/A')} ──"))
            print(f"  {field_label('ISO:')}             {field_value(country.get('iso', 'N/A'))}")
            print(f"  {field_label('ISO3:')}            {field_value(country.get('iso3', 'N/A'))}")
            print(f"  {field_label('TLD:')}             {field_value(country.get('tld', 'N/A'))}")
            print(f"  {field_label('Currency:')}        {field_value(country.get('currency_code', 'N/A'))} ({country.get('currency_name', 'N/A')})")
            print(f"  {field_label('Phone:')}           {field_value(country.get('phone', 'N/A'))}")
            print(f"  {field_label('Postal Format:')}   {field_value(country.get('postal_code_format', 'N/A'))}")
            print(f"  {field_label('Postal Regex:')}    {dim(country.get('postal_code_regex', 'N/A'))}")
            print(f"  {field_label('Languages:')}       {field_value(country.get('languages', 'N/A'))}")
            print(f"  {field_label('GeoName ID:')}      {dim(country.get('geonameid', 'N/A'))}")
            cities = country.get('cities', [])
            print(f"  {field_label('Cities:')}          {info(', '.join(cities)) if cities else dim('N/A')}")
    else:
        print()
        print(table_header(f"{'ISO':<6} {'ISO3':<6} {'Country':<30} {'Currency':<10} {'Phone':<10}"))
        print(separator("─", 65))
        for country in countries:
            iso_str = colorize(country.get('iso', ''), Colors.BRIGHT_YELLOW)
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


def get_country_input(existing: Optional[dict] = None, countries: list = None, exclude_iso: str = "") -> dict:
    """
    Get country data from user input with real-time validation.
    
    Args:
        existing: Existing country data for editing (optional)
        countries: List of existing countries for validation (optional)
        exclude_iso: ISO code to exclude from validation (for editing)
        
    Returns:
        Dictionary with country data, or None if validation fails
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
    
    def validate_unique_field(field_name: str, value: str, display_name: str) -> bool:
        """Check if a field value is unique among existing countries."""
        if not countries or not value:
            return True
        
        value_upper = value.upper() if field_name in ("iso", "iso3") else value.lower()
        
        for country in countries:
            current_iso = country.get("iso", "").upper()
            
            # Skip the country being edited
            if exclude_iso and current_iso == exclude_iso.upper():
                continue
            
            existing_value = country.get(field_name, "")
            if field_name in ("iso", "iso3"):
                existing_value = existing_value.upper()
            else:
                existing_value = existing_value.lower()
            
            if existing_value == value_upper:
                print(error(f"  ✗ {display_name} '{value}' already exists!"))
                return False
        
        print(success(f"  ✓ {display_name} is available"))
        return True
    
    # Get and validate ISO code
    while True:
        iso = get_field("iso", info("ISO Code (2 letters)"))
        if not iso:
            print(error("  ✗ ISO code is required"))
            continue
        if len(iso) != 2:
            print(error("  ✗ ISO code must be exactly 2 characters"))
            continue
        if validate_unique_field("iso", iso, "ISO Code"):
            break
    
    # Get and validate ISO3 code
    while True:
        iso3 = get_field("iso3", info("ISO3 Code (3 letters)"))
        if not iso3:
            print(error("  ✗ ISO3 code is required"))
            continue
        if len(iso3) != 3:
            print(error("  ✗ ISO3 code must be exactly 3 characters"))
            continue
        if validate_unique_field("iso3", iso3, "ISO3 Code"):
            break
    
    # Get and validate country name
    while True:
        country_name = get_field("country", info("Country Name"))
        if not country_name:
            print(error("  ✗ Country name is required"))
            continue
        if validate_unique_field("country", country_name, "Country Name"):
            break
    
    # Get remaining fields (no uniqueness validation needed)
    return {
        "iso": iso,
        "iso3": iso3,
        "country": country_name,
        "tld": get_field("tld", "Top-Level Domain"),
        "currency_code": get_field("currency_code", "Currency Code"),
        "currency_name": get_field("currency_name", "Currency Name"),
        "phone": get_field("phone", "Phone Code"),
        "postal_code_format": get_field("postal_code_format", "Postal Code Format"),
        "postal_code_regex": get_field("postal_code_regex", "Postal Code Regex"),
        "languages": get_field("languages", "Languages"),
        "geonameid": get_field("geonameid", "GeoName ID"),
        "cities": get_cities_field(existing),
    }


def get_cities_field(existing: Optional[dict] = None) -> list:
    """
    Get cities list from user input.
    
    Args:
        existing: Existing country data for editing (optional)
        
    Returns:
        List of city names
    """
    current_cities = existing.get("cities", []) if existing else []
    
    if current_cities:
        print(f"\nCurrent cities: {', '.join(current_cities)}")
    
    print("\nEnter cities (comma-separated, or press Enter to keep current):")
    cities_input = input("Cities: ").strip()
    
    if not cities_input:
        return current_cities
    
    # Parse comma-separated cities
    cities = [c.strip() for c in cities_input.split(",") if c.strip()]
    return cities


def confirm_action(message: str) -> bool:
    """
    Ask user to confirm an action.
    
    Args:
        message: Confirmation message
        
    Returns:
        True if confirmed, False otherwise
    """
    response = input(f"\n{warning('⚠')} {message} {dim('(y/n)')}: ").strip().lower()
    return response in ('y', 'yes')


def pause():
    """Pause and wait for user to press Enter."""
    input(dim("\n⏎ Press Enter to continue..."))


def display_message(message: str, is_error: bool = False):
    """
    Display a message to the user.
    
    Args:
        message: Message to display
        is_error: If True, format as error message
    """
    if is_error:
        print(error(f"\n✗ {message}"))
    else:
        print(success(f"\n✓ {message}"))
