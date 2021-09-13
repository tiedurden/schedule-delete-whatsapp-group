from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

import datetime
from datetime import datetime, timedelta
import threading
import time
import schedule
from schedule import Scheduler

import os, platform, sys


print(platform.system())

group_deleted = False

# Browser instance has to have an open connection from webwhatsapp to the phone
# tbd if it works after standby/restart
chrome_options = Options()
chrome_options.add_argument("--user-data-dir='path-to-chrome-profile'") # change to profile path
chrome_options.add_argument('--profile-directory=Profile 1')
# options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
#

# input_groupname = input("Which group should be deleted: ")
# input_member_count = int(input("Number of group members: "))
# TODO if possible get member_count automatic, count child divs 
# count i
# xpath_count_member divs'//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[4]/div/div[i]/div/div/div[2]/div[2]'


def delete_group():
    print("started deleting process")
    driver = webdriver.Chrome(options=chrome_options)
    action = ActionChains(driver)

    driver.get('https://web.whatsapp.com/')
    #input('Enter anything after scanning QR code')
    sleep(5)

    member_count = 2
    groupname = "testgruppe_auto2"

    # groubmemberi_xpath = "//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[4]/div/div[INDEX]/div/div/div[2]"
    # install loop for i group members to kick

    # search group
    searchfield = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    searchfield.click()
    try:    
        searchfield.send_keys(groupname)
        searchfield.send_keys(Keys.RETURN)
    except NoSuchElementException:
        print("No such Element")

        

    driver.find_element_by_xpath('//span[@title = "{}"]'.format(groupname))\
        .click()
    sleep(3)

    # communicate selfdestruction
    # msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    # msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
    # msg_box.send_keys("Selbstzerstoerung in:")
    # msg_box.send_keys(Keys.RETURN)
    # for i in range(3, 0, -1):
    #     sleep(1)
    #     msg_box.send_keys(i)
    #     msg_box.send_keys(Keys.RETURN)


    # go to group menu
    driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')\
        .click()
    sleep(3)

    # kick members
    for i in range(1, member_count):
        print(i)
        xpath_kick_menu = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[4]/div/div[1]/div/div/div[2]/div[2]'
        xpath_kick_menu = '//*[@id="app"]/div[1]/div[1]/div[2]/div[3]/span/div[1]/span/div[1]/div/section/div[5]/div[4]/div/div[1]/div/div/div[2]/div[2]'
        action.move_to_element(driver.find_element_by_xpath(xpath_kick_menu)).perform()
        action.context_click().perform()
        driver.find_element_by_xpath('//div[@aria-label = "Entfernen"]')\
        .click()
        sleep(1)
        # really kick
        driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')\
            .click()
        sleep(3)

     

    # leave group
    driver.find_element_by_xpath('//div[@title = "Gruppe verlassen"]')\
        .click()
    sleep(2)
    # really leave / confirm leaving
    driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')\
        .click()
    sleep(3)

    # delete Group
    driver.find_element_by_xpath('//div[@title = "Gruppe löschen"]')\
        .click()
    sleep(2)
    # confirm leaving
    driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')\
        .click()


    # TODO wrap in try-except block to only set True if 
    # group is not findable
    group_deleted = True
    quit()

def job_that_executes_once():
    delete_group()
    return schedule.CancelJob

today = datetime.now().strftime('%Y-%m-%d')
print(today)

if today == "2021-09-12":
    print("today is today")
    schedule.every().day.at('19:30').do(job_that_executes_once)
else:
    print("today is not today")


while not group_deleted :
    schedule.run_pending()
    time.sleep(1) 