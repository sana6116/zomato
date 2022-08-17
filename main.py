from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import itertools


cities = [
    'Lucknow',
    'Patna',
    'Kolkata',
    'Mumbai',
    'Jaipur'
]

def parse_for_city(driver, city):
    driver.get(f'https://www.zomato.com/{city.lower()}/dine-out?rating_range=4.0-5.0')


    for i in range(10):
        driver.execute_script(f"window.scrollTo(0, {i*400})") 
        time.sleep(3)


    # Find something which is static
    rest_names = driver.find_elements(
        By.CLASS_NAME, 'sc-1hp8d8a-0'
    )

    # select the parent div, in this case select parent to parent div
    restaurant_divs = [
        el.find_element(
            By.XPATH, "./../.."
        ) for el in rest_names
    ]

    restaurants = []

    for restaurant_div in restaurant_divs:
        try:
            restaurant_name = restaurant_div.find_element(
                By.XPATH, "./div[1]/h4"
            )
            # although data is present inside too many divs 
            # but text of the first div will give rating no need to go deep
            rating = restaurant_div.find_element(
                By.XPATH, "./div[1]/div"
            )
            restaurant_type = restaurant_div.find_element(
                By.XPATH, "./div[2]/p[1]"
            )
            price_range = restaurant_div.find_element(
                By.XPATH, "./div[2]/p[2]"
            )
            area = restaurant_div.find_element(
                By.XPATH, "./p[1]"
            )
        except:
            # for a case where the div is not in expected form
            continue
        restaurants.append({
            "city": city,
            "restaurant_name": restaurant_name.text,
            "rating": rating.text,
            "area": area.text,
            "restaurant_type": restaurant_type.text,
            "price_range": price_range.text,
            "url": restaurant_div.get_attribute('href'),
        })
    return restaurants



webdriver = webdriver.Chrome(ChromeDriverManager().install())
df = pd.DataFrame(
    list(itertools.chain(*[parse_for_city(webdriver, city) for city in cities]))
)
df.to_csv("restaurants.csv", index=False)
webdriver.quit()