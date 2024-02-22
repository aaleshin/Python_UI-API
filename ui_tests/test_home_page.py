import pytest
from misc.generators import generate_random_string
from ui_tests.page_objects.home_page_objects import HomePage
from hamcrest import assert_that, contains_string, equal_to


@pytest.mark.ui
class TestHomePage:

    @pytest.mark.parametrize("email, notification, expected_result",
                             [("test@@@@@@@@mail.@@ru", HomePage.WRONGEMAIL, "Wrong email address"),
                              ("", HomePage.EMPTYFIELD, "Empty field"),
                              (("ASKQA" + generate_random_string() + "@mail.ru"), "success", "SEE YA SOON!")])
    def test_email_notification(self, email, notification, expected_result, driver):
        home_page = HomePage(driver, HomePage.base_url)
        home_page.open()
        home_page.click_to_element(HomePage.ACCEPT)
        if len(email) > 0:
            home_page.input_email(email)
        home_page.click_to_element(HomePage.APPLY)
        if notification is "success":
            assert_that(home_page.accept_email(), equal_to(expected_result))
        else:
            assert_that(home_page.get_email_error(notification), equal_to(expected_result))

