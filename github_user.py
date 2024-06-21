import os

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GithubUser:
    def __init__(self):
        print('GithubUser __init__')
        self.browser = webdriver.Chrome()
        self.bLogin = False
        self.url = ''

    def login(self) -> None:
        self.__login__()

    def __login__(self) -> None:
        print('__login__')
        try:
            self.url = 'https://github.com/login'
            self.browser.get(self.url)

            timeout = 5  # seconds
            wait = WebDriverWait(self.browser, timeout)

            try:
                id_field_present = wait.until(EC.presence_of_element_located((By.ID, 'login_field')))
                print("field id ready!")

                id_field_present.send_keys(os.getenv('USERNAME'))

                password_field = self.browser.find_element(By.ID, 'password')
                password_field.send_keys(os.getenv('PASSWORD'))

                button_field = self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
                button_field_value = button_field.get_attribute('value')

                import re
                pattern = re.compile(r'\s+')
                button_field_value = re.sub(pattern, '', button_field_value)
                if button_field_value.lower() != 'signin':
                    raise Exception('button filed not found')

                button_field.click()

                self.browser.save_screenshot('outputs/main_page.png')

                self.logout()

            except TimeoutException:
                print("Loading took too much time!")

        except Exception as e:
            print(f'__login__ exception:: {e}')
        finally:
            print('__login__ finally')

    def logout(self) -> None:
        self.__logout__()

    def __logout__(self) -> None:
        print('__logout__')

        try:
            button_info = self.browser.find_element(By.CSS_SELECTOR, f'button[data-login="{os.getenv("USERNAME")}"]')
            button_info.click()

            self.browser.save_screenshot('outputs/button_info.png')

            logout_link = self.browser.find_element(By.CSS_SELECTOR, 'a[href="/logout"]')
            logout_link.click()

            self.browser.save_screenshot('outputs/logout.png')

        except Exception as e:
            print(f'__logout__ exception:: {e}')
        finally:
            print('__logout__ finally')

    def __del__(self):
        print('GithubUser __del__')
        self.browser.quit()

    @staticmethod
    def test() -> None:
        print('test static methods')
        pass
