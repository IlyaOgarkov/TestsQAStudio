def test_click_teachers_cards_katya(page_opener):
    page = page_opener

    frontbutton = page.locator('[class="swiper-button__next"]')
    assert frontbutton.get_attribute('aria-disabled') == 'false', 'Кнопка Вперед неактивна'
    frontbutton.click()

    katya = page.locator('[src="https://static.tildacdn.com/tild3532-3634-4630-b930-313431386261/5016.jpg"]')
    assert katya.is_visible(), 'Изображение ментора Кати не видно'
    katya.click()

    page.wait_for_url('https://mentor.qa.studio/24?returnTo=https%3A%2F%2Fqa.studio%2F%23team')
    current_url = page.url
    expected_url = 'https://mentor.qa.studio/24?returnTo=https%3A%2F%2Fqa.studio%2F%23team'
    assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    backbackbutton = page.locator('text="Назад"')
    assert backbackbutton.is_visible(), 'Кнопка Назад не видна'
    backbackbutton.click()

    assert page.title() == "QA Studio — Школа по тестированию", "Мы не вернулись назад"