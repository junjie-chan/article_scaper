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


input('Press enter to quit...')
driver.quit()
