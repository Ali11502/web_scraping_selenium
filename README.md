# Emirates Cargo Tracking Scraper README

## Overview

This script tracks cargo shipment details via the Emirates SkyCargo website using Selenium WebDriver. It collects and prints details such as the cargo type, journey information, and milestones.

## Prerequisites

Ensure you have the following installed:

1. **Python** (version 3.6 or later)
2. **Selenium** (Python package)
3. **ChromeDriver** (compatible with your installed version of Chrome browser)

### Install Selenium

```sh
pip install selenium
```

### Download ChromeDriver

Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's added to your system PATH.

## Usage

### Update the Tracking ID

Replace the `tracking_id` value with your actual tracking ID in the script:

```python
tracking_id = "17654016023"  # Replace with your actual tracking ID
```

### Running the Script

1. Save the script to a Python file, e.g., `track_cargo.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `track_cargo.py`.
4. Run the script:

```sh
python track_cargo.py
```

## Output

The script will print the following information:

1. **Basic Information**: Document number, cargo type, journey number, origin, and destination.
2. **Additional Data**: Pieces, gross weight, and other relevant details.
3. **Stops**: Number of stops in the journey.
4. **Milestones**: Detailed milestone information including status, dates, locations, and weights.