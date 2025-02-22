# Scraping Project 3

## Description
This project scrapes data from the [Quotes to Scrape](https://quotes.toscrape.com/) website and saves the extracted information in a `.csv` file. The goal is to demonstrate a simple and efficient approach to collecting and structuring data using Python and the `BeautifulSoup` library.

## Technologies Used
- Python 3.11
- Requests
- BeautifulSoup4
- csv

## Features
- Extraction of quotes, authors, and tags from the website.
- Saving the data into a `.csv` file.
- Modular and easy-to-understand code.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/scraping_project_3.git
   ```
2. Navigate to the project directory:
   ```bash
   cd scraping_project_3
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## Project Structure
```
 scraping_project_3/
 |-- main.py  # Main script for data scraping
 |-- requirements.txt  # Project dependencies
 |-- README.md  # Project documentation
 |-- quotes.csv  # Generated file with scraped data
```

## Example Output (`quotes.csv`)
```
"Phrase","Author","Tags"
"Life is what happens when you're busy making other plans.","John Lennon","life,inspiration"
"If you tell the truth, you don't have to remember anything.","Mark Twain","truth,honesty"
...
```

## Contribution
If you'd like to contribute, feel free to open an issue or submit a pull request!

## License
This project is licensed under the MIT License.

