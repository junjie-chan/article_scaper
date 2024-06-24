from os.path import join
from selenium import webdriver
from datetime import datetime, timedelta
from pandas import DataFrame, to_datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
    country = ''.join([i.text for i in li.find_elements(
        By.XPATH, './div/div//a')]).replace('Key Developments', '')
    articles.append({'title': title, 'country': country,
                    'time': time, 'link': link})
    # print(f'title: {title}\nlink: {link}\ntime: {time}\ncountry: {country}\n\n')
driver.quit()
results = DataFrame(articles)
results.time = to_datetime(results.time)
one_week_ago = (datetime.today() - timedelta(days=7)
                ).replace(hour=0, minute=0, second=0)
results = results[results.time >= one_week_ago]  # Articles in the past 7 days
results.time = results.time.apply(lambda x: x.strftime("%Y-%m-%d"))
print('Parsing process completed!')

if not results.empty:
    saving_path = join(
        input('Please enter the saving path and press "Enter": '), 'results.xlsx')
    print('Start exporting the results...')
    results.to_excel(saving_path, index=False)
    print(f'\nData exporting process completed!\nTotal number of articles found: {results.title.count()}\n'
          f'Please find the results from this path: {saving_path}')
else:
    print('No articles are found for the past 7 days!')

input('\nPress enter to quit...')
