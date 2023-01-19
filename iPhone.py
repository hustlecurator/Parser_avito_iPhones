from selenium import webdriver
from selenium.webdriver.common.by import By
import json

options = webdriver.ChromeOptions()

# options.add_argument('user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')

options.add_argument('--headless')

browser = webdriver.Chrome(options=options)

url = 'http://www.avito.ru/voronezh/telefony/mobilnye_telefony/apple-ASgBAgICAkS0wA3OqzmwwQ2I_Dc?cd=1&q=iphone+13'

try:
    browser.get(url)

    blocks = browser.find_elements(By.CLASS_NAME, 'iva-item-root-_lk9K')

    all_phones_dict = {}

    for block in blocks:
        title = block.find_element(By.CLASS_NAME, 'title-root-zZCwT').text.strip()
        price = block.find_element(By.CLASS_NAME, 'price-text-_YGDY').text
        date = block.find_element(By.CLASS_NAME, 'date-text-KmWDf').text
        char = block.find_element(By.CLASS_NAME, 'iva-item-text-Ge6dR').text
        site = block.find_element(By.CLASS_NAME, 'link-link-MbQDP').get_attribute('href')
        who = block.find_element(By.XPATH, '//div[@data-marker="item-line"]').text
        # print(f"{title} = {char} +  //  + {price} +  //  + {time} +  //  + {url} +  //  + {who}")
        all_phones_dict[title] = char + ' \\ ' + price + ' \\ ' + date + ' \\ ' + site + ' \\ ' + who

    with open('all_phones_dict.json', 'w', encoding='UTF-8') as file:
        json.dump(all_phones_dict, file, indent=4, ensure_ascii=False)


except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
