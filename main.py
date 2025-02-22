from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}

i = 0
list_of_dicts = []

# Searching for text blocks.
while True:
    i += 1

    response = requests.get(
        f'https://quotes.toscrape.com/page/{i}/', headers=headers)

    parser_html = BeautifulSoup(response.text, 'html.parser')
    breakpoint = parser_html.find_all('div', class_='col-md-8')

    if 'No quotes found!' in breakpoint[1].text:
        break

    phrases = parser_html.find_all('span', class_='text')
    authors = parser_html.find_all('small', class_='author')
    tags = parser_html.find_all('meta', class_='keywords')

    # Passing block by block.
    for phrase, author, tag in zip(phrases, authors, tags):

        quote = dict(
            Phrase=phrase.text,
            Author=author.text,
            Tags=tag.attrs['content'],  # type: ignore
        )
        list_of_dicts.append(quote)

# Opening and saving the block information in a .csv file.
with open('quotes.csv', 'w', newline='', encoding='utf8') as file:
    names_columns = list_of_dicts[0].keys()
    writer = csv.DictWriter(
        file,
        names_columns,
    )
    writer.writeheader()
    writer.writerows(list_of_dicts)
