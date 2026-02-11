# Email Domain Migrator

**Author:** Denis Naumov  
**Location:** Cologne, Germany

A production-grade Python CLI utility designed to safely and efficiently migrate email domains within CSV files using Regular Expressions (RegEx). 

This project demonstrates a robust ETL (Extract, Transform, Load) approach: it processes data via a memory-efficient stream, ensures the original source files are never mutated, and includes automated test data generation for seamless development.

---

## 🚀 Features

- **Memory Efficient (Streaming):** Processes CSV files line-by-line (O(1) memory complexity). It can handle massive datasets (e.g., gigabytes of data) without causing `MemoryError`.
- **Non-Destructive:** Safely reads from the input file and writes to a separate output file. Your original client data is protected and never overwritten.
- **CLI Interface:** Fully configurable via command-line arguments using Python's `argparse`. No hardcoded paths.
- **Smart Data Generation:** Integrated with `Faker` to automatically generate realistic, mixed-domain CSV datasets for safe local testing.
- **Bulletproof RegEx:** Utilizes `re.escape` and precise anchors (`$`) to prevent false positives and ensure strict domain matching.
- **Unit Tested:** Core logic is thoroughly tested using the `pytest` framework.

---

## 📁 Project Structure

```text
email-domain-migrator/
│
├── README.md
├── .gitignore
├── requirements.txt
├── main.py                     # CLI entry point
│
├── data/
│   ├── user_emails.csv         # Source data (read-only)
│   └── updated_user_emails.csv # Migration output
│
├── src/
│   ├── __init__.py
│   ├── generator.py            # Faker-based mock data generator
│   └── migrator.py             # Core RegEx and CSV streaming logic
│
└── tests/
    ├── __init__.py
    └── test_migrator.py        # Pytest unit tests for RegEx matching

```

---

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone [https://github.com/DenisNaumov7777/email-domain-migrator.git](https://github.com/DenisNaumov7777/email-domain-migrator.git)
cd email-domain-migrator

```


2. **Set up a virtual environment (Recommended):**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```



---

## 💻 Usage

The tool is completely driven by the Command Line Interface.

### 1. Standard Migration

To migrate emails from an existing CSV file:

```bash
python main.py --input data/clients.csv --output data/updated_clients.csv --old-domain abc.edu --new-domain xyz.edu

```

### 2. Generate Test Data

If you don't have a CSV file and want to test the tool, you can automatically generate a mock dataset with 50 rows:

```bash
python main.py --generate --count 50

```

*Note: This will safely generate `data/user_emails.csv` and immediately perform the migration to `data/updated_user_emails.csv`.*

### 3. View Help Menu

To see all available arguments and default values:

```bash
python main.py --help

```

---

## 🧪 Testing

This project uses `pytest` to ensure the integrity of the Regular Expressions used for domain matching and replacement.

To run the test suite, simply execute:

```bash
pytest tests/ -v

```

---

## 📜 License

Distributed under the Apache License 2.0. See `LICENSE` for more information.



