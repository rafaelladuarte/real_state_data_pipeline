from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class WebScraper:
    def __init__(self):
        self.driver = self.config_driver()

    def get_driver(self, url):
        self.driver.get(url)

    def config_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('--disable-gpu')
        options.add_experimental_option(
            "excludeSwitches",
            ["enable-automation"]
        )
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options)

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True
        )

        return driver

    def scroll_until_element_stops_moving(
            self,
            css_selector,
    ):
        previous_location = None
        attempts = 0

        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

        while attempts < 10:
            location = element.location_once_scrolled_into_view

            if previous_location is not None and location == previous_location:
                print("O elemento parou de se mover.")
                break

            self.driver.execute_script(
                "arguments[0].scrollIntoView();",
                element
            )
            sleep(5)

            previous_location = location
            attempts += 1
            print(f"Tentativa {attempts}: elemento movido para {location}")

    def get_elements(
        self,
        by: By,
        path: str,
        driver_element: webdriver = None
    ):
        try:
            if driver_element:
                elements = WebDriverWait(driver_element, 10).until(
                    EC.presence_of_all_elements_located((by, path))
                )
            else:
                elements = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((by, path))
                )
        except TimeoutException:
            return None

        return elements

    def get_element(
        self,
        by: By,
        path: str,
        attribute_type: str = None,
        driver_element: webdriver = None,
        timeout=10
    ):
        try:
            if driver_element:
                element = WebDriverWait(driver_element, timeout).until(
                    EC.presence_of_element_located((by, path))
                )
            else:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, path))
                )
            if attribute_type == "text":
                return element.text
            elif attribute_type == "href":
                return element.get_attribute("href")
            elif attribute_type == "button":
                element.click()
        except TimeoutException:
            return None

        return element

    def close_driver(self):
        self.driver.quit()
