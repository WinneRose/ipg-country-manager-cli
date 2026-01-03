"""
Import Handlers - UI logic for importing data.
"""
from ..menu_component import (
    display_message,
    confirm_action,
)
from ..data_handler import add_country, load_countries, save_countries
from ..importer_component import parse_source_file

def handle_import_data():
    """Handle importing data from source file."""
    print("\n--- Import from Source File ---")
    print("This will import countries from 'countryInfo.txt'.")
    print("Existing countries with the same ISO code will be skipped.")
    
    if not confirm_action("Proceed with import?"):
        return

    print("\nReading source file...")
    new_countries, errors = parse_source_file()
    
    if errors:
        print(f"\nEncoutered {len(errors)} issues during parsing:")
        for err in errors[:5]:
            print(f"  - {err}")
        if len(errors) > 5:
            print(f"  ...and {len(errors)-5} more.")
            
    if not new_countries:
        display_message("No valid countries found to import.", is_error=True)
        return
        
    print(f"\nFound {len(new_countries)} valid countries in source.")
    
    # Process import
    current_countries = load_countries()
    existing_isos = {c['iso'].upper() for c in current_countries}
    
    added_count = 0
    skipped_count = 0
    
    to_add = []
    
    for country in new_countries:
        if country['iso'].upper() in existing_isos:
            skipped_count += 1
        else:
            to_add.append(country)
            existing_isos.add(country['iso'].upper())
            added_count += 1
    
    if to_add:
        # Batch update is more efficient than calling add_country repeatedly due to repeated file IO
        current_countries.extend(to_add)
        if save_countries(current_countries):
             display_message(f"Import complete. Added: {added_count}, Skipped: {skipped_count}")
        else:
             display_message("Failed to save imported data.", is_error=True)
    else:
        display_message(f"No new countries to add. Skipped: {skipped_count}")
