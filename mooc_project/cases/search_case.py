from appium import webdriver
from lib import common,login
from pages.home_page import HomePage 
from pages.search_page import SearchPage 
import time
import unittest

class SearchCase(unittest.TestCase):

	driver=None

	def setUp(self):
		print('start test')
		self.driver=common.set_driver()

	def test_search(self):

		login.welcome(self.driver)

		keywords='python'
		home_page=HomePage(self.driver)
		home_page.search_box().click()
	
		search_page=SearchPage(self.driver)
		search_page.search_box().click()
		search_page.search_box().send_keys(keywords)
		search_page.search_btn().click()

		result=search_page.result_numbers().get_attribute('text')
		print(result)
		result_1=search_page.results()[0].get_attribute('text')
		print(result_1)
		self.assertTrue('Python' in result_1 or 'python' in result_1)
		time.sleep(4)


	def tearDown(self):
		print('end test')
		self.driver.quit()	

if __name__=='__main__':
	unittest.main()
