"""
City Handlers - UI logic for city CRUD operations within countries.
"""
from ..menu_component import (
    display_message,
    confirm_action,
)
from ..data_handler import (
    list_countries,
    get_country,
    update_country,
)


def handle_list_cities():
    """Handle listing cities for a specific country."""
    print("\n--- List Cities ---")
    iso = input("Enter country ISO code: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    cities = country.get("cities", [])
    print(f"\nCities in {country.get('country', iso)}:")
    print("-" * 30)
    
    if not cities:
        print("No cities found.")
    else:
        for i, city in enumerate(cities, 1):
            print(f"  {i}. {city}")
    
    print(f"\nTotal: {len(cities)} city(ies)")


def handle_add_city():
    """Handle adding a city to a country."""
    print("\n--- Add City ---")
    iso = input("Enter country ISO code: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    print(f"\nAdding city to: {country.get('country', iso)}")
    city_name = input("Enter city name: ").strip()
    
    if not city_name:
        display_message("City name is required", is_error=True)
        return
    
    cities = country.get("cities", [])
    
    # Check for duplicate
    if city_name.lower() in [c.lower() for c in cities]:
        display_message(f"City '{city_name}' already exists in this country", is_error=True)
        return
    
    if confirm_action(f"Add city '{city_name}' to {country.get('country')}?"):
        cities.append(city_name)
        country["cities"] = cities
        success, message = update_country(iso, country)
        display_message(message, is_error=not success)


def handle_edit_city():
    """Handle editing a city name in a country."""
    print("\n--- Edit City ---")
    iso = input("Enter country ISO code: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    cities = country.get("cities", [])
    if not cities:
        display_message("No cities found in this country", is_error=True)
        return
    
    print(f"\nCities in {country.get('country', iso)}:")
    for i, city in enumerate(cities, 1):
        print(f"  {i}. {city}")
    
    try:
        index = int(input("\nEnter city number to edit: ").strip()) - 1
        if index < 0 or index >= len(cities):
            display_message("Invalid city number", is_error=True)
            return
    except ValueError:
        display_message("Please enter a valid number", is_error=True)
        return
    
    old_name = cities[index]
    new_name = input(f"Enter new name for '{old_name}': ").strip()
    
    if not new_name:
        display_message("City name cannot be empty", is_error=True)
        return
    
    # Check for duplicate
    if new_name.lower() in [c.lower() for c in cities if c != old_name]:
        display_message(f"City '{new_name}' already exists in this country", is_error=True)
        return
    
    if confirm_action(f"Rename '{old_name}' to '{new_name}'?"):
        cities[index] = new_name
        country["cities"] = cities
        success, message = update_country(iso, country)
        display_message(message, is_error=not success)


def handle_delete_city():
    """Handle removing a city from a country."""
    print("\n--- Delete City ---")
    iso = input("Enter country ISO code: ").strip()
    
    if not iso:
        display_message("ISO code is required", is_error=True)
        return
    
    country = get_country(iso)
    if not country:
        display_message(f"Country with ISO code '{iso}' not found", is_error=True)
        return
    
    cities = country.get("cities", [])
    if not cities:
        display_message("No cities found in this country", is_error=True)
        return
    
    print(f"\nCities in {country.get('country', iso)}:")
    for i, city in enumerate(cities, 1):
        print(f"  {i}. {city}")
    
    try:
        index = int(input("\nEnter city number to delete: ").strip()) - 1
        if index < 0 or index >= len(cities):
            display_message("Invalid city number", is_error=True)
            return
    except ValueError:
        display_message("Please enter a valid number", is_error=True)
        return
    
    city_name = cities[index]
    
    if confirm_action(f"Delete city '{city_name}' from {country.get('country')}?"):
        cities.pop(index)
        country["cities"] = cities
        success, message = update_country(iso, country)
        display_message(message, is_error=not success)
