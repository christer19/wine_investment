from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

AGENT = user_agent_list[0] #random.choice(user_agent_list)

CRITICS = ['Robert Parker The Wine Advocate', 'James Suckling', 'Vinous Antonio Galloni', 'Neal Martin', 'Jancis Robinson']


def get_html_source(wine_name):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    browser=webdriver.Chrome(options=options)
    browser.get('https://www.wine-searcher.com/find/{}/1/uk/-/u?Xbottle_size=all&Xprice_set=CUR#t2'.format(wine_name))

    time.sleep(4)

    html = browser.page_source
    browser.quit()
    return html

def parse_html(html):
    soup = bs(html, features="html.parser")
    return soup

# def price_chrome_parser(wine_name, year):
# 	import time
# 	caps = Options()
# 	caps.page_load_strategy = "eager"
# 	caps.add_argument(f'user-agent={AGENT}')
# 	browser=webdriver.Chrome(options=caps)
# 	wait = WebDriverWait(browser, 3)
# 	URL = f"https://www.wine-searcher.com/find/{wine_name}/{year}?Xsavecurrency=Y&Xlist_format=&Xbottle_size=all&Xprice_set=CUR&Xprice_min=&Xprice_max=&Xshow_favourite=N&Xcurrencycode=GBP&Xsecondarycurrencycode=GBP".format(wine_name, year)
# 	browser.get(URL)
# 	time.sleep(0.3)
# # 	wait.until(
# #     EC.presence_of_element_located((By.XPATH, '<meta itemprop="price"'))
# # )
# 	html = browser.page_source
# 	browser.quit()
# 	return html

# def get_price_parser(html):
# 	soup = bs(html, features="html.parser")
# 	# price_tag = soup.find('meta', {'itemprop':'price'})
# 	price_tag = soup.find(itemprop='price')
# 	price_tag2 = price_tag.get_text()
# 	# return price_tag['content']
# 	return float(price_tag2.split()[-1].replace(',',''))

def get_grape(wine_name):
    html = get_html_source(wine_name)
    soup = parse_html(html)
    grape = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    grape_type = None
    for i in grape:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'variety':
                    grape_type = j.text
            except Exception:
                pass

    return grape_type

def get_region(wine_name):
    html = get_html_source(wine_name)
    soup = parse_html(html)
    find = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    region = []
    for i in find:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'region':
                    region.append(j.text)
            except Exception:
                pass
    return ' '.join(region)

def get_colour(wine_name):
    html = get_html_source(wine_name)
    soup = parse_html(html)
    find = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    colour = None
    for i in find:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'style':
                    colour = j.text
            except Exception:
                pass
    return colour



def get_country(wine_name):
    # html = get_html_source(wine_name)
    # soup = parse_html(html)
    return None


def parser_main(wine_name):
    html = get_html_source(wine_name)
    soup = parse_html(html)
    score = [i.text for i in soup.findAll('span', {'class': 'crt-score-s'})]
    critic_result_dict = {}
    result = []
    find_colour = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    colour = None

    for i in find_colour:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'Style' or j.get('title').split()[-1] == 'style':
                    colour = j.text
            except Exception:
                pass
    find_region = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    region = []
    for i in find_region:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'region':
                    region.append(j.text)
            except Exception:
                pass
    region = ' '.join(region)

    grape = soup.findAll('span', {'class':"dtlbl sidepanel-text"})
    grape_type = None
    for i in grape:
        for j in i.findAll('a', href=True):
            try:
                if j.get('title').split()[-1] == 'variety':
                    grape_type = j.text
            except Exception:
                pass

    for i, score in zip(soup.findAll('div', {'class': 'crt-info-col2-s'}), score):
        for year in i.find('div', {'class': 'belongs-color'}):
            pass
        for name in i.find('span', {'itemprop': 'name'}):
            pass
        year_val = year.split()[0]
        # name_val = re.compile('')
        # name_val = ' '.join(name.split()[0:2])
        name_val = name
        if name_val in CRITICS:
            critic_result_dict['critic'] = name_val
            critic_result_dict['year'] = year_val
            critic_result_dict['score'] = score
            result.append(critic_result_dict.copy())
    result.sort(key= lambda x: x['year'], reverse=True)
    types = []
    types.append({'grape':grape_type, 'region': region, 'colour': colour})
    return [result, types]
