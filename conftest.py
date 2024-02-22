import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     rep = outcome.get_result()
#     marker = item.get_closest_marker("ui")
#     if marker:
#         if rep.when == 'call' and rep.failed:
#             try:
#                 allure.attach(item.instance.driver.get_screenshot_as_png(),
#                               name=item.name,
#                               attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 print(f'Fail to take screen-shot: {e}')


@pytest.fixture(scope='function')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()



