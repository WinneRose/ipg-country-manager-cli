"""
Country Handlers - UI logic for country CRUD operations.
"""
from ..menu_component import (
    display_countries,
    get_country_input,
    display_message,
    confirm_action,
    display_country_detail,
)
from ..data_handler import (
    list_countries,
    add_country,
    get_country,
    update_country,
    delete_country,
)
from country_types import validate_country


def handle_list_countries():
    """Handle listing all countries."""
    countries = list_countries()
    
    if not countries:
        display_message("No countries found.", is_error=True)
        return

    # Sort options
    print("\nSort by:")
    print("1. ISO Code (Default)")
    print("2. Country Name")
    sort_choice = input("Select sort option (Enter for default): ").strip()
    
    if sort_choice == "2":
        countries.sort(key=lambda x: x.get('country', '').lower())
    else:
        countries.sort(key=lambda x: x.get('iso', ''))

    display_countries(countries, detailed=False)
    
    if countries:
        show_detail = input("\nShow detailed view? (y/n): ").strip().lower()
        if show_detail in ('y', 'yes'):
            display_countries(countries, detailed=True)


def handle_add_country():
    """Handle adding a new country."""
    print("\n--- Add New Country ---")
    country_data = get_country_input()
    
    is_valid, error = validate_country(country_data)
    if not is_valid:
        display_message(error, is_error=True)
        return
    
    if confirm_action(f"Add country '{country_data.get('country')}'?"):
        success, message = add_country(country_data)
        display_message(message, is_error=not success)


def handle_edit_country():
    """Handle editing an existing country."""
    print("\n--- Edit Country ---")
    iso = input("Enter ISO code of country to edit: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    print("\nCurrent data:")
    display_country_detail(country)
    
    print("\nEnter new values (press Enter to keep current):")
    updated_data = get_country_input(existing=country)
    
    is_valid, error = validate_country(updated_data)
    if not is_valid:
        display_message(error, is_error=True)
        return
    
    if confirm_action(f"Update country '{iso}'?"):
        success, message = update_country(iso, updated_data)
        display_message(message, is_error=not success)


def handle_delete_country():
    """Handle deleting a country."""
    print("\n--- Delete Country ---")
    iso = input("Enter ISO code of country to delete: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    print("\nCountry to delete:")
    display_country_detail(country)
    
    if confirm_action(f"Are you sure you want to delete '{country.get('country')}'?"):
        success, message = delete_country(iso)
        display_message(message, is_error=not success)
