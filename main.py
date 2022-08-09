from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.zomato.com/lucknow/delivery?rating_range=4.0-5.0')

time.sleep(3)

rest_names = driver.find_elements(
    By.CLASS_NAME, 'sc-1hp8d8a-0'
)

ratings = driver.find_elements(
    By.CLASS_NAME, 'sc-1q7bklc-1'
    )

costs = driver.find_elements(
    By.CLASS_NAME, 'iumJIm'
)

print(len(rest_names))
res = []

for rest in rest_names:
    res= rest.text


    print(res)


for rating in ratings:
    rate =rating.text
    print(rate)
    

#for cost in costs:
    #print(cost.text)
    data = {
        'restaurant' : res,
        'rates' : rate,
    }
    df = pd.DataFrame(data, index=[0])
    df.columns.to_list()
    df.to_csv('lucknow_restaurant.csv')


driver.quit()