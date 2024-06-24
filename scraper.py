from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 配置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 运行无头模式

chrome_driver_path = r'./chrome-win64/chrome.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome()
driver.get('https://southeastasiainfra.com/category/urban-infrastructure/')

li_tags = driver.find_elements(By.XPATH, '//ul[@class="widget_list"]/li')
for li in li_tags:
    link = li.find_element(By.XPATH, './div/a').get_attribute('href')
    title = li.find_element(By.XPATH, './div/a').text
    time = li.find_element(By.XPATH, './div/div/span[@class="updated"]').text
    country = li.find_element(By.XPATH, './div/div/a[last()]').text
    print(f'title: {title}\nlink: {link}\ntime: {time}\ncountry: {country}\n\n')

input('Press enter to quit...')
driver.quit()
