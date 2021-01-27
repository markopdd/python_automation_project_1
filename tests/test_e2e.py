from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()

        homepage = HomePage(self.driver)
        checkout_page = homepage.shop_items()
        log.info("Get card items")
        products = checkout_page.card_items()
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        checkout_page.checkout().click()
        log.info("Make a checkout")
        confirm_page = checkout_page.checkout_verify()
        confirm_page.check_country().send_keys("ind")
        log.info("Entering country name")
        self.explicit_wait('India')

        confirm_page.country_results().click()
        confirm_page.checkbox_mark().click()
        confirm_page.purchase_button().click()
        success = confirm_page.check_alert_success().text
        log.info("Check Success status" + success)
        assert "Success" in success

        self.driver.get_screenshot_as_file("screen.png")

        print(success)
