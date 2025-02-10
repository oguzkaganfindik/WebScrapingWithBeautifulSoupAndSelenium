#####################################################
# Web Kazıma ile Rakip ve Fiyat Analizi
#####################################################

#####################################################
# İş Problemi
#####################################################

# Online kitap satışı yapan bir şirket, “Seyahat” ve “Kurgu Dışı” kategorilerinde
# az satış yaptığını tespit ediyor. Bu sebeple şirketin, rakip firmanın kazınması izin verilen
# https://books.toscrape.com/ adlı web sitesinden “Travel” ve “Nonfiction” kategorisindeki
# kitaplara ait bilgileri alıp, rakip ve fiyat analizi yapmaya ihtiyacı var. Şirket sizden
# bu kategorilerdeki her kitaba ait detay sayfasında bulunan bilgileri almanızı bekliyor.

#####################################################
# Proje Görevleri
#####################################################

# Projede İstenilen Akış
# ------------------------------------------
# "Travel" ve "Nonfiction" kategorilerine ait kitapların yer aldığı sayfa linkleri alınmalı.
# Sonrasında bir kategoriye ait tüm kitapların detay sayfalarının linkleri alındıktan sonra
# o kitapların detay bilgileri kazınmalı ve diğer kategoriye geçilmeli.

#####################################################################
# Görev 1: Tarayıcıyı Konfigüre Etme ve Başlatma
#####################################################################

# 1. Selenium'un Webdriver sınıfını kullanarak bir adet options adında ChromeOptions tanımlayınız.

from selenium import webdriver
from spyder.app.restart import SLEEP_TIME

options = webdriver.ChromeOptions()

# 2. Tanımladığınız options’a tam ekran özelliği ekleyiniz.

options.add_argument("--start-maximized")

# 3. Bir önceki adımlarda hazırladığınız options’ı da kullanarak bir adet driver adında Chrome tarayıcısı oluşturunuz.

driver = webdriver.Chrome(options)

#####################################################################
# Görev 2: Ana Sayfanın İncelenmesi ve Kazınması
#####################################################################

# 1. Ana Sayfayı driver ile açınız ve inceleyiniz.

import time
SLEEP_TIME = 2

driver.get("https://books.toscrape.com/")
time.sleep(SLEEP_TIME)

# 2. "Travel" ile "Nonfiction" kategori sayfalarının linklerini tutan elementleri tek seferde bulan XPath sorgusunu yazınız.

category_elements_xpath = "//a[contains(text(),'Travel') or contains(text(),'Nonfiction')]"

# 3. XPath sorgusu ile yakaladığınız elementleri driver'ı kullanarak bulunuz ve kategori detay linklerini kazıyınız.

from selenium.webdriver.common.by import By
category_elements = driver.find_elements(By.XPATH, category_elements_xpath)

category_urls = [element.get_attribute("href") for element in category_elements]
print(category_urls)

#####################################################################
# GÖREV 3: Kategori Sayfasının İncelenmesi ve Kazınması
#####################################################################
# 1. Herhangi bir detay sayfasına girip o sayfadaki kitapların detay linkini tutan elementleri yakalayan XPath sorgusunu yazınız.

driver.get(category_urls[0])
time.sleep(SLEEP_TIME)
book_elements_xpath = "//div[@class='image_container']//a"

# 2. driver ile XPath sorgusunu kullanarak elementleri yakalayınız ve detay linklerini çıkarınız.

book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
book_urls = [element.get_attribute("href") for element in book_elements]
print(book_urls)
print(len(book_urls))

# 3. Sayfalandırma (Pagination) için butonlara tıklamak yerine sayfa linkini manipüle ediniz.
# İpucu: (Sayfa değiştikçe url'de ne değişiyor gözlemleyiniz)

MAX_PAGINATION = 3
url = category_urls[1]
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i == 1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)

    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))

# 4. Sayfalandırmanın sonuna geldiğinizi anlamak adına kategorinin 999. sayfasına giderek karşınıza çıkan sayfayı inceleyiniz.
#   İpucu: (..../category/books/nonfiction_13/page-999.html)
#   Dikkat: (..../category/books/travel_2/page-1.html ????????)


# 5. Bir önceki adımdaki incelemenin sonucunda sayfalandırmada sonsuz döngüye girmemek adına kontrol kullanınız.
#   İpucu: (text'inde 404 içeren bir h1 var mı?) veya (if not book_elements) ya da (len(book_elements) <= 0)

MAX_PAGINATION = 3
url = category_urls[1]
book_urls = []
for i in range(1, MAX_PAGINATION):
    update_url = url if i == 1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements = driver.find_elements(By.XPATH, book_elements_xpath)
    if not book_elements:
        break
    temp_urls = [element.get_attribute("href") for element in book_elements]
    book_urls.extend(temp_urls)

print(book_urls)
print(len(book_urls))

#####################################################################
# GÖREV 4: Ürün Detay Sayfasının Kazınması
#####################################################################

# 1. Herhangi bir ürünün detay sayfasına girip class attribute'ı content olan div elementini yakalayınız.

driver.get(book_urls[0])
time.sleep(SLEEP_TIME)
content_div = driver.find_elements(By.XPATH, "//div[@class='content']")

# 2. Yakaladığınız divin html'ini alınız ve inner_html adlı değişkene atayınız.

inner_html = content_div[0].get_attribute("innerHTML")

# 3. inner_html ile soup objesi oluşturunuz.

from bs4 import BeautifulSoup
soup = BeautifulSoup(inner_html, "html.parser")

# 4. Oluşturduğunuz soup objesi ile şu bilgileri kazıyınız:
# - Kitap Adı,

name_elem = soup.find("h1")
book_name = name_elem.text

# - Kitap Fiyatı,

price_elem = soup.find("p",attrs={"class": "price_color"})
book_price = price_elem.text

# - Kitap Yıldız Sayısı,
# İpucu: (regex = re.compile('^star-rating '))

import re
regex = re.compile('^star-rating ')
star_elem = soup.find("p", attrs={"class":regex})
print(star_elem)
book_star_count = star_elem["class"][-1]

# - Kitap Açıklaması,

desc_elem = soup.find("div", attrs={"id": "product_description"}).find_next_sibling()
book_desc = desc_elem.text

# - Product Information Başlığı altında kalan tablodaki bilgiler.

product_info = {}
table_rows = soup.find("table").find_all("tr")
for row in table_rows:
    key = row.find("th").text
    value = row.find("td").text
    product_info[key] = value

#####################################################################
# GÖREV 5: Fonksiyonlaştırma ve Tüm Süreci Otomatize Etme
#####################################################################
# 1. İşlemleri fonksiyonlaştırınız. Örnek olarak: def get_product_detail(driver):   |    def get_category_detail_urls(driver)

def get_book_detail(driver, url):
    """Gets book data from given book detail page url"""
    driver.get(url)
    time.sleep(SLEEP_TIME)
    content_div = driver.find_elements(By.XPATH, "//div[@class='content']")

    inner_html = content_div[0].get_attribute("innerHTML")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(inner_html, "html.parser")

    name_elem = soup.find("h1")
    book_name = name_elem.text

    price_elem = soup.find("p", attrs={"class": "price_color"})
    book_price = price_elem.text

    import re
    regex = re.compile('^star-rating ')
    star_elem = soup.find("p", attrs={"class": regex})
    book_star_count = star_elem["class"][-1]

    desc_elem = soup.find("div", attrs={"id": "product_description"}).find_next_sibling()
    book_desc = desc_elem.text

    product_info = {}
    table_rows = soup.find("table").find_all("tr")
    for row in table_rows:
        key = row.find("th").text
        value = row.find("td").text
        product_info[key] = value

    return {'book_name': book_name, 'book_price:': book_price, 'book_star_count': book_star_count,
            'book_desc': book_desc, **product_info}

def get_book_urls(driver, url):
    """Gets book urls from given category detail page url"""
    MAX_PAGINATION = 3

    book_urls = []
    book_elements_xpath = "//div[@class='image_container']//a"

    for i in range(1, MAX_PAGINATION):
        update_url = url if i == 1 else url.replace("index", f"page-{i}")
        driver.get(update_url)
        time.sleep(SLEEP_TIME)
        book_elements = driver.find_elements(By.XPATH, book_elements_xpath)

        #Controller of pagination
        if not book_elements:
            break
        temp_urls = [element.get_attribute("href") for element in book_elements]
        book_urls.extend(temp_urls)

    return book_urls

def get_travel_and_nonfiction_category_urls(driver, url):
    """Gets category urls from given homepage url"""
    driver.get(url)
    time.sleep(SLEEP_TIME)

    category_elements_xpath = "//a[contains(text(), 'Travel') or contains(text(),'Nonfiction')]"

    category_elements = driver.find_elements(By.XPATH, category_elements_xpath)
    category_urls = [element.get_attribute("href") for element in category_elements]

    return category_urls

def initialize_driver():
    """Initializes driver with maximized option"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized");
    driver = webdriver.Chrome(options)
    return  driver

# 2. Süreci otomatize ederek, Travel ile Nonfiction kategorilerine ait tüm kitapların detaylarını alacak şekilde kodu düzenleyiniz.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

SLEEP_TIME = 0.05

def main():
    BASE_URL = "https://books.toscrape.com/"
    driver = initialize_driver()
    category_urls = get_travel_and_nonfiction_category_urls(driver, BASE_URL)
    data = []
    for cat_url in category_urls:
        book_urls = get_book_urls(driver, cat_url)
        for book_url in book_urls:
            book_data = get_book_detail(driver, book_url)
            book_data["cat_url"] = cat_url
            data.append(book_data)

    len(data)

    # Optional
    import pandas as pd
    pd.set_option("display.max_columns", None)
    pd.set_option('display.max_colwidth', 40)
    pd.set_option("display.width", 2000)
    df = pd.DataFrame(data)

    return df

df = main()
print(df.head())
print(df.shape)