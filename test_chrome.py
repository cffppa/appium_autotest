from selenium import webdriver
from appium import webdriver
import time

#from selenium.webdriver.remote.switch_to import SwitchTo

#from .mobilecommand import MobileCommand



desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.android.chrome'
desired_caps['appActivity']='com.google.android.apps.chrome.Main'

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print(dr.current_context)   #当前上下文。源代码见https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/context.py
print(dr.current_activity)
print(dr.current_package)
print(dr.battery_info)

'''
def switch_h5():
	dr.execute(MobileCommand.SWITCH_TO_CONTEXT,{"name":"WEBVIEW_chrome"})

def switch_app():
	dr.execute(MobileCommand.SWITCH_TO_CONTEXT,{"name":'NATIVE_app'})
'''


checkbox=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.chrome:id/send_report_checkbox")')
checkbox.click()
time.sleep(1)
accept_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.chrome:id/terms_accept")')
accept_btn.click()
time.sleep(2)
nothanks_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.chrome:id/negative_button")')
nothanks_btn.click()
time.sleep(2)

#进入谷歌页面输入url
url='www.baidu.com'
url_text_area=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.chrome:id/search_box_text")')
url_text_area.send_keys(url)
#submit_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.chrome:id/recent_tabs_button")')
#submit_btn.click()
dr.keyevent(66) #点击键盘上的回车键
time.sleep(3)
print(dr.current_context)
print (dr.contexts)
#切换到H5页面(以下代码段没运行通过)：
'''
context=dr.contexts[-1]
dr.switch_to.context(context)
print(dr.current_context)
print(dr.page_source)
time.sleep(10)
dr.find_element_by_id('index-kw').send_keys('hahahah')
time.sleep(10)
'''

dr.quit()

