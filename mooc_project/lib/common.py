import time
from appium import webdriver

def set_driver():
	desired_caps={}
	desired_caps['platformName']='Android'
	desired_caps['platformVersion']='7.0'
	desired_caps['deviceName']='5c609f8e'
	desired_caps['appPackage']='cn.com.open.mooc'
	desired_caps['appActivity']='com.imooc.component.imoocmain.splash.MCSplashActivity'
	desired_caps['newCommandTimeout']='360'
	driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
	return driver


def get_window_size(driver):
	width=driver.get_window_size()['width']
	height=driver.get_window_size()['height']
	return width,height

def swipe_up(driver):
	x=get_window_size(driver)[0]*0.5
	y=get_window_size(driver)[1]*0.9
	y1=get_window_size(driver)[1]*0.1
	driver.swipe(x,y,x,y1)

def swipe_down(driver):
	x=get_window_size(driver)[0]/2
	y=get_window_size(driver)[1]/10
	y1=get_window_size(driver)[1]/2
	driver.swipe(x,y,x,y1)

def swipe_left(driver):
	x=get_window_size(driver)[0]*0.9
	x1=get_window_size(driver)[0]*0.1
	y=get_window_size(driver)[1]/2
	driver.swipe(x,y,x1,y)

def swipe_right(driver):
	x=get_window_size(driver)[0]/10
	x1=get_window_size(driver)[0]/2
	y=get_window_size(driver)[1]/2
	driver.swipe(x,y,x1,y)

def swipe(direction,driver):
	if 'up' in direction:
		swipe_up(driver)
	elif 'down' in direction:
		swipe_down(driver)
	elif 'left' in direction:
		swipe_left(driver)
	else:
		swipe_right(driver)

def is_element_exist(ele):
	source=driver.page_source
	if ele in source:
		print('this element is existed')
		return True
	else:
		print('this element is not exist')
		return False

def taphit(driver,i):
	driver.tap(i,500)