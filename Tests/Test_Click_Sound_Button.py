def test_sound_button(page_opener):
    page = page_opener

    sound_button = page.locator('[id="rec803921749"]')
    assert sound_button.is_visible(), "Кнопка звука не найдена на странице"

    initial_state = sound_button.locator('[src="https://static.tildacdn.com/tild6531-3964-4137-b461-363137393735/volume-x.svg"]')

    sound_button.click()

    new_state = sound_button.locator('[src="https://static.tildacdn.com/tild6465-3234-4830-a130-646232616661/volume-2.svg"]')

    assert initial_state != new_state, "Состояние кнопки звука не изменилось после клика"
    