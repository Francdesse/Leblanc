from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


# open the url and to go QA automation page
driver.get('https://www.careerist.com/')

driver.find_element(By.XPATH, "//span[text()= 'Our Programs' and @class= 'dropdown__title']").click()
driver.find_element(By.XPATH, "//a[text()= 'QA Automation' and @class='dropdown__link']").click()

Expected_result = 'QA Automation'
Actual_result = driver.find_element(By.XPATH, "//strong[text()= 'QA Automation']").text
assert Expected_result == Actual_result

print('QA Automation page pass')


# signing for a free consultation
driver.find_element(By.XPATH, "//button[text()='Get Free Consultation']").click()
driver.find_element(By.XPATH, "//div[@id='modal-req-form']//div[@class='modal-content']//form[@class='form extform extform_ready'] \
                                //div[@class='inp-group inp-group--input']//input[contains(@placeholder, 'Your full name')]").send_keys('John Snow')
driver.find_element(By.XPATH, "//div[@id='modal-req-form']//form[@class='form extform extform_ready']//input[@name='email' and @placeholder='Email']").send_keys('johnsnow@google.com')
driver.find_element(By.XPATH, "//div[@id='modal-req-form']//form[@class='form extform extform_ready']//input[@name='phone' and @placeholder='Phone, e.g. 999 555-2222']").send_keys('8005566770')
driver.find_element(By.XPATH, "//div[@id='modal-req-form']//div[@class='modal-req-form__in']//form[@class='form extform extform_ready'] \
                                //div[@class='form__btn']//button[@type='button' and @class='extform__submit btn btn-big btn-blue']").click()


# verify that user is able to sign up for a consultation and start the application progress

Expected_result1= 'Application in progress'
Actual_result1= driver.find_element(By.XPATH, "//span[text()='Application in progress']").text
assert Expected_result1 == Actual_result1
print('user is able to submit a form go to the application page')






driver.quit()