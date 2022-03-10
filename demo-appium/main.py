import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Test Device',
    'appActivity': 'com.example.android.contactmanager.ContactManager',
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# opens app
driver.start_activity("com.example.android.contactmanager", "ContactManager")

time.sleep(1)

# press on element
driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Contact").click()

time.sleep(1)

assert driver.find_element(MobileBy.ID, "com.example.android.contactmanager:id/contactNameEditText").is_displayed()

# write in element
driver.find_element(MobileBy.ID, "com.example.android.contactmanager:id/contactNameEditText").send_keys('asdf')

time.sleep(1)

driver.quit()
