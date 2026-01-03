"""
Test script for Country Manager Application.
Verifies CRUD operations, Import, Analytics, and PDF generation.
"""
import os
import sys
import json
import unittest

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components import (
    load_countries,
    add_country,
    get_country,
    update_country,
    delete_country,
    filter_by_field,
    search_countries,
    generate_pdf,
)
from components.importer_component import parse_source_file
from components.analytics_component import get_general_stats, get_currency_stats

# Backup original data file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "dados.json")
BACKUP_FILE = os.path.join(BASE_DIR, "dados.json.bak")

def backup_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = f.read()
        with open(BACKUP_FILE, 'w', encoding='utf-8') as f:
            f.write(data)

def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
            data = f.read()
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            f.write(data)
        os.remove(BACKUP_FILE)

class TestCountryManager(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        backup_data()
        
    @classmethod
    def tearDownClass(cls):
        restore_data()

    def test_01_read_initial_data(self):
        countries = load_countries()
        self.assertGreaterEqual(len(countries), 3)
        print(f"\n[OK] Loaded {len(countries)} countries.")

    def test_02_add_country(self):
        new_country = {
            "iso": "TS",
            "iso3": "TST",
            "country": "Testland",
            "tld": ".ts",
            "currency_code": "TST",
            "currency_name": "Test Coin",
            "phone": "999",
            "postal_code_format": "#####",
            "postal_code_regex": "^(\\d{5})$",
            "languages": "en,ts",
            "geonameid": "000000"
        }
        success, msg = add_country(new_country)
        self.assertTrue(success, msg)
        
        c = get_country("TS")
        self.assertIsNotNone(c)
        print("\n[OK] Added Country 'Testland'")

    def test_03_analytics(self):
        countries = load_countries()
        stats = get_general_stats(countries)
        self.assertGreater(stats['total'], 0)
        
        curr_stats = get_currency_stats(countries)
        self.assertTrue(len(curr_stats) > 0)
        print("\n[OK] Analytics calculated successfully")

    def test_04_import_parsing(self):
        # Parses the actual source file if present
        countries, errors = parse_source_file()
        if os.path.exists(os.path.join(BASE_DIR, "countryInfo.txt")):
            self.assertGreater(len(countries), 0)
            print(f"\n[OK] Parser found {len(countries)} valid countries in source file")
        else:
            print("\n[SKIP] Source file not found, skipping import test")

    def test_05_pdf_generation(self):
        countries = load_countries()
        success, path = generate_pdf(countries, "test_report.pdf")
        self.assertTrue(success, path)
        if os.path.exists(path):
            os.remove(path)
        print(f"\n[OK] generated PDF at {path}")

    def test_06_delete_country(self):
        success, msg = delete_country("TS")
        self.assertTrue(success, msg)
        c = get_country("TS")
        self.assertIsNone(c)
        print("\n[OK] Deleted Country 'Testland'")

if __name__ == '__main__':
    unittest.main(verbosity=2)
