from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.education-services.ru/"

    ORDER_BUTTON_TOP    = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")

    
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def open(self):
        self.driver.get(self.URL)
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except Exception:
            pass

    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        self.scroll_to(self.ORDER_BUTTON_BOTTOM)
        self.click(self.ORDER_BUTTON_BOTTOM)

  
    def click_faq_question(self, index: int):
        locator = (By.ID, f"accordion__heading-{index}")
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def get_faq_answer_text(self, index: int) -> str:
        locator = (By.ID, f"accordion__panel-{index}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text
