@pytest.mark.regression
def test_conditions_link(page_opener):
    page = page_opener

    conlink = page.locator('text="Подробные условия"')
    assert conlink.is_visible(), 'Текста Подробные условия не видно'
    conlink.click()

    diploma = page.locator('text="Условия получения диплома"')
    assert diploma.is_visible(), 'Текст не открылся'
