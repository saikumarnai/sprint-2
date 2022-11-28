import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given(u'I launch Chrome browser')
def step_impl(context):
    path = r"C:\Users\sai kumar naik\Downloads\chromedriver_win32\chromedriver.exe"
    context.driver = webdriver.Chrome(path)
    time.sleep(2)
    context.driver.implicitly_wait(50)




@given(u'Enter email')
def step_impl(context):
    time.sleep(2)

    context.driver.get(r"https://www.glassdoor.co.in/profile/login_input.htm")
    time.sleep(2)


    context.driver.maximize_window()
    time.sleep(2)

    context.driver.find_element_by_xpath("//input[@id='inlineUserEmail']").send_keys("sainaik8639@gmail.com")
    time.sleep(2)



@given(u'click on continue with email')
def step_impl(context):
    time.sleep(2)

    context.driver.find_element_by_xpath("//span[@class='css-2etp8b evpplnh1']").click()
    time.sleep(2)


@given(u'Enter Password')
def step_impl(context):
    obj1 = context.driver.find_element_by_xpath("//label[@class='css-w3qhip eb2o9h0']")
    obj = ActionChains(context.driver)
    obj.click(obj1)
    obj.send_keys("9866875783").perform()


@then(u'click on signin')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[text()='Sign In']").click()


@then(u'move on companies')
def step_impl(context):
    company = context.driver.find_element("xpath",'(//div[@class="d-flex flex-column align-items-center justify-content-center flex-lg-row justify-content-lg-start"])[3]')
    obj = ActionChains(context.driver)
    obj.move_to_element(company).perform()



@then(u'click on write a review')
def step_impl(context):
    context.driver.find_element("xpath", "(//span[text()='Write a Review'])[2]").click()


@then(u'click on compant review')
def step_impl(context):
    context.driver.find_element("xpath", "//div[text()='Company Review']").click()


@then(u'click on current employee')
def step_impl(context):
    context.driver.find_element("xpath", '//div[text()="Current Employee"]').click()


@then(u'Enter company name')
def step_impl(context):
    context.driver.find_element("xpath", '//input[@name="survey-AddCompany-component"]').send_keys("Capgemini")


@then(u'click on company name')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element("xpath", "//span[text()='Capgemini']").click()



@then(u'click on next')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element("xpath", '//button[@class="gd-ui-button css-s89dmq evpplnh0"]').click()


@then(u'click on star')
def step_impl(context):
    context.driver.find_element("xpath", '(//span[@class="gd-ui-star  css-15840pv e7cj4650"])[5]').click()


@then(u'click on dropdown')
def step_impl(context):
    context.driver.find_element("xpath", '//div[@class="css-47sx24 egu3u860"]').click()


@then(u'select fulltime')
def step_impl(context):
    context.driver.find_element("xpath", '(//div[@class="dropDownOptionsContainer"])[1]').click()


@then(u'enter job')
def step_impl(context):
    context.driver.find_element("xpath", '//input[@name="survey-company-component"]').send_keys("Analyst")


@then(u'click on job')
def step_impl(context):
    time.sleep(5)
    context.driver.find_element("xpath", "(//span[text()='Analyst'])[1]").click()


@then(u'Enter review')
def step_impl(context):
    context.driver.find_element("xpath", '//input[@id="ReviewHeadline"]').send_keys("General feeling of work happiness")


@then(u'enter reasons')
def step_impl(context):
    context.driver.find_element("xpath", '//textarea[@id="ProsTextField"]').send_keys(
        "Feel free to growOver the course of your career, your goals may shift. Want to change your focus? Switch tracks? We’re here to help.")


@then(u'enter downsides')
def step_impl(context):
    context.driver.find_element("xpath", '//textarea[@id="ConsTextField"]').send_keys(
        "No downsides of working at Capgemini company")

@then(u'click on checkbox')
def step_impl(context):
    context.driver.find_element("xpath", '//div[@class="checkboxBox"]').click()






