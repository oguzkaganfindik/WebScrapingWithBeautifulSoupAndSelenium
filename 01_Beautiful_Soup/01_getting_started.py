#######################
# Getting Started
#######################
# pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
            </html>

"""

soup = BeautifulSoup(html, "html.parser")

title = soup.title
type(title)
title.text
title.string

print(soup.prettify())

soup.ul
soup.li

ul = soup.ul
type(ul)
ul.li

html = """
        <!DOCTYPE html><html><head><title>Example HTML</title></head><body><h1>Hello, World!</h1><p>A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
            </html>

"""

soup = BeautifulSoup(html, "html.parser")

title = soup.title
type(title)
title.li

soup.ul.li
