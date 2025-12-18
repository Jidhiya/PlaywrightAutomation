def test_Open_Gooogle(page):
    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle", timeout=15000 )
    print("Page Title is:", page.title())
