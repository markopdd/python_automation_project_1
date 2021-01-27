from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.XPATH, "//input[@id='country']")
    country_list = (By.XPATH, "//a[normalize-space()='India']")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    alert_success = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def check_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def country_results(self):
        return self.driver.find_element(*ConfirmPage.country_list)

    def checkbox_mark(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def check_alert_success(self):
        return self.driver.find_element(*ConfirmPage.alert_success)