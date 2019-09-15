from pages.base_page import BasePage 

class SetupPage(BasePage):

	def __init__(self,driver):
		super(SetupPage,self).__init__(driver)

	def clear_cache(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/clear')

	def player_setup(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/player_setting')

	def logout_btn(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/logout_label')

	def logout_alert_yes(self):
		return self.by_id('cn.com.open.mooc:id/positiveBtn')


#未登录态：
	def  click_login_btn(self):
		return self.by_id('cn.com.open.mooc:id/login_btn')


	def name(self):
		return self.by_id('cn.com.open.mooc:id/nickname_tv')