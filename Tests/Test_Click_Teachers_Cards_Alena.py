def test_click_teachers_cards_alena(page_opener):
    page = page_opener

    @pytest.mark.regression
    frontbutton = page.locator('[class="swiper-button__next"]')
    assert frontbutton.get_attribute('aria-disabled') == 'false', 'Кнопка Вперед неактивна'
    frontbutton.click()
    frontbutton.click()
    frontbutton.click()

    backbutton = page.locator('[class="swiper-button__prev"]')
    assert backbutton.get_attribute('aria-disabled') == 'false', 'Кнопка Назад неактивна'
    backbutton.click()

    alena = page.locator('[src="https://static.tildacdn.com/tild3239-3930-4333-b630-663634316564/48.jpg"]')
    assert alena.is_visible(), 'Изображение ментора Алены не видно'
    alena.click()

    page.wait_for_url('https://mentor.qa.studio/28?returnTo=https%3A%2F%2Fqa.studio%2F%23team')
    current_url = page.url
    expected_url = 'https://mentor.qa.studio/28?returnTo=https%3A%2F%2Fqa.studio%2F%23team'
    assert current_url == expected_url, f"Ожидался URL {expected_url}, но получен {current_url}"

    backbackbutton = page.locator('text="Назад"')
    assert backbackbutton.is_visible(), 'Кнопка Назад не видна'
    backbackbutton.click()

    assert page.title() == "QA Studio — Школа по тестированию", "Мы не вернулись назад"
