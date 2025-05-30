@when('I visit the "Home Page"')
def step_impl(context):
    context.browser.get(context.get_url("/"))

@when('I press the "{button}" button')
def step_impl(context, button):
    context.browser.find_element(By.ID, button.lower().replace(" ", "_")).click()

@when('I enter "{value}" in the name field')
def step_impl(context, value):
    context.browser.find_element(By.ID, "name").send_keys(value)

@when('I select "{value}" in the category field')
def step_impl(context, value):
    Select(context.browser.find_element(By.ID, "category")).select_by_visible_text(value)

@when('I select "{value}" in the availability filter')
def step_impl(context, value):
    Select(context.browser.find_element(By.ID, "available")).select_by_visible_text(value)

@then('I should see "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source
