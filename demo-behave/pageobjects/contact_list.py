from appium.webdriver.common.mobileby import MobileBy


class ContactListPageObject(object):

    def __init__(self, driver):
        self.show_all_check = driver.find_element(MobileBy.ID, "com.example.android.contactmanager:id/showInvisible")

    def show_all_contacts(self):
        self.show_all_check.click()
