from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create a new page (tab)
    page = browser.new_page()

    # Navigate to website
    page.goto("https://demoqa.com/text-box")

    # Fill in the text boxes
    page.get_by_placeholder("Full Name").fill("John Doe")
    page.locator("#userEmail").fill("Haryish@email.com")
    page.fill("#currentAddress", "123 Main St,\nAnytown,\nUSA")
    page.fill("#permanentAddress", "456 Elm St, Othertown, USA")
    page.get_by_role("button", name="Submit").click()  # Click on "Submit" button
    
    # Print the output after submission
    print("Current URL after clicking Submit:", page.url," with title: ", page.title())
    
    # Printing details after submission for validation
    # Naive approach
    output_section = page.locator("#output")
    rows = output_section.locator("p")
    count = rows.count()
    
    for i in range(count):
        print(rows.nth(i).text_content()) 
        #nth() : It is a method used to select a specific element from a collection of elements based on its index. The index is zero-based, meaning that the first element has an index of 0, the second element has an index of 1, and so on. For example, if you have a collection of elements and you want to select the third element, you would use nth(2) since the index starts at 0.
        # text_content() : It is a method used to retrieve the text content of an element. It returns the text content as a string, including any whitespace and line breaks. This method is often used to extract the visible text from an element on a web page. For example, if you have an element that contains the text "Hello, World!", calling text_content() on that element would return the string "Hello, World!".
        
    # Better approach using get by text
    texts = page.locator("#output p").all_inner_texts()
    
    for text in texts:
        print(text)
        
    # Interveiew ready model
    output_texts = page.locator("#output p").all_text_contents()
    
    data = {}
    
    for text in output_texts:
        form_field, form_value = text.split(":", 1)  # Split only on the first colon
        data[form_field.strip()] = form_value.strip()  # Remove any leading/trailing whitespace
    
    print(data)
    
    # Close browser
    browser.close()
    