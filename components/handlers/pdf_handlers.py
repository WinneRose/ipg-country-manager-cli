"""
PDF Handlers - UI logic for PDF export.
"""
from ..menu_component import display_message
from ..data_handler import list_countries
from ..pdf_component import generate_pdf


def handle_export_pdf():
    """Handle exporting countries to PDF."""
    print("\n--- Export to PDF ---")
    
    countries = list_countries()
    if not countries:
        display_message("No countries to export", is_error=True)
        return
    
    filename = input("Enter filename (default: countries_report.pdf): ").strip()
    if not filename:
        filename = "countries_report.pdf"
    
    if not filename.endswith(".pdf"):
        filename += ".pdf"
    
    print(f"\nExporting {len(countries)} countries to PDF...")
    success, result = generate_pdf(countries, filename)
    
    if success:
        display_message(f"PDF exported successfully: {result}")
    else:
        display_message(result, is_error=True)
