from playwright.sync_api import sync_playwright, expect

def run(p):
    global browser
    global page
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    launchThePracticeAutomationWebsite()
    testLoginText = page.locator("//h2[text()='Test login']")
    validateTheVisibilityOfAnElement(testLoginText)
    userNameLocator = page.locator("input#username")
    validateTheVisibilityOfAnElement(userNameLocator)
    passWordLocator = page.locator("input#password")
    validateTheVisibilityOfAnElement(passWordLocator)
       
    
 
 
def launchThePracticeAutomationWebsite():
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.wait_for_load_state("networkidle",timeout=60000)
    expect(page).to_have_title("Test Login | Practice Test Automation")
 
def validateTheVisibilityOfAnElement(locator):
    expect(locator).to_be_visible()
 
def loginToTheWebsite(userNameValue, passWordValue):
    userNameLocator = page.locator("input#username")
    passWordLocator = page.locator("input#password")
    submitBtn = page.locator("button#submit")
    userNameLocator.fill(userNameValue)
    passWordLocator.fill(passWordValue)    
    submitBtn.click()
    page.wait_for_load_state("networkidle",timeout=60000)

def validUsernameAndPassword():
    loginToTheWebsite("student", "Password123")
    page.wait_for_timeout(4000)
    expect(page).to_have_title("Logged In Successfully | Practice Test Automation")
    
    

def invalidUserName():
    run(p)
    loginToTheWebsite("student1", "Password123")
    page.wait_for_timeout(4000)
    expect(page).to_have_title("Test Login | Practice Test Automation")


def invalidUPassword():
    run(p)
    loginToTheWebsite("student", "Password")
    page.wait_for_timeout(4000)
    expect(page).to_have_title("Test Login | Practice Test Automation")


   
 
with sync_playwright() as p:
    run(p)
    validUsernameAndPassword()
    invalidUserName()
    invalidUPassword()
    browser.close()

 