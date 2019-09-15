
class BasePage(object):

	driver=None
	url=''

	def __init__(self,driver):
		self.driver=driver

	def nagative(self):
		self.driver.get(url)

	def by_uiautomator_by_text(self,text):
		ttext='UiSelector().text("'+text+'")'
		print (ttext)
		return self.driver.find_element_by_android_uiautomator(ttext)

	def by_class(self,class_name):
		return self.driver.find_element_by_class_name(class_name)

	def by_uiautomator_by_id(self,the_id):
		iid='UiSelector().resourceId("'+the_id+'")'
		print (iid)
		return self.driver.find_element_by_android_uiautomator(iid)


	def by_id(self,the_id):
		return self.driver.find_element_by_id(the_id)

	def by_accessibility_id(self,the_id):
		return self.driver.find_element_by_accessibility_id(the_id)

	def eles_by_id(self,the_id):
		return self.driver.find_elements_by_id(the_id)
		

