# This snippets demonstrates handling alerts, frames, and windows using Playwright in Python.

from playwright.sync_api import expect, sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com")
    
    # Opening 'Alert, Frame and Windows' option on menus
    page.get_by_text("Alerts, Frame & Windows").click()
    
    # Wait for menu items to load
    page.wait_for_timeout(1000)
    
    # Get all element-groups
    all_element_groups = page.locator('xpath=//div[@class="element-group"]')
    
    # Find the Alerts, Frame & Windows group
    target_group_index = -1
    for i in range(all_element_groups.count()):
        group_text = all_element_groups.nth(i).inner_text()
        if "Alerts, Frame & Windows" in group_text:
            target_group_index = i
            break
    
    if target_group_index >= 0:
        # Get the menu items from this group
        group = all_element_groups.nth(target_group_index)
        menu_items = group.locator('li.btn.btn-light span.text')
        option_count = menu_items.count()
        
        print(f"\n=== Options under 'Alerts, Frame & Windows' ===")
        for i in range(option_count):
            option_text = menu_items.nth(i).inner_text()
            print(f"{i+1}. {option_text}")
    
    # Click on 'Alerts' option
    print("\nClicking on 'Alerts' option...")
    page.click('a[href="/alerts"]')
    
    # Wait for navigation
    page.wait_for_timeout(1000)
    
    # Assert URL ends with alerts
    expect(page).to_have_url(re.compile(r'alerts$'))
    print("✓ Successfully navigated to Alerts page")
    print(f"Current URL: {page.url}")
    
    # Hitting different buttons to trigger different alerts now
    print("\nTriggering different alerts...")
    
    