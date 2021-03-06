from django.utils import unittest
from noseselenium.cases import SeleniumTestCaseMixin


class ArchiveMonthTest(unittest.TestCase, SeleniumTestCaseMixin):

    selenium_fixtures = ['test_generated_model.json']
    url = '/test_app/generatedmodel/archive/2012/8/'

    def setUp(self):
        self.selenium.open(self.url)

    def test_ok(self):
        s = self.selenium
        self.failUnless(s.is_text_present('GeneratedModel Month Archive'))
        self.failUnless(s.is_text_present('Generated Model Fixture'))

    # FIXME
    # https://github.com/modocache/django-generate-scaffold/issues/2
    # def test_day_list(self):
    #     s = self.selenium
    #     s.click('link=Aug. 11, 2012')
    #     s.wait_for_page_to_load('30000')
    #     self.failUnless(s.is_text_present('GeneratedModel Day Archive'))

    def test_link_month_archive(self):
        s = self.selenium
        s.click('link=Month Archive')
        s.wait_for_page_to_load('30000')
        self.failUnless(s.is_text_present('GeneratedModel Month Archive'))

    def test_link_year_archive(self):
        s = self.selenium
        s.click('link=Year Archive')
        s.wait_for_page_to_load('30000')
        self.failUnless(s.is_text_present('GeneratedModel Year Archive'))

    def test_link_archive_index(self):
        s = self.selenium
        s.click('link=Archive Index')
        s.wait_for_page_to_load('30000')
        self.failUnless(s.is_text_present('GeneratedModel Archive Index'))
