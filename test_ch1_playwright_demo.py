from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    # for firefox: browser = p.firefox.launch(headless=False)
    # for webkit: browser = p.webkit.launch(headless=False) 
    # for edge: browser = p.chromium.launch(channel="msedge", headless=False)
    # Set headless=True to run in the background without opening a browser window

    # Create a new page (tab)
    page = browser.new_page()

    # Navigate to website
    page.goto("https://github.com")

    # Print page title
    print("Page Title:", page.title())
    
    # Interact with the page (e.g., click on "Sign in" link)
    # Note: The selector may need to be updated if the website's structure changes.
    # getbyrole: it finds elements based on their ARIA role and accessible name, which is more robust than relying on specific CSS selectors or XPath.
    # ARIA means Accessible Rich Internet Applications, which is a set of attributes that can be added to HTML elements to make web content more accessible to people with disabilities.
    page.get_by_role("link", name="Sign in").click()  # Click on "Sign in" link
    
    # get_by_* methods are more robust and maintainable than using CSS selectors or XPath, as they rely on the semantic structure of the page rather than specific element attributes or positions. This makes tests less brittle and more resilient to changes in the page layout or design.
    # We have get by role, get by text, get by label, get by placeholder, get by alt text, get by title, get by test id, get by display value, get by role with name, get by role with name and level, get by role with name and pressed, get by role with name and selected, get by role with name and expanded, get by role with name and checked.
    
    print("Current URL after clicking Sign in:", page.url," with title: ", page.title())

    # Close browser
    browser.close()