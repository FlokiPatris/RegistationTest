# RegistationTest

This repository contains an end-to-end testing suite for a registration form, leveraging [Pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/).

## Prerequisites

Before proceeding, ensure you have installed:

- **Python 3.9+**
- **Node.js** (required by Playwright)
- **pip**

## Instalation steps

### 1. Cloning the Repository

Open a terminal and run:

git clone https://github.com/FlokiPatris/RegistationTest.git <br>
cd RegistationTest

### 2. Set Up a Virtual Environment (optional but recommended)

python -m venv venv

On Windows: <br> venv\Scripts\activate <br> <br>
On macOS/Linux: <br> source venv/bin/activate

### 3. Install Python Dependencies
python -m pip install -r requirements.txt

### 4. Install Playwright Browsers
playwright install

### 5. Run the Tests
pytest --verbose
