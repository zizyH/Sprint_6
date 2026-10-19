import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.urls import Urls


class MainPage(BasePage):
    URL = Urls.BASE_URL

    ORDER_BUTTON_TOP    = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[text()='Заказать'])[2]")
    COOKIE_BUTTON       = (By.ID, "rcc-confirm-button")

    @allure.step("Открыть главную страницу и принять cookies")
    def open(self):
        self.open_url(self.URL)
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BUTTON)).click()
        except Exception:
            pass

    @allure.step("Нажать кнопку 'Заказать' вверху страницы")
    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку 'Заказать' внизу страницы")
    def click_order_bottom(self):
        self.scroll_to(self.ORDER_BUTTON_BOTTOM)
        self.click(self.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть по вопросу FAQ #{index}")
    def click_faq_question(self, index: int):
        locator = (By.ID, f"accordion__heading-{index}")
        self.scroll_and_js_click(locator)

    @allure.step("Получить текст ответа FAQ #{index}")
    def get_faq_answer_text(self, index: int) -> str:
        locator = (By.ID, f"accordion__panel-{index}")
        return self.wait.until(EC.visibility_of_element_located(locator)).text