from pages.base_page import BasePage 

class AccountPage(BasePage):

	def __init__(self,driver):
		super(AccountPage,self).__init__(driver)

#---------------------------以下是登录态-----------------------------------

	def nick_name(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/nickname')

	def follow_btn(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/follow')

	def fans_btn(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/fans')

	def integral_btn(self):
		return self.by_uiautomator_by_id('cn.com.open.mooc:id/integral')

	def shopping_cart(self):
		return self.by_uiautomator_by_text('购物车')

	def my_order(self):
		return self.by_uiautomator_by_text('我的订单')

	def setup(self):
		return self.by_uiautomator_by_text('设置')

#---------------------------以下是未登录--------------------------------
	
	def click_login(self):
		return self.by_uiautomator_by_text('点击登录')