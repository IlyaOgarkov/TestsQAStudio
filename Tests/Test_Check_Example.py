def test_check_example(page_opener):
    page = page_opener

    checkex = page.locator('text="Cмотреть пример"')
    assert checkex.is_visible(), 'Надписи Смотреть пример не видно'

    with page.expect_popup() as new_page_info:
        checkex.click()
        new_page = new_page_info.value
        new_page.bring_to_front()
        new_page.wait_for_load_state("networkidle")
        expected_url = 'https://t.me/juniors_qa/1507'
        assert new_page.url == expected_url, f"Ожидался URL {expected_url}, но получен {new_page.url}"
        
        assert new_page.title() == "Telegram: Contact @juniors_qa", 'Заявленный заголовок не совпадает'

        new_page.close()