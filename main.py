from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\Users\R021340\AppData\Local\JetBrains\PyCharm Community Edition 2019.3.3\bin\chromedriver.exe')
driver.get("https://calendar.google.com/calendar/r/search?q=NCAD&start=20200517&end=20200523")

element1 = driver.find_element_by_name("identifier")
element1.send_keys("russell.pacheco@randstad.co.jp")
element1.send_keys(Keys.RETURN)

driver.implicitly_wait(4)

element2 = driver.find_element_by_name("password")
element2.send_keys("7aiIJzRg8PC3")
element2.send_keys(Keys.RETURN)

driver.implicitly_wait(10)
try:
    rows = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "taTyDe DSThoc"))
    )

    articles = rows.
except:
    driver.quit()


for row in rows:
    details = row.find_element_by_class_name("i06k6b NlL62b")
    print(details.text)
