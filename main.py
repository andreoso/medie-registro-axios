userid = "MODIFICAMI"
password = "MODIFICAMI"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.get("https://family.sissiweb.it/Secret/REStart.aspx?Customer_ID=92047700155")
sleep(2.5)
elem = driver.find_element_by_name("txtUser")
elem.clear()
elem.send_keys(userid)
elem = driver.find_element_by_name("txtPassword")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
sleep(3)
elem = driver.find_element_by_id("IdRED")
elem.click()
sleep(3)
elem = driver.find_elements_by_class_name('label');

tot = 0
count = 0
for a in elem:
    raw = a.text
    val = raw.replace(',', '.')
    tot = tot + float(val)
    count += 1

media = tot / count
print ("Hai ", count, " voti")
print ("La media dei voti e' : ", media)


driver.close()










