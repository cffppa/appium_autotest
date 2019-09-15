#coding=utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'
desired_caps['deviceName']='5c609f8e'
desired_caps['app']='F:\\mobileqq_android.apk'
desired_caps['appActivity']='com.tencent.mobileqq.activity.SplashActivity'
desired_caps['appPackage']='com.tencent.mobileqq'
#desired_caps['adbExecTimeout']='50000'
dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


accept_btn_1=dr.find_element_by_android_uiautomator('UiSelector().text("允许")')
accept_btn_1.click()
accept_btn_2=dr.find_element_by_android_uiautomator('UiSelector().text("允许")')
accept_btn_2.click()


try:
	WebDriverWait(dr,120).until(EC.presence_of_element_located((By.ID,'com.tencent.mobileqq:id/dialogRightBtn')))
	#accept_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/dialogRightBtn")')
	dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.tencent.mobileqq:id/dialogRightBtn")').click()
except:
	print('element not found')

login_btn=dr.find_element_by_id('com.tencent.mobileqq:id/btn_login')
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





#dr.quit()