# Selenium Web Scraper for Emirates Cargo Tracking

This project is a Selenium web scraper designed to extract cargo tracking information from the Emirates SkyCargo tracking website. The script automates the process of entering a tracking ID, navigating the website, and extracting relevant tracking details, including milestones of the cargo journey.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Setup

1. **Install Selenium:**
   ```bash
   pip install selenium
   ```

2. **Download Chrome WebDriver:**
   - Make sure to download the Chrome WebDriver that matches your version of Google Chrome.
   - You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).
   - Place the WebDriver executable in a directory included in your system's PATH or specify the path in the script.

## Usage

1. **Initialize WebDriver and Open Website:**
   The script initializes the Chrome WebDriver and navigates to the Emirates SkyCargo tracking page.

2. **Enter Tracking ID:**
   The script inputs the tracking ID into the specified field and submits the form.

3. **Extract Cargo Details:**
   - The script extracts various cargo details, such as document number, cargo type, journey number, origin, and destination.
   - It gathers additional information like pieces, gross weight, and other cargo metrics.

4. **Extract Milestones:**
   - The script retrieves milestones related to the cargo's journey, including status updates, dates, locations, and other relevant details.

5. **Output Data:**
   The extracted data is printed in a structured format, showing all relevant information about the cargo tracking.

## Data Structure

### Basic Information
- **Document Number**
- **Cargo Type**
- **Journey Number**
- **Origin**
- **Destination**

### Additional Details
- **Pieces**
- **Gross Weight**
- **Other Cargo Metrics**

### Milestones
- **Status**
- **Status Date**
- **Pieces**
- **Gross Weight**
- **Status Location**
- **Status Time**
- **Source**
- **Destination**
- **Planned Time at Source**
- **Planned Time at Destination**
- **Planned Date at Source**
- **Planned Date at Destination**

## Notes

- Ensure that the Chrome WebDriver version matches your installed version of Google Chrome.
- Adjust the `implicitly_wait` and `time.sleep` durations as needed based on your internet connection and the website's response time.
