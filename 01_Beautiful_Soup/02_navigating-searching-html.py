#################################
# Navigating and Searching HTML
#################################

from bs4 import BeautifulSoup

html = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Example HTML</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p id="paragraph" >A simple HTML page for testing web scraping with BeautifulSoup.</p>
                <a class='link' href='www.miuul.com' target='blank' aria-label='Miuul (Opens Miuul Page)'>Click</a>
                <li>Outsider</li>
                <ul>
                    <li class="list-item">Item 1</li>
                    <li class="list-item">Item 2</li>
                </ul>
                <li>Outsider 2</li>
            </body>
            </html>
"""

soup = BeautifulSoup(html, "html.parser")

soup.a
soup.find("a", attrs={"class": "link", "target": "blank"})

soup.find("li")
soup.find_all("li")

ul = soup.find("ul")

ul.find_all("li")

li_elements = soup.find_all("li", attrs={"class": "list-item"})
li_elements
li_elements[-1]
