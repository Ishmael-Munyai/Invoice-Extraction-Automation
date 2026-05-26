from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".

    #launch
    browser = chromium.launch()

    #login
    page = browser.new_page()

    #navigate
    page.goto("https://rpachallengeocr.azurewebsites.net/")

    

    # other actions...
    browser.close()