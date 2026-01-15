"""
Authentication Handlers - UI logic for login and setup screens.
"""
from ..menu_component import display_message
from ..auth_component import (
    is_super_user_created,
    create_super_user,
    authenticate_super_user,
)


def handle_setup() -> bool:
    """
    Handle first-time super user setup.
    
    Returns:
        True if setup successful, False otherwise
    """
    print("\n" + "=" * 60)
    print("           FIRST TIME SETUP")
    print("=" * 60)
    print("\nNo super user found. Please create one to manage countries.")
    print("-" * 40)
    
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


def handle_login() -> tuple[bool, bool]:
    """
    Handle user login screen.
    
    Returns:
        Tuple of (success, is_super_user)
        - success: True if login process completed
        - is_super_user: True if logged in as super user
    """
    print("\n" + "=" * 60)
    print("           LOGIN")
    print("=" * 60)
    print("\n1. Super User (Full Access)")
    print("2. Guest (View Only)")
    print("0. Exit")
    print("-" * 30)
    
    choice = input("Select option: ").strip()
    
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
            return handle_login()  # Retry login
    
    elif choice == "2":
        # Guest login
        display_message("Welcome, Guest! (View-only access)", is_error=False)
        return True, False
    
    else:
        display_message("Invalid option", is_error=True)
        return handle_login()  # Retry login
