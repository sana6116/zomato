from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.zomato.com/lucknow/delivery?rating_range=4.0-5.0')
#driver.get('https://www.zomato.com/ncr/dine-out?rating_range=4.0-5.0')

for i in range(5):
    driver.execute_script(f'window.scrollTo(0,{i*400})')
    time.sleep(3)

rest_names = driver.find_elements(
    By.CLASS_NAME, 'sc-1hp8d8a-0'
)

ratings = driver.find_elements(
    By.CLASS_NAME, 'sc-1q7bklc-1'
)

cost_details = driver. find_elements(
    By.CLASS_NAME, 'sc-jTqLG'
)

cost = [c.text for c in cost_details]
print(cost)

data = {
    'restaurant' : [el.text for el in rest_names],
    'rating' : [el.text for el in ratings],
    
}
        
    
df = pd.DataFrame(data)
df.to_csv('lucknow_restaurant.csv', index=False)






    
    





driver.quit()
