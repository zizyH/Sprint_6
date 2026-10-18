import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


order_data = [
    {
        "name": "Даша",
        "surname": "Дарьева",
        "address": "Москва, Вербная 8с1",
        "metro": "Бульвар Рокоссовского",
        "phone": "89991234567",
        "date": "07.10.2026",
        "period": "трое суток",
        "color": "grey",
        "comment": "позвоните перед приездом",
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "address": "Москва, Тверская 1",
        "metro": "Черкизовская",
        "phone": "89997654321",
        "date": "08.10.2026",
        "period": "двое суток",
        "color": "black",
        "comment": "домофон 123",
    },
]


@pytest.mark.parametrize("entry", ["top", "bottom"])
@pytest.mark.parametrize("data", order_data)
def test_order_scooter_success(driver, entry, data):
    main = MainPage(driver)
    main.open()
    if entry == "top":
        main.click_order_top()
    else:
        main.click_order_bottom()

    order = OrderPage(driver)
    order.fill_first_form(
        data["name"], data["surname"], data["address"], data["metro"], data["phone"]
    )
    order.fill_second_form(
        data["date"], data["period"], data["color"], data["comment"]
    )
    order.confirm_order()

    assert "Заказ оформлен" in order.get_success_text()