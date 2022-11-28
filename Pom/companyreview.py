import time
import xlrd
from Data.reading_obj import ReadExcel
from Data import reading_obj
from selenium.webdriver.common.action_chains import ActionChains

from Library.config import Config
from selenium.webdriver.common.keys import Keys
var = "glassdoor"
obj_1=ReadExcel()
review_obj=obj_1.read_locator(Config.locator_sheet)

class Glassdoor():

    def __init__(self,driver):
        self.driver=driver
    def Enter_Email(self,Enter_Email):
        self.Enter_Email=Enter_Email
        self.driver.find_element(*review_obj['Enter_Email']).send_keys(Enter_Email)
    def Click_continue(self):
        self.driver.find_element(*review_obj['click_continue']).click()
    def Enter_pwd(self,Enter_pwd):
        self.Enter_pwd=Enter_pwd
        if isinstance(Enter_pwd,float):
            Enter_pwd=str(int(Enter_pwd))
        assert len(Enter_pwd) == 10
        obj1 = self.driver.find_element(*review_obj['Enter_pwd'])
        obj = ActionChains(self.driver)
        obj.click(obj1)
        obj.send_keys(Enter_pwd).perform()
    def Click_signin(self):
        self.driver.find_element(*review_obj['click_signin']).click()
    def Click_companies(self):
        time.sleep(7)
        company=self.driver.find_element(*review_obj['click_companies'])
        obj = ActionChains(self.driver)
        obj.move_to_element(company).perform()

    def Click_writereview(self):
        self.driver.find_element(*review_obj['click_writereview']).click()
    def Radiobtn_company(self):
        self.driver.find_element(*review_obj['click_radiobtn_company']).click()
    def Radiobtn_currentemp(self):
        self.driver.find_element(*review_obj['click_radiobtn_currentemp']).click()
    def Enter_companyname(self,Enter_companyname):
        self.Enter_companyname=Enter_companyname
        self.driver.find_element(*review_obj['Enter_companyname']).send_keys(Enter_companyname)
        time.sleep(3)
        self.driver.find_element(*review_obj['click_comanyname']).click()
    def Next_btn(self):
        time.sleep(3)
        self.driver.find_element(*review_obj['click_nextbtn']).click()
    def Enter_rating(self):
        self.driver.find_element(*review_obj['enter_rating']).click()
    def Click_options(self):
        self.driver.find_element(*review_obj['click_options']).click()
    def Select_dropdown(self):
        self.driver.find_element(*review_obj['select_dropdown']).click()
    def Enter_jobname(self,Enter_jobname):
        self.Enter_jobname=Enter_jobname
        self.driver.find_element(*review_obj['Enter_jobname']).send_keys(Enter_jobname)
        time.sleep(4)
        obj = ActionChains(self.driver)
        obj.send_keys(Keys.ARROW_DOWN).perform()
        obj.send_keys(Keys.ARROW_UP).perform()
        obj.send_keys(Keys.ENTER).perform()
    def Enter_review(self,Enter_review):
        self.Enter_review=Enter_review
        time.sleep(3)
        self.driver.find_element(*review_obj['Enter_review']).send_keys(Enter_review)
    def Enter_reason(self,Enter_reason):
        self.Enter_reason=Enter_reason
        self.driver.find_element(*review_obj['Enter_reason']).send_keys(Enter_reason)
    def Enter_downside(self,enter_downsides):
        self.enter_downsides=enter_downsides
        self.driver.find_element(*review_obj['enter_downsides']).send_keys(enter_downsides)
    def Click_checkbox(self):
        self.driver.find_element(*review_obj['click_checkbox']).click()
        # driver.find_element("xpath","//span[text()='Submit Review']").click()




