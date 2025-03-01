from playwright.sync_api import expect

def test_podcast_button(page_opener):
    page = page_opener

    podcast = page.locator('text="Подкаст"')
    podcast.wait_for(state='visible')
    assert podcast.is_visible(), 'Кнопки Подкаст не видно'
    podcast.click()

    page.wait_for_url("https://redbarn.ru/audio/testirovshhik/")
    expect(page).to_have_url("https://redbarn.ru/audio/testirovshhik/")
    expect(page.locator('title')).to_be_visible()
    assert page.title() == "Работник месяца - Тестировщик | Подкаст-студия RED BARN", 'Страница не открылась'