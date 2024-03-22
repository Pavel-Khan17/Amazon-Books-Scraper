# Audible Best Sellers Web Scraper

## Description

This Python script scrapes the Amazon Audible Best Sellers website to extract information about the best-selling audiobooks across various categories. It retrieves details such as the book name, author, rating, number of ratings, price, and book image link. The data is then saved to a CSV file and optionally converted to an Excel file for further analysis or visualization.

## Features

- Scrapes Amazon Audible Best Sellers website for audiobook information.
- Extracts details such as book name, author, rating, number of ratings, price, and book image link.
- Handles rate limiting by adding delays between requests.
- Checks for duplicate entries to avoid writing redundant data to the CSV file.
- Supports converting the CSV file to an Excel file for easy data manipulation.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Pavel-Khan17/Amazon-Books-Scraper.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script `audible_best_sellers_scraper.py`:

    ```bash
    python audible_best_sellers_scraper.py
    ```

2. Once the script finishes execution, the data will be saved to a CSV file named `audible_best_sellers.csv` in the same directory.
3. Optionally, you can convert the CSV file to an Excel file using the provided script:

    ```bash
    python convert_to_excel.py
    ```

4. The Excel file named `audible_best_sellers.xlsx` will be generated containing the scraped data.

## Configuration

- You can adjust the delay between requests and other parameters directly in the script `audible_best_sellers_scraper.py`.
- Optionally, you can modify the headers and selectors in the script to adapt to changes in the website's structure.

## Acknowledgments

- This project was inspired by the need to collect data for study and practice purposes.
  
## License

- All Rights reserved by Pavel Khan
