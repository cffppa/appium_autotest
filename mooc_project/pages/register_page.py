from pages.base_page import BasePage 

class RegisterPage(BasePage):

	def __init__(self,driver):
		super(RegisterPage,self).__init__(driver)

	def login_btn(self):
		return self.by_uiautomator_by_text('登录')