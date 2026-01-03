"""
Components package for Country Manager application.
"""
from .data_handler import (
    load_countries,
    save_countries,
    get_country,
    add_country,
    update_country,
    delete_country,
    list_countries,
)
from .filter_component import (
    filter_by_field,
    search_countries,
    get_filterable_fields,
)
from .pdf_component import generate_pdf
from .menu_component import (
    clear_screen,
    display_header,
    display_menu,
    display_countries,
    display_country_detail,
    get_country_input,
    confirm_action,
    pause,
    display_message,
)

__all__ = [
    # Data handler
    "load_countries",
    "save_countries",
    "get_country",
    "add_country",
    "update_country",
    "delete_country",
    "list_countries",
    # Filter
    "filter_by_field",
    "search_countries",
    "get_filterable_fields",
    # PDF
    "generate_pdf",
    # Menu
    "clear_screen",
    "display_header",
    "display_menu",
    "display_countries",
    "display_country_detail",
    "get_country_input",
    "confirm_action",
    "pause",
    "display_message",
]
