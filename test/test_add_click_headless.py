from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import headless


def test_click_incognito(headless):
    headless.get("https://the-internet.herokuapp.com/floating_menu#home")
    wait = WebDriverWait(headless, 7)

    menu_item_locators = [
        (By.XPATH, "//a[text()='Home']"),
        (By.XPATH, "//a[text()='News']"),
        (By.XPATH, "//a[text()='Contact']"),
        (By.XPATH, "//a[text()='About']")
    ]

    for menu_item_locator in menu_item_locators:
        menu_item = wait.until(EC.presence_of_element_located(menu_item_locator))
        menu_item.click()
        assert "floating_menu" in headless.current_url.lower()
