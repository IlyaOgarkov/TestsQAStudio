def test_click_teachers_cards_nastya(page_opener):
    page = page_opener

    @pytest.marker.regression
    nastya = page.locator('[src="https://static.tildacdn.com/tild6635-3630-4237-b339-313035623266/5026.jpg"]')
    assert nastya.is_visible(), "Изображение Анастасии Чичериной не видно"
    nastya.click()

    page.wait_for_url('https://mentor.qa.studio/36?returnTo=https%3A%2F%2Fqa.studio%2F%23team')
    current_url = page.url
    expected_url = 'https://mentor.qa.studio/36?returnTo=https%3A%2F%2Fqa.studio%2F%23team'
    assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    backbackbutton = page.locator('text="Назад"')
    assert backbackbutton.is_visible(), 'Кнопка Назад не видна'
    backbackbutton.click()

    assert page.title() == "QA Studio — Школа по тестированию", "Мы не вернулись назад"
