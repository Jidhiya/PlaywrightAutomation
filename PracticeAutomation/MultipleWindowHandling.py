import re
from playwright.sync_api import Playwright, sync_playwright, expect


def stepsForMyExecution(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login")
    page.get_by_role("textbox", name="Username").fill("student")
    page.get_by_role("textbox", name="Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()
    page.locator("//a[text()='Courses']").click()
    with page.expect_popup() as newPageValues:
        page.get_by_role("link", name="Selenium WebDriver: Selenium Automation Testing with Java").click()

    page1 = newPageValues.value
    page1.wait_for_selector("//span[text()='Premium']", timeout =60000)
    
    with page.expect_popup() as secondPageValues:
        page.locator("//a[text()='Selenium WebDriver: Selenium Automation Testing with Python']").click()

    page1.bring_to_front()
    page.wait_for_timeout(4000)
    page2 = secondPageValues.value
    page2.wait_for_selector("//h1[text()='Selenium WebDriver: Selenium Automation Testing with Python']",timeout=40000)
    expect(page1.locator("//span[text()='Plans & Pricing']")).to_be_visible()

    
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    stepsForMyExecution(playwright)