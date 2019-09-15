from appium import webdriver
import time
import os

file=open('aa.txt','w')

def caps():
	desired_caps={}
	desired_caps['platformName']='Android'
	desired_caps['platformVersion']='7.0'
	desired_caps['deviceName']='5c609f8e'
	#desired_caps['app']='F:\\imooc.apk'  #安装的时候需要这一条
	desired_caps['appPackage']='cn.com.open.mooc'
	desired_caps['appActivity']='com.imooc.component.imoocmain.splash.MCSplashActivity'
	desired_caps['noReset']='true'
	return desired_caps

dr=webdriver.Remote('http://localhost:4723/wd/hub',caps())

#获取屏幕的宽高
def get_size(dr):
	width=dr.get_window_size()['width']
	height=dr.get_window_size()['height']
	return width,height

#左滑
def swipe_left():
	x=get_size(dr)[0]/10*9 #(宽度的9/10)
	x1=get_size(dr)[0]/10 #(屏幕宽度的1/10)
	y=get_size(dr)[1]/2 #(高度的1/2)	
	dr.swipe(x,y,x1,y)

#右滑
def swipe_right():
	x=get_size(dr)[0]/10 #(屏幕宽度的1/10)
	x1=get_size(dr)[0]/10*9 #(宽度的9/10)
	y=get_size(dr)[1]/2	
	dr.swipe(x,y,x1,y)

#上滑
def swipe_up():
	x=get_size(dr)[0]/2
	y=get_size(dr)[1]/10*9
	y1=get_size(dr)[1]/10
	dr.swipe(x,y,x,y1)

#下滑
def swipe_down():
	x=get_size(dr)[0]/10
	x1=get_size(dr)[0]/10*9
	y=get_size(dr)[1]/2
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

def go_login():
	login_btn_1=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/right_text")')
	print(login_btn_1)
	login_btn_1.click()

def login(username,password):
	user_input=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/accountEdit")')
	user_input.send_keys(username)
	password_input=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/passwordEdit")')
	password_input.send_keys(password)
	login_btn_2=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/login")')
	login_btn_2.click()


#判断元素是否存在：
def is_element_exist(ele):
	print(ele)
	source=dr.page_source
	#file.write(source)   这一步是把source写入到txt文件中方便我调试之前出现的问题。
	#print(source)
	if ele in source:
		print('is  existed')
		return True		
	else:
		print('is not exist')
		return False
#-----------------------------------------以下代码段，设置'noreset'=true后不需要了--------------------------------------------------------------------
'''	
#滑动轮播图
swipe_on('left')
time.sleep(2)

swipe_on('right')
time.sleep(2)
swipe_on('up')
time.sleep(2)
swipe_on('down')
time.sleep(2)

swipe_on('left')
time.sleep(2)
swipe_on('left')
time.sleep(2)
swipe_on('left')
time.sleep(2)


print(dr.contexts)
print(dr.current_context)


#立即体验页面NAF=true不能定位，通过点击父控件来定位
ele=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/viewpager")')
ele.click()


#跳过按钮
skip_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/tvSkip")')
skip_btn.click()
'''
#----------------------------------------------以上代码段，设置'noreset'=true后不需要了-----------------------------------------------------------

#"我的"

account_btn=dr.find_element_by_accessibility_id('账号')
account_btn.click()



username='18086039320'
password='cff123456'

#dr.find_element_by_android_uiautomator('UiSelector().resourceId(\"cn.com.open.mooc:id/nickname\")')
flag=is_element_exist("cn.com.open.mooc:id/nickname")
print(flag)
if flag is False:
	login_btn=dr.find_element_by_android_uiautomator('UiSelector().text("点击登录")')
	login_btn.click()
	login(username,password)
else:
	swipe_on('up')
	time.sleep(1)
	set_btn=dr.find_element_by_android_uiautomator('UiSelector().text("设置")')
	set_btn.click()
	logout_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/logout")')
	logout_btn.click()
	confirm_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/positiveBtn")')
	confirm_btn.click()
	dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/login_btn")').click()
	login(username,password)

		
'''
#注册页面
register_phone=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/et_phone_edit")')
register_phone.send_keys('18686039320')

register_next=dr.find_element_by_android_uiautomator('UiSelector().resourceId("cn.com.open.mooc:id/over")')
register_next.click()
'''





