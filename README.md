# Selenium WebDriver E-Commerce Automation

A Python-based Selenium WebDriver automation framework for testing an end-to-end e-commerce purchase workflow using the [TutorialsNinja Demo Store](https://tutorialsninja.com/demo/).

The project follows the **Page Object Model (POM)** design pattern and uses external Excel test data to make the automation workflow structured, reusable, and maintainable.

## Overview

This project automates a typical customer purchase journey on an e-commerce web application:

**Login → Search Product → Select Product → Add to Cart → Update Quantity → Verify Cart → Capture Screenshots**

The framework is designed as a practical Selenium WebDriver capstone demonstrating browser automation, page-object-based test design, external test data handling, assertions, explicit waits, and execution evidence through screenshots.

## Features

- Browser automation using **Selenium WebDriver**
- **Python**-based test automation
- **Page Object Model (POM)** architecture
- Login automation
- Product search and selection
- Add-to-cart automation
- Cart quantity update
- Cart detail verification
- Explicit waits for improved synchronization
- Test data management using **Excel**
- Automated screenshot capture
- Pytest-based test execution
- Privacy-conscious handling of test credentials using `.gitignore`

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Automation programming language |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution and assertions |
| OpenPyXL | Reading Excel test data |
| Chrome | Test browser |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
selenium-capstone/
│
├── config/
│   └── config.json
│
├── pages/
│   ├── cart_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── search_page.py
│
├── test_data/
│   └── testdata.xlsx
│
├── tests/
│   └── test_selenium.py
│
├── utilities/
│   ├── excel_reader.py
│   └── screenshot.py
│
├── screenshots/
├── reports/
├── .gitignore
└── README.md
```

> `test_data/testdata.xlsx`, generated screenshots, reports, and the Python virtual environment are excluded from version control where appropriate.

## Automation Workflow

### 1. Launch Browser

The test initializes a Chrome WebDriver instance and navigates to the TutorialsNinja Demo Store.

### 2. Login

The automation opens the My Account menu, navigates to the login page, and enters the credentials provided through the external test-data file.

### 3. Search Product

The required product is read from Excel and searched through the website's search functionality.

### 4. Select Product

The automation identifies and opens the requested product from the search results.

### 5. Add to Cart

The selected product is added to the shopping cart.

### 6. Update Quantity

The quantity in the cart is updated using the value supplied through the test-data file.

### 7. Verify Cart

The test verifies that:

- The expected product is present in the cart.
- The cart quantity matches the expected quantity.

### 8. Capture Screenshots

Screenshots are captured at important stages of execution, including:

- Successful login
- Search results
- Product page
- Cart details

## Test Data

Test data is maintained separately from the test logic using an Excel workbook.

Example structure:

| email | password | product | quantity |
|---|---|---|---:|
| Test account | Test password | iPhone | 2 |

Actual credentials are intentionally excluded from the GitHub repository through `.gitignore`.

## Installation

### Prerequisites

Make sure the following are installed:

- Python 3
- Google Chrome
- Git

### Clone the Repository

```bash
git clone https://github.com/Devi2006/selenium-capstone.git
cd selenium-capstone
```

### Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install selenium pytest openpyxl pytest-html
```

## Test Data Setup

The actual test-data Excel file is intentionally excluded from version control.

Create:

```text
test_data/testdata.xlsx
```

with a worksheet named:

```text
LoginData
```

and the following columns:

```text
email | password | product | quantity
```

Enter credentials for a valid test account and the required product information.

## Running the Test

From the project root:

```bash
python -m pytest tests/test_selenium.py -v
```

The test will launch Chrome and execute the complete purchase workflow.

## Screenshots

Execution screenshots are automatically stored in:

```text
screenshots/
```

The generated files are excluded from GitHub through `.gitignore`.

## Design Approach

The project uses the **Page Object Model**, separating page-specific interactions from the test workflow.

### Page Objects

- `HomePage` — account navigation and product search
- `LoginPage` — login form interactions
- `SearchPage` — product selection and cart addition
- `CartPage` — cart navigation, product verification, and quantity updates

### Utilities

- `excel_reader.py` — reads test data from Excel
- `screenshot.py` — captures timestamped screenshots during execution

This separation improves readability and makes the automation easier to maintain when individual page elements or workflows change.

## Test Coverage

| Test Scenario | Status |
|---|---|
| Launch application | ✓ |
| Login | ✓ |
| Search product | ✓ |
| Select product | ✓ |
| Add product to cart | ✓ |
| Update quantity | ✓ |
| Verify product in cart | ✓ |
| Verify quantity | ✓ |
| Capture screenshots | ✓ |
| External Excel test data | ✓ |

## Security & Privacy

This repository deliberately excludes local and potentially sensitive files, including:

```text
venv/
test_data/testdata.xlsx
screenshots/
reports/
.env
.env.*
```

Test credentials should never be committed to a public repository.

## Future Enhancements

Potential improvements include:

- Parameterized testing with multiple products and accounts
- JSON-based test-data support
- Additional negative test scenarios
- Automated HTML execution reports
- Improved alert/popup handling
- Cross-browser execution
- CI/CD integration using GitHub Actions
- More comprehensive assertions for cart totals and product details

## Author

**Devi Prasad Chakraborty**

B.Tech — Computer Science & Technology  
Institute of Engineering & Management, Kolkata

GitHub: [Devi2006](https://github.com/Devi2006)

---

### Disclaimer

This project uses the publicly available TutorialsNinja Demo Store for educational and automation-testing purposes.
