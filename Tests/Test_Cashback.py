def test_cashback(page_opener):
    page = page_opener

    moreinfo = page.locator('[id="rec750932517"]')
    assert moreinfo.is_visible(), 'Кнопки Подробнее в Вернем деньги в любой момент нет'
    moreinfo.click()

    cashback = page.locator('[id="rec750932517"]')
    cashback.wait_for(state='visible')
    assert cashback.is_visible(), 'Сообщение не появилось'