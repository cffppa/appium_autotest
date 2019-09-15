from pages.base_page import BasePage 

class Navigation(BasePage):

	def __init__(self,driver):
		super(Navigation,self).__init__(driver)

	def home_page_btn(self):
		return self.by_uiautomator_by_text('首页')

	def classify_btn(self):
		return self.by_uiautomator_by_text('分类')

	def study_btn(self):
		return self.by_uiautomator_by_text('我的学习')

	def account_btn(self):
		return self.by_uiautomator_by_text('账号')