from appium import webdriver
from pages.navigation_bar import Navigation
from pages.classify_page import ClassifyPage
import unittest
import time
from lib import login,common


class ClassifyCase(unittest.TestCase):

	driver=None

	def setUp(self):
		print('start test')
		self.driver=common.set_driver()

	def test_classify(self):
		login.welcome(self.driver)

		navigation_bar=Navigation(self.driver)
		navigation_bar.classify_btn().click()
	
		classify_page=ClassifyPage(self.driver)
		lists=classify_page.lists()


		#classify_page.get_classify_data()
		self.assertTrue(lists[0].get_attribute('text')='前端开发')



	def tearDown(self):
		print('end test')
		#self.driver.quit()

if __name__=='__main__':
	unitttest.main()	
