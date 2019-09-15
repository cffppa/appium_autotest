from pages.base_page import BasePage 

class WelcomePage(BasePage):
	
	def __init__(self,driver):
		super(WelcomePage,self).__init__(driver)

	def skip_btn(self):
		return self.by_id('cn.com.open.mooc:id/tvSkip')

	def experience_now_btn(self):
		return self.by_id('cn.com.open.mooc:id/viewpager')