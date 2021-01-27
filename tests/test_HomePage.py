import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_home_page(self, get_data):
        homepage = HomePage(self.driver)
        homepage.name_values().send_keys(get_data["first_name"])
        homepage.email_values().send_keys(get_data["email"])
        homepage.password_values().send_keys(get_data["password"])
        homepage.checkbox_mark().click()

        self.select_option_by_text(homepage.get_gender(), get_data["gender"])
        homepage.employment_radiobutton().click()
        homepage.set_day_of_birth().send_keys(get_data["dofb"])
        homepage.get_submit().click()
        success_text = homepage.get_success_result().text

        assert success_text == 'Success!'
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data_from_excel("TestCase1"))
    def get_data(self, request):
        return request.param
