#coding=utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time


def get_driver():
	desired_caps={}
	desired_caps['platformName']='Android'
	desired_caps['platformVersion']='7.0'
	desired_caps['deviceName']='5c609f8e'
	desired_caps['app']='F:\\mobileqq_android.apk'
	desired_caps['appActivity']='com.tencent.mobileqq.activity.SplashActivity'
	desired_caps['appPackage']='com.tencent.mobileqq'
	#desired_caps['adbExecTimeout']='50000'
	dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


dr=get_driver()

try:
	WebDriverWait(dr,240).until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/dialogRightBtn')))
	#accept_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/dialogRightBtn")')
	dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/dialogRightBtn")').click()
except:
	print('element not found')

login_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/btn_login")')
login_btn.click()

username='709537875'
password='Cff_8187_Cisco'

user_input=dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱')
user_input.click()
time.sleep(2)
user_input.send_keys(username)
time.sleep(2)
pass_input=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/password")')
pass_input.send_keys(password)
time.sleep(2)
submit_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/login")')
submit_btn.click()
time.sleep(2)

close_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/ivTitleBtnRightText")')
close_btn.click()

#获取屏幕的宽高
def get_size():
	dr=get_driver()
	width=dr.get_window_size()['width']
	height=dr.get_window_size()['height']
	return width,height

#左滑
def swipe_left():
	x=get_size()[0]/10*9 (宽度的9/10)
	x1=get_size()[0]/10 (屏幕宽度的1/10)
	y=get_size()[1]/2 (高度的1/2)	
	dr.swipe(x,y,x1,y)

#右滑
def swipe_right():
	x=get_size()[0]/10 (屏幕宽度的1/10)
	x1=get_size()[0]/10*9 (宽度的9/10)
	y=get_size()[1]/2	
	dr.swipe(x,y,x1,y)

#上滑
def swipe_up():
	x=get_size()[0]/2
	y=get_size()[1]/10*9
	y1=get_size()[1]/10
	dr.swipe(x,y,x,y1)

#下滑
def swipe_down():
	x=get_size()[0]/10
	x1=get_size()[0]/10*9
	y=get_size()[1]/2
	dr.swipe(x,y,x1,y)

def swipe_on(direction):
	if direction=='up':
		swipe_up()
	elif direction=='down':
		swipe_down()
	elif direction=='left':
		swipe_left()
	else:
		swipe_right()



#dr.quit()