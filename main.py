from selenium import webdriver
import  undetected_chromedriver as uc 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def menu():
    print("*" * 40)
    print("Telegram Scraper & Mass DM Sender Tool")
    print("*" * 40)
    print()
    print("Choose an option:")
    print("1. Scrape followers of given group")
    print("2. Send DMs to scraped followers")
    print("3. Exit")
with open("group_name.txt", "r") as f:
            group_name = f.read()

chrome_options = uc.ChromeOptions()
chrome_options.add_argument(r'--no-sandbox')
        
driver = uc.Chrome(options=chrome_options)
driver.get('https://web.telegram.org/a/')
        
wait = WebDriverWait(driver, 50)
action = ActionChains(driver)
while True:
    menu()
    choice = int(input("\nEnter your choice: (1 - 3): "))

    if choice == 1:
        try:
            #search group by name
            searchTextbox = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div[2]/input')))
            action.move_to_element(searchTextbox).click().send_keys(group_name).perform()
            time.sleep(5)

            firstSearchAppear = driver.find_element("xpath" ,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]')
            firstSearchAppear.click()
            time.sleep(1)

            groupExpand = driver.find_element("xpath", "/html/body/div[2]/div/div[2]/div[4]/div[1]/div[1]/div/div/div/div[2]")
            groupExpand.click()
        except:
            print("Provide a valid group Name")

        time.sleep(4)
        with open('scrapped_users.txt', 'w') as file:
            pass
        try:
            memberList = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div")
            sub_divs = memberList.find_elements(By.XPATH, "./div")
        except:
            print("Not a valid group")
        print("Started Scrapping....")
        print(len(sub_divs))
        for i in range(0, len(sub_divs)):
            if i != 0:
                try:
                    memberIdtag  = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div/div/div[1]".format(i+1))
                    memberId = memberIdtag.get_attribute("data-peer-id")
                    memberNametag = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/div/div[2]/div/div[2]/div[1]/div/div[{}]/div/div/div[2]/div/h3".format(i+1))
                    print(memberId, memberNametag.text)
                    with open('scrapped_users.txt', 'a') as f:
                        f.write(str(memberNametag.text) + ", " +  str(memberId) + '\n')
                except:
                    pass
        print("Scrapping done!")
        time.sleep(4)
    if choice == 2:
        with open("message.txt", "r") as f:
            message = f.readlines()
        with open('scrapped_users.txt', 'r') as f:
            l = f.readlines()
        print("Sending messages ....")
        print(len(l))
        for i in l:
            try:    
                driver.get("https://web.telegram.org/k/#{}".format(str(i.split(',')[1].strip())))
                print(("https://web.telegram.org/k/#{}".format(str(i.split(',')[1].strip()))))
                time.sleep(5)
                driver.execute_script("location.reload()")
                time.sleep(5)
                msgBox = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')))
                for i in message:
                    msgBox.send_keys(i)
                time.sleep(2)
                sendbutton = driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div[4]/div/div[5]/button")
                sendbutton.click()
            except:
                pass
        print("Sending messages done!")
    
        
    if choice == 3:
        break