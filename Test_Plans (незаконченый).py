def test_plans(page_opener):
    page = page_opener

    changedatebutton = page.locator('#rec750932476')
    assert changedatebutton.is_visible(), 'Кнопки изменения даты не видно'
    changedatebutton.click()

    changedatebutton.select_option(value="https://checkout.qa.studio/p/c/kYNtrXryoy?returnTo=https%3A%2F%2Fqa.studio%2F%23payment")

    selected_option = changedatebutton.evaluate("updateButton(this, '.button1')")
    assert selected_option == "29 апреля", f"Выбранная опция должна быть '29 апреля', но получено '{selected_option}'"


