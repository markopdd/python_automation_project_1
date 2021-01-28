from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    card = (By.XPATH, "//div[@class='card h-100']")
    checkout_button = (By.XPATH, "//li[@class='nav-item active']")
    go_check = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def card_items(self):
        return self.driver.find_elements(*CheckoutPage.card)

    def checkout(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def checkout_verify(self):
        self.driver.find_element(*CheckoutPage.go_check).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
