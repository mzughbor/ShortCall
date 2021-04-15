from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pyperclip
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AList = ['AF', '93', 'AL', '355', 'AS', '1', 'AD', '376', 'AO', '244', 'AI', '1', 'AG', '1', 'AR', '54', 'AM', '374', 'AW', '297', 'AU', '61', 'AT', '43', 'AZ', '994', 'BS', '1', 'BD', '880', 'BB', '1', 'BY', '375', 'BE', '32', 'BZ', '501', 'BJ', '229', 'BM', '1', 'BT', '975', 'BO', '591', 'BQ', '599', 'BA', '387', 'BW', '267', 'BR', '55', 'VG', '1', 'BN', '673', 'BG', '359', 'BF', '226', 'BI', '257', 'KH', '855', 'CM', '237', 'CA', '1', 'CV', '238', 'KY', '1', 'CF', '236', 'TD', '235', 'CL', '56', 'CN', '86', 'CO', '57', 'KM', '269', 'CG', '242', 'CK', '682', 'CR', '506', 'HR', '385', 'CU', '53', 'CW', '599', 'CY', '357', 'CZ', '420', 'CI', '225', 'DK', '45', 'DJ', '253', 'DM', '1', 'DO', '1', 'EC', '593', 'SV', '503', 'GQ', '240', 'ER', '291', 'EE', '372', 'ET', '251', 'FK', '500', 'FO', '298', 'FJ', '679', 'FI', '358', 'FR', '33', 'GF', '594', 'PF', '689', 'GA', '241', 'GM', '220', 'GE', '995', 'DE', '49', 'GH', '233', 'GI', '350', 'GR', '30', 'GL', '299', 'GD', '1', 'GP', '590', 'GU', '1', 'GT', '502', 'GN', '224', 'GW', '245', 'GY', '592', 'HT', '509', 'HN', '504', 'HK', '852', 'HU', '36', 'IS', '354', 'IN', '91', 'ID', '62', 'IR', '98', 'IE', '353', 'IM', '44', 'IL', '972', 'IT', '39', 'JM', '1', 'JP', '81', 'JE', '44', 'KZ', '7', 'KE', '254', 'KI', '686', 'KG', '996', 'LA', '856', 'LV', '371', 'LS', '266', 'LR', '231', 'LI', '423', 'LT', '370', 'LU', '352', 'MO', '853', 'MK', '389', 'MG', '261', 'MW', '265', 'MY', '60', 'MV', '960', 'ML', '223', 'MT', '356', 'MQ', '596', 'MR', '222', 'MU', '230', 'YT', '262', 'MX', '52', 'FM', '691', 'MD', '373', 'MC', '377', 'MN', '976', 'ME', '382', 'MS', '1', 'MZ', '258', 'MM', '95', 'NA', '264', 'NR', '674', 'NP', '977', 'NL', '31', 'NC', '687', 'NZ', '64', 'NI', '505', 'NE', '227', 'NG', '234', 'NF', '672', 'MP', '1', 'NO', '47', 'PK', '92', 'PS', '970', 'PA', '507', 'PG', '675', 'PY', '595', 'PE', '51', 'PH', '63', 'PL', '48', 'PT', '351', 'PR', '1', 'RE', '262', 'RO', '40', 'RU', '7', 'RW', '250', 'KN', '1', 'LC', '1', 'MF', '590', 'VC', '1', 'WS', '685', 'SM', '378', 'ST', '239', 'SN', '221', 'RS', '381', 'SC', '248', 'SL', '232', 'SG', '65', 'SX', '1', 'SK', '421', 'SI', '386', 'SB', '677', 'SO', '252', 'ZA', '27', 'KR', '82', 'SS', '211', 'ES', '34', 'LK', '94', 'SR', '597', 'SZ', '268', 'SE', '46', 'CH', '41', 'TW', '886', 'TJ', '992', 'TZ', '255', 'TH', '66', 'CD', '243', 'TL', '670', 'TG', '228', 'TO', '676', 'TT', '1', 'TR', '90', 'TM', '993', 'TC', '1', 'TV', '688', 'VI', '1', 'UG', '256', 'UA', '380', 'GB', '44', 'US', '1', 'UY', '598', 'UZ', '998', 'VU', '678', 'VE', '58', 'VN', '84', 'XK', '383', 'ZM', '260', 'ZW', '263', 'JO', '962', 'AE', '971', 'BH', '973', 'DZ', '213', 'SA', '966', 'IQ', '964', 'KW', '965', 'MA', '212', 'YE', '967', 'TN', '216', 'OM', '968', 'QA', '974', 'LB', '961', 'LY', '218', 'EG', '20']

class TwitterSignup(object):
    def __init__(self):
        global driver
        driver  = webdriver.Chrome(executable_path='C:/WebDriver/chromedriver.exe') # for another OS CHANGE this Path
        self.driver = driver

    def Signup(self):
        global tester
        tester = 0
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span').click()
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input').send_keys('Nahnood')
        windows_before = driver.current_window_handle
        self.driver.execute_script("window.open('https://emailfake.com/')")
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        windows_after = self.driver.window_handles
        new_window = [x for x in windows_after if x != windows_before][0]
        self.driver.switch_to.window(new_window)
        self.driver.find_element_by_xpath('//*[@id="copbtn"]').click()
        email = pyperclip.paste()
        print(email)
        self.driver.switch_to.window(windows_before)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input').send_keys(email)
        element = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "Month")))
        Select(element).select_by_value("6")
        day = WebDriverWait(self.driver,6).until(EC.visibility_of_element_located((By.ID, "Day")))
        Select(day).select_by_value("14")
        year = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, "Year")))
        Select(year).select_by_value("1999")
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div').click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div').click()
        self.driver.switch_to.window(new_window)
        time.sleep(3)
        self.driver.refresh()
        verification = self.driver.find_element_by_xpath('//*[@id="email-table"]/div[1]/div[2]').text
        verification = verification.split()[0]
        driver.close()
        self.driver.switch_to.window(windows_before)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input').send_keys(verification)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
        time.sleep(2)

        elements = driver.find_elements_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/label/div/div[2]/div/input')
        if len(elements) != 1:
            tester = line
            print('line',line,'elem',element,'lenelement',len(elements))
            print("im here")
            driver.close()
        else:
            print('hi 1',cc)
            countryCode = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID, "Country code")))
            print('hi 2',cc)
            Select(countryCode).select_by_value(cc)
            print('hi 3',cc)
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/label/div/div[2]/div/input').send_keys(line)
            print('hi 4',cc)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
            driver.close()


def get_indices(x: list, value: str) -> list:
    indices = list()
    for i in range(len(x)):
        if x[i] == value:
            indices.append(i)
    return indices

# Run
with open("D:\shortcall\\twitter_v3\\twitter_v3-01\\numbers.txt") as file_in:
    for line in file_in:
        preNum = line[0:3]
        result = get_indices(AList, str(preNum))
        if len(result) == 1:
            print(preNum, result, AList[result[0] - 1])
            cc =AList[result[0] - 1]
        else:
            # len(result) > 1 or len(result) == 0:
            preNum = line[0:2]
            result = get_indices(AList, str(preNum))
            if len(result) == 0:
                preNum = line[0:1]
                result = get_indices(AList, str(preNum))
                print(preNum, result, AList[result[-1] - 1])
                cc = AList[result[-1] - 1]
                continue
            else:
                print(preNum, result, AList[result[0] - 1])
                cc = AList[result[0] - 1]

        try:
            test = TwitterSignup()
            test.Signup()
        except WebDriverException:
            print("page down")
        if tester == line:
            try:
                test = TwitterSignup()
                test.Signup()
            except WebDriverException:
                print("page down 2 ")
        else:
            continue
file_in.close()
