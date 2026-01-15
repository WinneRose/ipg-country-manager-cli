"""
Handlers package for Country Manager application.
"""
from .country_handlers import (
    handle_list_countries,
    handle_add_country,
    handle_edit_country,
    handle_delete_country,
)
from .filter_handlers import (
    handle_filter_countries,
    handle_search_countries,
)
from .pdf_handlers import handle_export_pdf
from .import_handlers import handle_import_data
from .analytics_handlers import handle_show_statistics
from .auth_handlers import (
    handle_login,
    handle_setup,
)
from .city_handlers import (
    handle_list_cities,
    handle_add_city,
    handle_edit_city,
    handle_delete_city,
)

__all__ = [
    "handle_list_countries",
    "handle_add_country",
    "handle_edit_country",
    "handle_delete_country",
    "handle_filter_countries",
    "handle_search_countries",
    "handle_export_pdf",
    "handle_import_data",
    "handle_show_statistics",
    "handle_login",
    "handle_setup",
    "handle_list_cities",
    "handle_add_city",
    "handle_edit_city",
    "handle_delete_city",
]

