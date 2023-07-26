import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select


print('Loading driver...')
options = Options()
# options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
print('Driver load')

print('Open site...')
driver.get('https://www.roblox.com')

month = driver.find_element(By.ID, 'MonthDropdown')
day = driver.find_element(By.ID, 'DayDropdown')
year = driver.find_element(By.ID, 'YearDropdown')
selectmonth = Select(month)
selectday = Select(day)
selectyear = Select(year)

selectmonth.select_by_index(random.randint(1, 12))
selectday.select_by_index(random.randint(1, 28))
selectyear.select_by_value(str(random.randint(1924, 2023)))

user = driver.find_element(By.ID, 'signup-username')
valid = driver.find_element(By.ID, 'signup-usernameInputValidation')
name = 'Andrey'
user.send_keys(name)
while True:
    time.sleep(1)
    if valid.text == 'This username is already in use.':
        user.send_keys(str(random.randint(0, 9)))
    else:
        break

passw = driver.find_element(By.ID, 'signup-password')
valid = driver.find_element(By.ID, 'signup-passwordInputValidation')
pas = 'qwertyui'
passw.send_keys(pas)
while True:
    time.sleep(1)
    if valid.text == 'Please create a more complex password.':
        passw.send_keys(str(random.randint(0, 9)))
    else:
        break

sex = driver.find_element(By.ID, 'MaleButton')
sex.click()


time.sleep(20)

driver.close()

