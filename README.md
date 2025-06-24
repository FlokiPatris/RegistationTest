# RegistationTest

This repository contains an end-to-end testing suite for a registration form, leveraging [Pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/). 
It implements the Page Object Model (POM) pattern so that tests remain clean and maintainable.

## Prerequisites

Before proceeding, ensure you have installed:

- **Python 3.9+**
- **Node.js** (required by Playwright)
- **pip**

## Instalation steps

### 1. Cloning the Repository

Open a terminal and run:

```bash
git clone https://github.com/FlokiPatris/RegistationTest.git
cd RegistationTest

### 2. Set Up a Virtual Environment (optional but recommended)
python -m venv venv

#### On Windows
venv\Scripts\activate
#### On macOS/Linux
source venv/bin/activate

### 3. Install Python Dependencies
python -m pip install -r requirements.txt

### 4. Install Playwright Browsers
playwright install

### 5. Run the Tests
pytest --verbose
