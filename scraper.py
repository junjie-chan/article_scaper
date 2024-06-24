from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pandas import DataFrame

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 运行无头模式

target_url = 'https://southeastasiainfra.com/category/urban-infrastructure/'
driver = webdriver.Chrome(options=chrome_options)


print(f'Scraping from {target_url}...')
driver.get(target_url)
print('Scraping process completed!')

print('Start parsing article details...')
articles = []
li_tags = driver.find_elements(By.XPATH, '//ul[@class="widget_list"]/li')
for li in li_tags:
    link = li.find_element(By.XPATH, './div/a').get_attribute('href')
    title = li.find_element(By.XPATH, './div/a').text
    time = li.find_element(By.XPATH, './div/div/span[@class="updated"]').text
    country = li.find_element(By.XPATH, './div/div/a[last()]').text
    articles.append({'title': title, 'country': country,
                    'time': time, 'link': link})
    # print(f'title: {title}\nlink: {link}\ntime: {time}\ncountry: {country}\n\n')
print('Parsing process completed!')


print('Start exporting the results...')
DataFrame(articles).to_excel()
print(f'Data exporting process completed!\nPlease find the results from this path:')

input('Press enter to quit...')
driver.quit()
