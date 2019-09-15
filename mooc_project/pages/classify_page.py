from pages.base_page import BasePage 
import os

class ClassifyPage(BasePage):

	def __init__(self,driver):
		super(ClassifyPage,self).__init__(driver)


	def lists(self):
		classify_list=self.by_id('cn.com.open.mooc:id/rgClassify')
		lists=classify_list.find_elements_by_class_name('android.widget.RadioButton')
		print(lists)
		return lists

'''
	#这段函数功能是把对应的每个分类的名称写到文件里去。运行通过了，但是目标文件没有数据写入。
	def get_classify_data(self):
		path='F:\\code_new\\appium_autotest\\mooc_project\\data'
		dirs=os.listdir(path)
		data=open('classify_data.py','a')
		print(data.name)
		num1=len(self.lists())
		print(num1)
		for i in range(0,num1):
			self.lists()[i].click()
			titles=self.driver.find_elements_by_id('cn.com.open.mooc:id/tvTitle')
			num2=len(titles)
			for j in range(0,num2):
				title=titles[j].get_attribute('text')
				data.write(title+"  ")
			data.write('\n')
'''



