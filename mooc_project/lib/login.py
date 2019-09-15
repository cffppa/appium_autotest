from appium import webdriver
from pages.login_page import LoginPage 
from pages.navigation_bar import Navigation
from pages.account_page import AccountPage 
from pages.welcome_page import WelcomePage 
from pages.register_page import RegisterPage
from lib import common
import time

def welcome(driver):
	common.swipe('left',driver)
	time.sleep(2)
	common.swipe('left',driver)
	time.sleep(2)
	common.swipe('left',driver)
	time.sleep(2)

	welcome_page=WelcomePage(driver)
	welcome_page.experience_now_btn().click()
	welcome_page.skip_btn().click()

def login(driver,username,password):

	welcome(driver)
	
	navigation=Navigation(driver)
	navigation.account_btn().click()

	account_page=AccountPage(driver)
	account_page.click_login().click()

	register_page=RegisterPage(driver)
	register_page.login_btn().click()
	

	login_page=LoginPage(driver)
	login_page.login(username,password)
