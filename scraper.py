from selenium import webdriver
from pandas import DataFrame, set_option, to_datetime
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


target_url = 'https://southeastasiainfra.com/category/urban-infrastructure/'
driver = webdriver.Chrome()


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
results = DataFrame(articles)
results.time = to_datetime(results.time)
one_week_ago = (datetime.today() - timedelta(days=7)
                ).replace(hour=0, minute=0, second=0)
results = results[results.time >= one_week_ago]  # Articles in the past 7 days
print('Parsing process completed!')

# saving_path = input('Please enter the ')

print('Start exporting the results...')

print(f'Data exporting process completed!\nPlease find the results from this path:')

input('Press enter to quit...')
driver.quit()
