"""
Colors Component - ANSI color codes for terminal beautification.
Cross-platform support using colorama for Windows.
"""
import os
import sys

# Try to use colorama for Windows compatibility
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False


# ANSI Color codes (fallback)
class Colors:
    """ANSI color codes for terminal output."""
    # Reset
    RESET = '\033[0m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'


# Enable ANSI on Windows 10+
if os.name == 'nt':
    os.system('')  # Enables ANSI escape codes in Windows terminal


# Color helper functions
def colorize(text: str, color: str) -> str:
    """Apply color to text and reset after."""
    return f"{color}{text}{Colors.RESET}"


def header(text: str) -> str:
    """Format text as a header (cyan, bold)."""
    return colorize(text, Colors.BOLD + Colors.BRIGHT_CYAN)


def success(text: str) -> str:
    """Format text as success message (green)."""
    return colorize(text, Colors.BRIGHT_GREEN)


def error(text: str) -> str:
    """Format text as error message (red)."""
    return colorize(text, Colors.BRIGHT_RED)


def warning(text: str) -> str:
    """Format text as warning message (yellow)."""
    return colorize(text, Colors.BRIGHT_YELLOW)


def info(text: str) -> str:
    """Format text as info message (blue)."""
    return colorize(text, Colors.BRIGHT_BLUE)


def highlight(text: str) -> str:
    """Format text as highlighted (magenta)."""
    return colorize(text, Colors.BRIGHT_MAGENTA)


def dim(text: str) -> str:
    """Format text as dimmed (gray)."""
    return colorize(text, Colors.BRIGHT_BLACK)


def bold(text: str) -> str:
    """Format text as bold."""
    return colorize(text, Colors.BOLD)


def menu_item(number: str, text: str) -> str:
    """Format a menu item with colored number."""
    num_colored = colorize(number, Colors.BRIGHT_YELLOW + Colors.BOLD)
    return f"{num_colored}. {text}"


def table_header(text: str) -> str:
    """Format table header text."""
    return colorize(text, Colors.BOLD + Colors.BRIGHT_WHITE)


def field_label(text: str) -> str:
    """Format field label."""
    return colorize(text, Colors.CYAN)


def field_value(text: str) -> str:
    """Format field value."""
    return colorize(text, Colors.WHITE)


def separator(char: str = "─", length: int = 60) -> str:
    """Create a colored separator line."""
    return colorize(char * length, Colors.BRIGHT_BLACK)


def box_top(length: int = 60) -> str:
    """Create box top border."""
    return colorize("╔" + "═" * (length - 2) + "╗", Colors.BRIGHT_CYAN)


def box_bottom(length: int = 60) -> str:
    """Create box bottom border."""
    return colorize("╚" + "═" * (length - 2) + "╝", Colors.BRIGHT_CYAN)


def box_side() -> str:
    """Create box side border."""
    return colorize("║", Colors.BRIGHT_CYAN)


def banner(text: str, width: int = 60) -> str:
    """Create a centered banner with box borders."""
    padding = (width - 4 - len(text)) // 2
    content = " " * padding + text + " " * (width - 4 - len(text) - padding)
    return f"{box_side()} {colorize(content, Colors.BOLD + Colors.BRIGHT_WHITE)} {box_side()}"
