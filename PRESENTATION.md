# Country Manager Application - Project Presentation

## 1. Project Overview
**Country Manager** is a robust Python console application designed to manage, analyze, and export country data. It provides a user-friendly interface for performing CRUD (Create, Read, Update, Delete) operations, advanced filtering, statistics visualization, and reporting.

This project demonstrates clean code principles, modular architecture, and real-world application features like PDF generation and bulk data handling.

## 2. Key Features

### Core Functionality
- **CRUD Operations**: Complete management of country records (ISO codes, currency, language, etc.).
- **Data Persistence**: All data is automatically saved to a local JSON database (`dados.json`), ensuring no data loss between sessions.

### Advanced Features
- **Smart Filtering & Search**:
    - Filter by specific fields (e.g., find all countries using "EUR").
    - Full-text search across all data attributes.
- **Statistics Dashboard**: Real-time analytics showing:
    - Total country count.
    - Most common currencies.
    - Most widely spoken languages.
- **Bulk Import**: Capable of parsing and importing data from external source files (`countryInfo.txt`), intelligently skipping duplicates.
- **PDF Export**: Generates professional-grade PDF reports of the country list using the `fpdf2` library.
- **Sorting**: Flexible list views sorted by Name or ISO code.

## 3. Technical Architecture

The project follows a **Component-Based Architecture** to ensure maintainability and scalability.

### Directory Structure
```
country/
├── main.py                 # Application Entry Point
├── dados.json              # Data Storage
├── country_types.py        # Type Definitions & Validation
├── components/             # Core Logic Modules
│   ├── constants.py        # Configuration
│   ├── data_handler.py     # Data IO & CRUD
│   ├── menu_component.py   # UI & Interaction
│   ├── handlers/           # Feature Handlers
│   │   ├── country_handlers.py
│   │   ├── filter_handlers.py
│   │   ├── pdf_handlers.py
│   │   ├── import_handlers.py
│   │   └── analytics_handlers.py
```

### Key Design Decisions
1.  **Separation of Concerns**: Logic is split into distinct components. UI code (`menu_component`) is separate from data logic (`data_handler`), which is separate from feature sets (`handlers`).
2.  **Type Safety**: Utilizes Python `TypedDict` and type hinting throughout to ensure code reliability and better developer experience.
3.  **Graceful Error Handling**: The application handles invalid inputs, missing files, and interruptions (Ctrl+C) without crashing.
4.  **Centralized Configuration**: All file paths and constants are managed in `components/constants.py`.

## 4. How to Use

### Prerequisites
- Python 3.8+
- Dependencies: `fpdf2` (Install via `pip install fpdf2`)

### Running the Application
Execute the main script from the terminal:
```bash
python main.py
```

### Menu Options
1.  **List all countries**: View database. Options to sort and see details.
2.  **Add new country**: Step-by-step wizard to create a record.
3.  **Edit country**: Modify existing records by ISO code.
4.  **Delete country**: Remove records.
5.  **Filter countries**: Find specific subsets of data.
6.  **Search countries**: Global text search.
7.  **Export to PDF**: Generate `countries_report.pdf`.
8.  **Import from Source**: Bulk load data from text files.
9.  **Statistics**: View data insights.

## 5. Future Enhancements
- **GUI Interface**: Potential upgrade to a graphical interface (Tkinter/PyQt).
- **API Integration**: Fetching real-time country data from online APIs.
- **Database Support**: Migration to SQLite for larger datasets.
