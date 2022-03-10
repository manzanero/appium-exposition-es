from appium import webdriver


def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    if 'android_driver' in scenario.effective_tags:
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'appActivity': 'com.example.android.contactmanager.ContactManager',
        }
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    if 'android_driver' in scenario.effective_tags:
        context.driver.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
