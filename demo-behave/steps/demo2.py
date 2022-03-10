import time

from appium.webdriver.common.mobileby import MobileBy
from behave import *

from pageobjects.contact_list import ContactListPageObject


@given("the user access list of contacts")
def step_impl(context):
    context.driver.start_activity("com.example.android.contactmanager", "ContactManager")


@when('the user press "Add Contact"')
def step_impl(context):
    context.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Add Contact").click()

    time.sleep(1)


@step('the user enters "Contact Name"')
def step_impl(context):
    context.contact_name = 'Alejandro'

    context.driver.find_element(
        MobileBy.ID, "com.example.android.contactmanager:id/contactNameEditText").send_keys(context.contact_name)


@step('the user enters "Contact Phone"')
def step_impl(context):
    context.contact_phone = '987654321'

    context.driver.find_element(
        MobileBy.ID, "com.example.android.contactmanager:id/contactPhoneEditText").send_keys(context.contact_phone)


@step('the user press "Save"')
def step_impl(context):
    context.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Save").click()

    time.sleep(1)


@then("the contact appears in the list")
def step_impl(context):
    ContactListPageObject(context.driver).show_all_contacts()

    contacts = context.driver.find_elements(MobileBy.XPATH, '//android.widget.TextView[@content-desc="false"]')

    assert [contact for contact in contacts if contact.text == context.contact_name], 'Contact not in list'

