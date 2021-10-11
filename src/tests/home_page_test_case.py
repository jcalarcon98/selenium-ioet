from src.pom.home_page import HomePage
from src.tests.base_test_case import BaseTestCase


class HomePageTestCase(BaseTestCase):

    def test_title_verification(self):
        home_page_pom = HomePage(self.web_driver)
        home_page_title = home_page_pom.get_title()
        self.assertIsNotNone(home_page_title)
