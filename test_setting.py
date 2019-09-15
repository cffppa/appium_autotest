from appium import webdriver
import time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='10'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='.Settings'

dr=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#设置网路--------------------------------------------------------------------------
net_set_btn=dr.find_element_by_android_uiautomator('UiSelector().text("Network & internet")')
net_set_btn.click()

switch_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.settings:id/switchWidget")')
if switch_btn.get_attribute('text')=='OFF':
	switch_btn.click()
	assert(switch_btn.get_attribute('text')=='ON')
else:
	wifi_btn=dr.find_element_by_android_uiautomator('UiSelector().text("Wi‑Fi")')
	wifi_btn.click()
	time.sleep(10)
	addnet_btn=dr.find_element_by_android_uiautomator('UiSelector().text("Add network")')
	addnet_btn.click()
	time.sleep(3)
	net_name='kingjay'
	ssid_enter_textare=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.settings:id/ssid")')
	ssid_enter_textare.send_keys(net_name)
	security='cjj9861@cisco'
	security_btn=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.settings:id/security")')
	security_btn.click()
	wpa_btn=dr.find_element_by_android_uiautomator('UiSelector().text("WPA/WPA2-Personal")')
	wpa_btn.click()
	password=dr.find_element_by_android_uiautomator('UiSelector().resourceId("com.android.settings:id/password")')
	password.send_keys(security)
	save_btn=dr.find_element_by_android_uiautomator('UiSelector().text("Save")')
	save_btn.click()



#设置显示亮度-----------------------------------------------------------------------


#设置声音--------------------------------------------------------------------------