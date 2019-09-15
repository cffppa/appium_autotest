import unittest
from appium import webdriver
from pages.account_page import AccountPage 
from pages.setup_page import SetupPage 
from lib import common,login
import time


class  LoginCase(unittest.TestCase):

	caps=[]
	driver=None

	def setUp(self):
		print('start test')
		self.driver=common.set_driver()
		time.sleep(5)
	'''
	def test_login(self):

		username='18086039320'
		password='cff123456'
		login.login(self.driver,username,password)

		account_page=AccountPage(self.driver)
		nickname=account_page.nick_name().get_attribute('text')
		print(nickname)
		self.assertTrue('函数'in nickname)
	'''
	
	def test_logout(self):
		username='18086039320'
		password='cff123456'
		login.login(self.driver,username,password)
		time.sleep(3)

		common.swipe('up',self.driver)
		account_page=AccountPage(self.driver)
		account_page.setup().click()

		setup_page=SetupPage(self.driver)
		setup_page.logout_btn().click()
		setup_page.logout_alert_yes().click()

		name=setup_page.name().get_attribute('text')
		print(name)
		self.assertTrue('函数' not in name)




	def tearDown(self):
		print('end test')
		#self.driver.quit()


if __name__=='__main__':
	unittest.main()





