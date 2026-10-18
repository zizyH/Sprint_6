from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    NAME    = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO   = (By.XPATH, "//input[@placeholder='* Станция метро']")
    
    
    METRO_OPTION = (By.XPATH, "//li[contains(@class,'select-search__row')] | //div[contains(@class,'select-search__option')] | //button[contains(@class,'select-search__option')]")
    
    PHONE   = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    
    DATE        = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, "//div[contains(@class,'Dropdown-root')]")
    RENT_OPTION = (By.XPATH, "//div[contains(@class,'Dropdown-option')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY  = (By.ID, "grey")
    COMMENT     = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    
   
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Content')]//button[text()='Заказать']")
    YES_BUTTON   = (By.XPATH, "//button[text()='Да']")

    
    SUCCESS_HEADER = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")

    def fill_first_form(self, name, surname, address, metro, phone):
        
        self.find(self.NAME).send_keys(name)
        self.find(self.SURNAME).send_keys(surname)
        self.find(self.ADDRESS).send_keys(address)

        
        self.click(self.METRO)
        self.find(self.METRO).send_keys(metro)
        
       
        self.wait.until(EC.visibility_of_element_located(self.METRO_OPTION))
        
        metro_item = (By.XPATH, f"//*[contains(@class, 'select-search__row') or contains(@class, 'select-search__option')][contains(., '{metro}')]")
        self.click(metro_item)
        self.find(self.PHONE).send_keys(phone)
        self.click(self.NEXT_BUTTON)

    def fill_second_form(self, date, period, color, comment):
        date_input = self.find(self.DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.click(self.RENT_PERIOD)
        options = self.driver.find_elements(*self.RENT_OPTION)
        for opt in options:
            if period in opt.text:
                opt.click()
                break

        self.click(self.COLOR_BLACK if color == "black" else self.COLOR_GREY)
        self.find(self.COMMENT).send_keys(comment)

    def confirm_order(self):
        self.click(self.ORDER_BUTTON)   
        self.click(self.YES_BUTTON)     

    def get_success_text(self):
        return self.get_text(self.SUCCESS_HEADER)