from pages.base_page import BasePage 

class HomePage(BasePage):

	def __init__(self,driver):
		super(HomePage,self).__init__(driver)

	def login_btn(self):
		return self.by_id('cn.com.open.mooc:id/ivOperation')

	def search_box(self):
		return self.by_id('cn.com.open.mooc:id/tvKeywords')