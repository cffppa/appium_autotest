from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction 
import time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.0'

#这是模拟器。。。。。
desired_caps['deviceName']='Android Emulator'
#desired_caps['app']='Calculator.apk'
desired_caps['appPackage']='com.android.calculator2'
desired_caps['appActivity']='.Calculator'
'''
#这是真机 运行未通过哦！
desired_caps['deviceName']='5c609f8e'
desired_caps['appPackage']='com.miui.calculator'
desired_caps['appActivity']='.cal.CalculatorActivity'
'''

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print(dr.current_context)   #当前上下文。源代码见https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/context.py
print(dr.current_activity)
print(dr.current_package)
#print(dr.battery_info)
#dr.background_app(5)  #app后台运行时间5秒。源码见：https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/applications.py

#用webdriver的方法找元素
#btns=dr.find_elements_by_class_name('android.widget.Button')  #找到所有的button
#delete_btn=btns[0]
#delete_btn.click()


#按键6、+号、1：通过uiautomator的uiselector的resource_id定位
btn_0=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/digit_0")')

btn_1=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/digit_1")')

btn_3=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/digit_3")')

btn_6=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/digit_6")')

add_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/op_add")')

time.sleep(5)

#按键：通过uiautomator的uiselector的description定位：
#delete_btn=dr.find_element_by_android_uiautomator('UiSelector().description("delete")')
#按键+-*/号：通过uiautomator的uiselector的text定位：
add_btn=dr.find_element_by_android_uiautomator('UiSelector().text("+")')
sub_btn=dr.find_element_by_android_uiautomator('UiSelector().text("−")')
mul_btn=dr.find_element_by_android_uiautomator('UiSelector().text("×")')
div_btn=dr.find_element_by_android_uiautomator('UiSelector().text("÷")')
equ_btn=dr.find_element_by_android_uiautomator('UiSelector().text("=")')

#显示区域：com.android.calculator2:id/formula
result=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.calculator2:id/result")')




#加法：
btn_1.click()
btn_6.click()
add_btn.click()
btn_3.click()
equ_btn.click()
time.sleep(3)
print(result.get_attribute('text'))
assert(result.get_attribute('text')=='19')
#减法：
btn_1.click()
btn_6.click()
sub_btn.click()
btn_3.click()
equ_btn.click()
time.sleep(3)
assert(result.get_attribute('text')=='13')

#乘法
btn_6.click()
btn_1.click()
mul_btn.click()
btn_0.click()
equ_btn.click()
time.sleep(3)
assert(result.get_attribute('text')=='0')

#除法
btn_6.click()
btn_6.click()
div_btn.click()
btn_0.click()
equ_btn.click()
time.sleep(3)
#assert(result.get_attribute('text')==?)



dr.close_app()     #源码：https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/applications.py
#dr.lock()
dr.quit()