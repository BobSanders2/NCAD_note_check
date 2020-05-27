from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://calendar.google.com/calendar/r/search?q=NCAD&start=20200517&end=20200523")

element1 = driver.find_element_by_name("identifier")
element1.send_keys("russell.pacheco@randstad.co.jp")
element1.send_keys(Keys.RETURN)

driver.implicitly_wait(8)

element2 = driver.find_element_by_name("password")
element2.send_keys("7aiIJzRg8PC3")
element2.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

totaldata = driver.find_element_by_class_name("yHbHub")
eventsgroup = totaldata.find_elements_by_class_name("L1Ysrb")
for group in eventsgroup:
    print(group.text)

#yHbHub this works but has time
#L1Ysrb this works but has time
#taTyDe DSThoc
#dtaVuc OY8yJd
#LLxvl IeojK EmMre
#i06k6b NlL62b
