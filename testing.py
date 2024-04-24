from selenium import webdriver
import  undetected_chromedriver as uc 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


with open("message.txt", "r") as f:
    message = f.readlines()
print(message)

with open("group_name.txt", "r") as f:
    group_name = f.read()
group_name = group_name.replace(" ", "_")

with open(f'{group_name}.txt', 'w') as file:
    file.write('usernames of {} group members'.format(group_name) + '\n')

chrome_options = uc.ChromeOptions()
chrome_options.add_argument(r'--no-sandbox')

driver = uc.Chrome(options=chrome_options)
driver.get('https://web.telegram.org/a/')
# driver.add_cookie({'name': 'sessionid', 'value': cookies})
wait = WebDriverWait(driver, 50)
action = ActionChains(driver)

#search group by name
searchTextbox = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/input')))
action.move_to_element(searchTextbox).click().send_keys(group_name).perform()
time.sleep(5)

firstSearchAppear = driver.find_element("xpath" ,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]')
firstSearchAppear.click()
time.sleep(1)
groupExpand = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div[2]")
groupExpand.click()
time.sleep(4)

memberList = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div")
sub_divs = memberList.find_elements(By.XPATH, "./div")
time.sleep(4)
for i in range(0, len(sub_divs)):
    if (i != 0):
        name = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div/div/div[2]/div/h3".format(i + 1))
        with open(f'{group_name}.txt', 'a') as f:
            f.write(str(name.text) + '\n')

    member = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div".format(i + 1))
    member.click()
    time.sleep(1)

    msgbox = driver.find_element("xpath" , "/html/body/div[2]/div/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]")
    print(message)
    for i in message:
        msgbox.send_keys(i)
    time.sleep(1)

    sendbutton = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div[4]/div[2]/div[2]/div[2]/div[1]/button")
    sendbutton.click()
    time.sleep(1)

    backbutton  = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/button")
    backbutton.click()
    time.sleep(1)

time.sleep(500)

    