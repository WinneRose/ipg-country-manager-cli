"""
Filter Handlers - UI logic for filtering and searching countries.
"""
from ..menu_component import (
    display_countries,
    display_message,
)
from ..data_handler import list_countries
from ..filter_component import (
    filter_by_field,
    search_countries,
    get_filterable_fields,
)


def handle_filter_countries():
    """Handle filtering countries by field."""
    print("\n--- Filter Countries ---")
    print("\nAvailable fields:")
    
    fields = get_filterable_fields()
    for i, (key, name) in enumerate(fields, 1):
        print(f"  {i}. {name} ({key})")
    
    try:
        choice = int(input("\nSelect field number: ").strip())
        if 1 <= choice <= len(fields):
            field_key, field_name = fields[choice - 1]
            value = input(f"Enter value to filter by {field_name}: ").strip()
            
            if value:
                countries = list_countries()
                filtered = filter_by_field(countries, field_key, value)
                display_countries(filtered, detailed=True)
            else:
                display_message("Filter value is required", is_error=True)
        else:
            display_message("Invalid selection", is_error=True)
    except ValueError:
        display_message("Please enter a valid number", is_error=True)


def handle_search_countries():
    """Handle searching countries."""
    print("\n--- Search Countries ---")
    query = input("Enter search term: ").strip()
    
    if not query:
        display_message("Search term is required", is_error=True)
        return
    
    countries = list_countries()
    results = search_countries(countries, query)
    display_countries(results, detailed=True)
