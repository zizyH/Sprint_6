import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from config.urls import Urls


@allure.feature("Logos")
class TestLogos:

    def test_logo_scooter_redirects_to_main_from_order_page(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_order_top()

        order = OrderPage(driver)
        order.click_logo_scooter()

        order.wait_for_url(Urls.BASE_URL)
        assert order.get_current_url().rstrip("/") == Urls.BASE_URL.rstrip("/")

    def test_logo_yandex_opens_new_tab(self, driver):
        main = MainPage(driver)
        main.open()

        initial_windows = main.get_window_handles()
        main.click_logo_yandex()

        main.wait_for_new_window(len(initial_windows))
        main.switch_to_last_window()
        main.wait_for_real_url()

        current = main.get_current_url()
        assert ("ya.ru" in current) or ("dzen.ru" in current)