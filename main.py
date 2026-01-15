"""
Country Manager - Main Application Entry Point

A console application for managing country data with CRUD operations,
filtering, and PDF export. Features role-based access control.
"""
import sys
import os

# Add the parent directory to the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.constants import APP_VERSION
from components.menu_component import (
    clear_screen,
    display_header,
    pause,
    display_message,
    display_menu,
    display_login_menu,
    display_setup_screen,
)
from components.auth_component import (
    is_super_user_created,
    create_super_user,
    authenticate_super_user,
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
    handle_list_cities,
    handle_add_city,
    handle_edit_city,
    handle_delete_city,
)


def handle_setup_flow() -> bool:
    """
    Handle first-time super user setup.
    
    Returns:
        True if setup successful, False otherwise
    """
    display_setup_screen()
    
    password = input("Enter new password (min 4 chars): ").strip()
    if not password:
        display_message("Password cannot be empty", is_error=True)
        return False
    
    confirm = input("Confirm password: ").strip()
    if password != confirm:
        display_message("Passwords do not match", is_error=True)
        return False
    
    success, message = create_super_user(password)
    display_message(message, is_error=not success)
    return success


def handle_login_flow() -> tuple[bool, bool]:
    """
    Handle user login.
    
    Returns:
        Tuple of (should_continue, is_super_user)
    """
    choice = display_login_menu()
    
    if choice == "0":
        return False, False
    
    if choice == "1":
        # Super user login
        password = input("\nEnter super user password: ").strip()
        success, message = authenticate_super_user(password)
        
        if success:
            display_message("Welcome, Super User!", is_error=False)
            return True, True
        else:
            display_message(message, is_error=True)
            pause()
            return handle_login_flow()  # Retry
    
    elif choice == "2":
        # Guest login
        display_message("Welcome, Guest! (View-only access)", is_error=False)
        return True, False
    
    else:
        display_message("Invalid option", is_error=True)
        pause()
        return handle_login_flow()


def handle_city_menu():
    """Display and handle city management submenu."""
    print("\n--- City Management ---")
    print("1. List cities in a country")
    print("2. Add city to a country")
    print("3. Edit city name")
    print("4. Delete city")
    print("0. Back to main menu")
    print("-" * 30)
    
    choice = input("Select option: ").strip()
    
    if choice == "1":
        handle_list_cities()
    elif choice == "2":
        handle_add_city()
    elif choice == "3":
        handle_edit_city()
    elif choice == "4":
        handle_delete_city()
    elif choice == "0":
        return
    else:
        display_message("Invalid option", is_error=True)


def main():
    """Main application loop."""
    try:
        clear_screen()
        display_header()
        
        # Check if super user needs to be created
        if not is_super_user_created():
            if not handle_setup_flow():
                print("\nSetup cancelled. Exiting...")
                return
            pause()
        
        # Login flow
        clear_screen()
        display_header()
        should_continue, is_super_user = handle_login_flow()
        
        if not should_continue:
            print("\nGoodbye!")
            return
        
        pause()
        clear_screen()
        display_header()
        
        while True:
            choice = display_menu(is_super_user)
            
            if choice == "1":
                handle_list_countries()
            elif choice == "2" and is_super_user:
                handle_add_country()
            elif choice == "3" and is_super_user:
                handle_edit_country()
            elif choice == "4" and is_super_user:
                handle_delete_country()
            elif choice == "5":
                handle_filter_countries()
            elif choice == "6":
                handle_search_countries()
            elif choice == "7":
                handle_export_pdf()
            elif choice == "8" and is_super_user:
                handle_import_data()
            elif choice == "9":
                handle_show_statistics()
            elif choice.upper() == "C" and is_super_user:
                handle_city_menu()
            elif choice == "0":
                print("\nGoodbye!")
                break
            else:
                display_message("Invalid option or access denied.", is_error=True)
            
            pause()
            clear_screen()
            display_header()
            
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()

