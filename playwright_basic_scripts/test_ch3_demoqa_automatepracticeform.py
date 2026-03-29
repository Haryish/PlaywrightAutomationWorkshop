from playwright.sync_api import sync_playwright,expect
import os

#helper functions
def get_file_path(file_name):
    return os.path.join(os.getcwd(), "test_data", file_name)

def validate_result(page, label, expected_value):
    actual_value = page.locator(f"//td[text()='{label}']/following-sibling::td").inner_text()
    assert expected_value == actual_value, f"{label} mismatch: expected {expected_value}, got {actual_value}"
    

with sync_playwright() as p:
    
# Setup and Initiation
    browser = p.chromium.launch(headless=False)                 # Launching browser
    context = browser.new_context()                             # setting context
    page = context.new_page()                               # creating new page (page instance)    
    page.goto("https://demoqa.com/automation-practice-form")    # Opening automate practice form page
    page.wait_for_load_state('networkidle')                     # waiting for the page to load completely
    
# PRACTICE FORM
    
    #Input Values
    name = "Haryish Elangumaran"
    dob = "09/10/1999"
    email = "haryish@sample.com"
    gender = "Male"
    mobile_number = "1234567890"
    subject_value = "Hindi, English, Maths, Chemistry, Physics, Computer Science"
    hobbies = "Sports, Reading"
    current_address = "123, Sample Street, Sample City, Sample State, 123456"
    state = "NCR"
    city = "Delhi"
    
    
#Filling the first name and last name fields using locator
    name_inputs = page.locator("//label[text()='Name']/parent::div/following-sibling::div//input")
    name_segment = name.split(" ")

    for i in range(name_inputs.count()):
        name_inputs.nth(i).fill(name_segment[i])
        
    # Alternately, you can also use the following code to fill the first name and last name fields:
    # wait = page.wait_for_selector("#firstName")
    # wait.fill("John")
    # page.fill("#lastName", "Doe")
    
# Filling the email field using label locator and relative xpath
    email_label = page.get_by_text("Email")
    input_field = email_label.locator("xpath=../following::input[1]")
    input_field.fill(email)
    
    # Alternately, you can also use the following code to fill the email field:
    # page.fill("#userEmail", "email@email.com")
    
# Radio button on genders (radio button locator using label)
    page.get_by_label(gender, exact=True).click()
    
    # Alternately, you can also use the following code to click on the radio button:
    page.click("input[name='gender'][value='Female']")
    
    # Keeping scope of label 'Gender' and clicking on the radio button using relative xpath
    gender_label = page.get_by_text("Gender")
    radio_button = gender_label.locator("xpath=following-sibling::div//input[@value='Other']")
    radio_button.click()
    
# Filling the mobile number field using label locator and relative xpath
    page.get_by_placeholder("Mobile Number").fill(mobile_number)
    
# Filling the date of birth field using label locator and relative xpath

    day,month,year = dob.split("/")
    day = str(int(day))
    month = str(int(month)-1)
    
    datepicker = page.locator("#dateOfBirthInput")
    datepicker.click()
    page.locator(".react-datepicker__year-select").select_option(year)
    page.locator(".react-datepicker__month-select").select_option(month)
    page.locator(f".react-datepicker__day--{int(day):03d}:not(.react-datepicker__day--outside-month)").click()    
    
    # asserting input date with date on ui
    print(dob)
    print(datepicker.input_value())
    
# Filling subject text box
    # By substrings search
    subject_text = page.locator("#subjectsInput")
    subject_text.fill("hi")
    page.get_by_text("Hindi", exact=True).click()
    
    # clear the subject text box
    page.locator(".subjects-auto-complete__multi-value__remove").click()   
    subject_text.fill("")
    
    # From the List
    subject_list = subject_value.split(", ")
    for subject in subject_list:
        subject_text.fill(subject[:3])
        page.get_by_text(subject, exact=True).click()
                
    print("Subjects Input is: ",subject_value)    
    print("Subjects entered successfully as: ", page.locator(".subjects-auto-complete__multi-value__label").all_inner_texts())
    
# Filling the hobbies checkbox using label locator and relative xpath
    hobbies_label = page.get_by_text("Hobbies")
    hobbies_options = page.locator("xpath=//label[text()='Hobbies']/parent::div/following-sibling::div//label")
    print("Total hobbies options: ", hobbies_options.count())
    print("Hobbies options are: ", hobbies_options.all_inner_texts())
    
    # Clicking on the first checkbox using relative xpath
    first_checkbox = hobbies_label.locator("xpath=/parent::div/following-sibling::div//input[@value='1']")
    first_checkbox.click()
    first_checkbox.click()
    
    
    # Clicking the checkbox from list of hobbies options
    hobbies_list = hobbies.split(",")
    for hobby in hobbies_list:
        hobby_checkbox = page.get_by_label(hobby).click()
    
    print("Hobbies Input as: ", hobbies_list)
    
# File Upload web element
    page.set_input_files("#uploadPicture", get_file_path("sample.pdf"))
    
# Filling the current address field using label locator and relative xpath
    address_label = page.get_by_text("Current Address")
    address_input = address_label.locator("xpath=../following-sibling::div/textarea")
    address_input.fill(current_address)
    
# Filling the state and city dropdown using label locator and relative xpath
    state_city_label = page.get_by_text("State and City")
    state_input = state_city_label.locator("xpath=../following-sibling::div/div[@id='state']//input")
    state_input.fill("N") 
    page.get_by_text(state, exact=True).click()
    state_city_label.click()
    city_input = state_city_label.locator("xpath=../following-sibling::div/div[@id='city']//input")
    city_input.fill("Del")
    page.get_by_text(city, exact=True).click()

# Submitting the form
    page.click("#submit")
    
# waiting for the email field to be visible and filling it
    page.wait_for_timeout(5000)
    
# Assertions can be added to verify the form submission and the data entered in the form.
    result_scope = page.locator(".modal-content")
    expect(result_scope.get_by_text("Thanks for submitting the form")).to_be_visible()
    
    validate_result(page, "Student Name", name)
    validate_result(page, "Student Email", email)
    validate_result(page, "Gender", "Other")
    validate_result(page, "Mobile", mobile_number)
    # validate_result(page, "Date of Birth", dob)
    validate_result(page, "Subjects", subject_value)
    validate_result(page, "Hobbies", hobbies)
    # validate_result(page, "Picture", "sample.pdf")
    validate_result(page, "Address", current_address)
    validate_result(page, "State and City", f"{state} {city}")

#close
    browser.close()
    
    
    