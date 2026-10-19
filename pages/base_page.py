import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX  = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)


    @allure.step("Найти элемент: {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Найти все элементы: {locator}")
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проскроллить к элементу: {locator}")
    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Проскроллить и JS-кликнуть по элементу: {locator}")
    def scroll_and_js_click(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    

    @allure.step("Открыть URL: {url}")
    def open_url(self, url: str):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Дождаться URL: {expected_url}")
    def wait_for_url(self, expected_url: str, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url.rstrip("/") == expected_url.rstrip("/")
        )

    @allure.step("Получить список окон браузера")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Дождаться появления нового окна")
    def wait_for_new_window(self, initial_count: int, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > initial_count
        )

    @allure.step("Переключиться на последнее открытое окно")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться, пока URL перестанет быть about:blank")
    def wait_for_real_url(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.current_url != "about:blank"
        )


    @allure.step("Кликнуть по логотипу Scooter")
    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    @allure.step("Кликнуть по логотипу Yandex")
    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)