from selenium import webdriver
import time
import pyperclip
import os
from pywinauto.application import Application
from pywinauto import actionlogger
import logging
import argparse

class MyTest(object):
    def __init__(self):
        global driver
        driver  = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe') # for another OS CHANGE this Path
        self.driver = driver

    def login_process(self):
        self.driver.get("https://client.premiumy.net/login")
        # self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[1]/div/input').send_keys('test')  # ('')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[2]/div/input').send_keys('premiumy_test') # ('')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/form/div[4]/div[1]/button').click()

    def get_numbers(self):
        self.driver.get("https://client.premiumy.net/accesses")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[1]/form/div/div[2]/div/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[1]/form/div/div[2]/div/div/div/input').send_keys('twitter')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[6]/form/div/div/input').clear()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[6]/form/div/div/input').send_keys('100')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[5]/div[2]/div[1]/div[1]/div/div[4]/div/div/button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/form/div/div[1]/div/div/div/div/div/div/a').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/a').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div/div/div/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/form/div/div[2]/div/div/div/div/div/input').send_keys('2')
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/form/div/div[3]/div/div/label/span').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[3]/button[1]').click()
        time.sleep(10) # it's important when internet speed is sucks ...
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[5]/div[1]/div/a').click()
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div[5]/div[1]/div/ul/li[1]/a').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/a').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/div[1]/ul/li[12]/a').click()
        #self.driver.close()
        # Hint do >>> pip install pyperclip <<< for another OS users
        s = pyperclip.paste()
        print(s)
        with open('numbers.txt', 'w') as file_numbers:
            file_numbers.write(s)

    def remove_empty_lines(self):
        ''' This Function for removing line from txt file after using paste from clipboard'''
        if not os.path.isfile('numbers.txt'):
            print("{} does not exist ".format('numbers.txt'))
            return
        with open('numbers.txt') as filehandle:
            lines = filehandle.readlines()
        with open('numbers.txt','w') as filehandle:
            lines = filter(lambda x: x.strip(), lines)
            filehandle.writelines(lines)

    def start_disktop_app(self):
        '''This Function to start running the numbers by Twitter Script'''
        parser = argparse.ArgumentParser()
        parser.add_argument("--log", help="enable logging", type=str, required=False)
        args = parser.parse_args()

        actionlogger.enable()
        logger = logging.getLogger('pywinauto')

        if args.log:
            logger.handlers[0] = logging.FileHandler(args.log)

        app = Application(backend='uia').start(r'D:\shortcall\\twitter_v3\\twitter_v3-01\\Twitter_test.exe')
        dlg = app.window(title_re='Twitter')
        dlg.child_window(title="Prefix :", auto_id="TextBox2", control_type="Edit").set_text('TU')
        dlg.child_window(title="Start", auto_id="Btn_Start", control_type="Button").click()


numOfIterasions = 5
test = MyTest()

#try:
while numOfIterasions >= 0 :

    test.login_process()
    checkTF = driver.find_elements_by_link_text("Report") # check if logged in or not
    #print(checkTF)
    while len(checkTF) == 0 :
        #print('the list is empty')
        test.login_process()
        time.sleep(8)
        if len(checkTF) != 0:
            continue
        break

    test.get_numbers()
    test.remove_empty_lines()

    if numOfIterasions == 0:
        driver.close()

    test.start_disktop_app()
    time.sleep(70) # need to be connected to X close twitter script ...
    numOfIterasions -= 1
    continue

#except Exception as e:
#    print("An exception occurred:", e)
