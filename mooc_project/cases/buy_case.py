from appium import webdriver
import time
from pages.navigation_bar import Navigation 
from pages.home_page import HomePage 
from lib import common,login
import unittest

class BuyCase(unittest.TestCase):

	driver=None

	def setUp(self):
		print('start test')
		self.driver=common.set_driver()

	def test_buy(self):

		username='18086039320'
		password='cff123456'
		login.login(self.driver,username,password)

		navigation_bar=Navigation(self.driver)
		navigation_bar.home_page_btn().click()

		home_page=HomePage(self.driver)
		common.taphit(self.driver,[(60,603),(300,682)])
		time.sleep(10)



	def tearDown(self):
		print('end test')
		self.driver.quit()

if __name__=='__main__':
	unittest.main()
