import pytest

from Pom.companyreview import Glassdoor
from Library.config import Config
from Data.reading_obj import ReadExcel


class TestCompanyreview:
    read_xl=ReadExcel()
    data=read_xl.read_test_data()
    @pytest.mark.parametrize("Enter_Email,Enter_pwd,Enter_companyname,Enter_jobname,Enter_reason,Enter_review,enter_downsides",data)
    def test_Glassdoor(self,init_driver,Enter_Email,Enter_pwd,Enter_companyname,Enter_jobname,Enter_reason,Enter_review,enter_downsides):
        driver=init_driver
        s1 =Glassdoor(driver)
        s1.Enter_Email(Enter_Email)
        s1.Click_continue()
        s1.Enter_pwd(Enter_pwd)
        s1.Click_signin()
        s1.Click_companies()
        s1.Click_writereview()
        s1.Radiobtn_company()
        s1.Radiobtn_currentemp()
        s1.Enter_companyname(Enter_companyname)
        s1.Next_btn()
        s1.Enter_rating()
        s1.Click_options()
        s1.Select_dropdown()
        s1.Enter_jobname(Enter_jobname)
        s1.Enter_review(Enter_review)
        s1.Enter_reason(Enter_reason)
        s1.Enter_downside(enter_downsides)
        s1.Click_checkbox()



