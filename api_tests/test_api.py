import os
import pytest
import requests
from hamcrest import *
from misc.generators import generate_random_string


@pytest.mark.api
class TestServerFunctionality:
    """
    Check negative and basic value
    """

    def setup_method(self):
        host = os.environ.get('TEST_HOST', 'cube.bluelight.inc')
        command = 'subs/Email'
        self.url = f'https://{host}/{command}'

    @pytest.mark.parametrize("email, expected_response_code, expected_response_body",
                             [(("ASKQA" + generate_random_string() + "@mail.ru"), 200, "true"),
                              ("wPLAINAdDRESs", 400, "Invalid email"),
                              ("@DOMAIN.COM", 400, "Invalid email"),
                              ("@«»‘~!@#$%^&*()?>,./\<][ /*<!—«»♣☺♂", 400, "Invalid email"),
                              ("JOE SMITH <EMAIL@DOMAIN.COM>", 400, "Invalid email"),
                              ("JOE SMITH <EMAIL@DOMAIN.COM>", 400, "Invalid email"),
                              ("EMAIL@DOMAIN@DOMAIN.COM", 400, "Invalid email"),
                              (".EMAIL@DOMAIN.COM", 400, "Invalid email"),
                              ("EMAIL.@DOMAIN.COM", 400, "Invalid email"),
                              ("@ EMAIL@.DOMAIN.COM", 400, "Invalid email"),
                              ("EMAIL..EMAIL@DOMAIN.COM", 400, "Invalid email"),
                              ("EMAIL@DOMAIN..COM", 400, "Invalid email"),
                              ("EMAIL@-DOMAIN.COM", 400, "Invalid email"),
                              ("EMAIL@111.222.333.44444", 400, "Invalid email"),
                              ("SELECT * FROM Users", 400, "Invalid email"),
                              ("<script>alert('XSS1')</script>", 400, "Invalid email"),
                              ("< form % 20 action =»http: // live.hh.ru» > < input % 20 type =»submit» > < / form >",
                               400, "Invalid email")])
    def test_bad_params(self, email, expected_response_code, expected_response_body):
        response = requests.post(self.url, files={("email", (None, email))})
        assert_that(response.status_code, equal_to(expected_response_code))
        assert_that(str(response.text), contains_string(expected_response_body))
