import re                                                   # Regex: Regular Expressions
from playwright.sync_api import expect, sync_playwright     # Playwright Expectation and Sync API

def test_demoqa_open(page):
    page.goto("https://demoqa.com/")
    with page.context.expect_page() as new_page_info:
        page.get_by_alt_text("Selenium Online Training", exact=True).click()
    toolsqa_page = new_page_info.value
    toolsqa_page.wait_for_load_state("domcontentloaded")
    expect(toolsqa_page).to_have_title("Tools QA - Selenium Training")
    
    
