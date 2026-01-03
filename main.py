"""
Country Manager - Main Application Entry Point

A console application for managing country data with CRUD operations,
filtering, and PDF export.
"""
import sys
import os

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.constants import  APP_VERSION
from components.menu_component import (
    clear_screen,
    display_header,
    pause,
    display_message,
    display_menu,
)

from components.handlers import (
    handle_list_countries,
    handle_add_country,
    handle_edit_country,
    handle_delete_country,
    handle_filter_countries,
    handle_search_countries,
    handle_export_pdf,
    handle_import_data,
    handle_show_statistics,
)



def main():
    """Main application loop."""
    try:
        clear_screen()
        display_header()
        
        while True:
            choice = display_menu()
            
            if choice == "1":
                handle_list_countries()
            elif choice == "2":
                handle_add_country()
            elif choice == "3":
                handle_edit_country()
            elif choice == "4":
                handle_delete_country()
            elif choice == "5":
                handle_filter_countries()
            elif choice == "6":
                handle_search_countries()
            elif choice == "7":
                handle_export_pdf()
            elif choice == "8":
                handle_import_data()
            elif choice == "9":
                handle_show_statistics()
            elif choice == "0":
                print("\nGoodbye!")
                break
            else:
                display_message("Invalid option. Please try again.", is_error=True)
            
            pause()
            clear_screen()
            display_header()
            
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
