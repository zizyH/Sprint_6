from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")
    LOGO_YANDEX  = (By.XPATH, "//a[contains(@class,'Header_LogoYandex')]")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    def click_logo_scooter(self):
        self.click(self.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(self.LOGO_YANDEX)