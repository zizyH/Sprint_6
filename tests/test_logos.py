from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


def test_logo_scooter_redirects_to_main_from_order_page(driver):
   
    main = MainPage(driver)
    main.open()
    main.click_order_top()             

    order = OrderPage(driver)
    order.click_logo_scooter()         

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url.rstrip("/") == MainPage.URL.rstrip("/")
    )
    assert driver.current_url.rstrip("/") == MainPage.URL.rstrip("/")


def test_logo_yandex_opens_new_tab(driver):
    main = MainPage(driver)
    main.open()

    initial_windows = len(driver.window_handles)
    main.click_logo_yandex()

    WebDriverWait(driver, 10).until(
        lambda d: len(d.window_handles) > initial_windows
    )
    driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != "about:blank"
    )
    
    assert ("ya.ru" in driver.current_url) or ("dzen.ru" in driver.current_url)