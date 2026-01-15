"""
Authentication Component - Handles user authentication and password encryption.
"""
import json
import os
import hashlib
import secrets
from typing import Optional, Tuple

from .constants import BASE_DIR

# Users file path
USERS_FILE = os.path.join(BASE_DIR, "users.json")


def generate_salt() -> str:
    """Generate a random salt for password hashing."""
    return secrets.token_hex(16)


def hash_password(password: str, salt: str) -> str:
    """
    Hash a password with the given salt using SHA256.
    
    Args:
        password: Plain text password
        salt: Random salt string
        
    Returns:
        Hexadecimal hash string
    """
    combined = f"{salt}{password}"
    return hashlib.sha256(combined.encode('utf-8')).hexdigest()


def verify_password(password: str, salt: str, password_hash: str) -> bool:
    """
    Verify a password against stored hash.
    
    Args:
        password: Plain text password to verify
        salt: Salt used in hashing
        password_hash: Stored hash to compare against
        
    Returns:
        True if password matches, False otherwise
    """
    return hash_password(password, salt) == password_hash


def load_users() -> dict:
    """Load users data from JSON file."""
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"super_user": None}
    except json.JSONDecodeError:
        return {"super_user": None}


def save_users(users: dict) -> bool:
    """Save users data to JSON file."""
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving users data: {e}")
        return False


def is_super_user_created() -> bool:
    """Check if a super user has been created."""
    users = load_users()
    return users.get("super_user") is not None


def create_super_user(password: str) -> Tuple[bool, str]:
    """
    Create a new super user with encrypted password.
    
    Args:
        password: Plain text password
        
    Returns:
        Tuple of (success, message)
    """
    if is_super_user_created():
        return False, "Super user already exists"
    
    if len(password) < 4:
        return False, "Password must be at least 4 characters"
    
    salt = generate_salt()
    password_hash = hash_password(password, salt)
    
    users = load_users()
    users["super_user"] = {
        "salt": salt,
        "password_hash": password_hash
    }
    
    if save_users(users):
        return True, "Super user created successfully"
    return False, "Failed to save super user data"


def authenticate_super_user(password: str) -> Tuple[bool, str]:
    """
    Authenticate a super user login attempt.
    
    Args:
        password: Plain text password
        
    Returns:
        Tuple of (success, message)
    """
    users = load_users()
    super_user = users.get("super_user")
    
    if super_user is None:
        return False, "No super user has been created"
    
    salt = super_user.get("salt", "")
    stored_hash = super_user.get("password_hash", "")
    
    if verify_password(password, salt, stored_hash):
        return True, "Login successful"
    return False, "Invalid password"
