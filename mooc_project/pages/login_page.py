from pages.base_page import BasePage 
import time

class LoginPage(BasePage):

	def __init__(self,driver):
		super(LoginPage,self).__init__(driver)

	def welcome_login(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/tv_welcom_login')

	def  username(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/accountEdit')

	def password(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/passwordEdit')

	def login_btn(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/login')

	def login_by_phone_msg(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/tv_login_by_phone_msg')

	def forget_pass(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/forget_label')

	def register(self):
		return self.by_uiautomator_by_text('注册')

	def login(self,username,password):
		self.username().clear()
		self.username().send_keys(username)
		time.sleep(1)
		self.password().send_keys(password)
		time.sleep(1)
		self.login_btn().click()
		time.sleep(1)