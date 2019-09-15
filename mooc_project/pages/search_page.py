from pages.base_page import BasePage 

class SearchPage(BasePage):

	def __init__(self,driver):
		super(SearchPage,self).__init__(driver)


	def search_box(self):
		return self.by_id('cn.com.open.mooc:id/et_edit_content')


	def search_btn(self):
		return self.by_id('cn.com.open.mooc:id/iv_search_icon')

	def search_clear(self):
		return self.by_id('cn.com.open.mooc:id/tv_remote_history')

	def result_numbers(self):
		return self.by_id('cn.com.open.mooc:id/tv_numbers')


	def results(self):
		return self.eles_by_id('cn.com.open.mooc:id/name')