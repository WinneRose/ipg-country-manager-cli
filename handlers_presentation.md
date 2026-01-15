# Country Management Application: Handlers Components
## Technical Overview & Architecture

---

## 1. Introduction to Handlers

**What are Handlers?**
The `handlers` component acts as the **Controller** layer in our application's architecture. It serves as the bridge between:
- **Presentation Layer** (`menu_component`): Reads user input and displays output.
- **Data Layer** (`data_handler`, `importer_component`, `pdf_component`): Manages data storage and core business logic.

**Key Responsibilities:**
- Orchestrating the flow for specific user actions (e.g., "Add Country").
- Validating user input before passing it to the data layer.
- Determining which UI messages to show based on operation success or failure.

---

## 2. Core Country Operations
**File:** `country_handlers.py`

This module manages the primary CRUD (Create, Read, Update, Delete) lifecycle of country data.

### Key Functions
| Function | Description |
| :--- | :--- |
| `handle_list_countries()` | Retrieves the list of countries, offers sorting options (ISO or Name), and optionally triggers a detailed view. |
| `handle_add_country()` | Orchestrates the addition of a new country: gets input, validates it, asks for confirmation, and saves it. |
| `handle_edit_country()` | Looks up a country by ISO, displays current data, accepts partial updates, validates, and saves changes. |
| `handle_delete_country()` | Finds a country by ISO, shows details to confirm identity, and executes deletion upon confirmation. |

---

## 3. Search & Filter
**File:** `filter_handlers.py`

Handles the logic for narrowing down the dataset based on specific criteria.

### Key Functions
| Function | Description |
| :--- | :--- |
| `handle_filter_countries()` | interactively asks the user to select a field (e.g., Currency, Region) and a value, then displays matches. |
| `handle_search_countries()` | Takes a generic search query string and finds matches across relevant fields. |

---

## 4. Analytics & Statistics
**File:** `analytics_handlers.py`

Provides high-level insights into the country dataset.

### Key Functions
- **`handle_show_statistics()`**: Compiles and displays a dashboard containing:
    - Total number of countries.
    - Top 5 most common currencies.
    - Top 5 most common languages.

---

## 5. Data Import
**File:** `import_handlers.py`

Manages the ingestion of external data.

### Key Functions
- **`handle_import_data()`**:
    - Reads from `countryInfo.txt` using the importer component.
    - Validates parsed data.
    - Handles duplicates (skips existing ISO codes).
    - performs a batch update to save valid new entries.
    - Reports success/failure counts (Added vs. Skipped).

---

## 6. PDF Export
**File:** `pdf_handlers.py`

Handles the generation of reports.

### Key Functions
- **`handle_export_pdf()`**: It gets the current list of countries (potentially filtered in a future version) and triggers the PDF generator to create a report file (defaulting to `countries_report.pdf`).

---

## Summary

The **Handlers** layer is crucial for keeping our code clean and modular. By separating the "flow" of an action from the "details" of how to print to the screen or save to a file, we ensure the application is easier to test and maintain.
