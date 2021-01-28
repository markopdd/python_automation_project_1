from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    shop = (By.XPATH, "//nav/ul/li[2]")
    name = (By.XPATH, "// input[ @ name = 'name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    employment = (By.XPATH, "//input[@id='inlineRadio2']")
    day_of_birth = (By.XPATH, "//input[@name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    success_result = (By.XPATH, "//div/strong['Success!']")

    def __init__(self, driver):
        self.driver = driver

    def name_values(self):
        return self.driver.find_element(*HomePage.name)

    def email_values(self):
        return self.driver.find_element(*HomePage.email)

    def password_values(self):
        return self.driver.find_element(*HomePage.password)

    def checkbox_mark(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def employment_radiobutton(self):
        return self.driver.find_element(*HomePage.employment)

    def set_day_of_birth(self):
        return self.driver.find_element(*HomePage.day_of_birth)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_result(self):
        return self.driver.find_element(*HomePage.success_result)

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
