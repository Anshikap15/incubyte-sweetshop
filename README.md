# Incubyte - Sweet Shop Management System 

This repository contains my solution to the **Incubyte Assessment Problem Statement: AI Kata Sweet Shop Management System.

## Features
- Add new sweets to the shop
- Restock existing sweets
- Sell sweets and calculate revenue
- Maintain inventory levels

## Files
- `sweetshop.py` → main implementation
- `test_sweetshop.py` → unit tests using pytest
- `requirements.txt` → dependencies
- `incubyte.pdf` → original problem statement

## How to run tests locally
```bash
# 1. Create a virtual environment
python3 -m venv venv
# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
pytest -q
