from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.example.com/")
    assert page.title() == "Example Domain"
    page.wait_for_timeout(4000)
    browser.close()
    