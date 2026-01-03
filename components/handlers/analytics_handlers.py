"""
Analytics Handlers - UI logic for statistics.
"""
from ..data_handler import list_countries
from ..analytics_component import (
    get_general_stats,
    get_currency_stats,
    get_language_stats
)
from ..menu_component import display_header

def handle_show_statistics():
    """Show statistics dashboard."""
    print("\n--- Statistics Dashboard ---")
    
    countries = list_countries()
    stats = get_general_stats(countries)
    
    if stats["total"] == 0:
        print("No data available.")
        return

    print(f"Total Countries: {stats['total']}")
    print("-" * 30)
    
    print("Top 5 Currencies:")
    currencies = get_currency_stats(countries)
    for curr, count in currencies:
        print(f"  {curr}: {count}")
    print("-" * 30)
        
    print("Top 5 Languages:")
    langs = get_language_stats(countries)
    for lang, count in langs:
        print(f"  {lang}: {count}")
