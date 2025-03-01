@pytest.mark.regression
def test_project_site_link(page_opener):
    page = page_opener

    prosite = page.locator('text="Сайт проекта"')
    assert prosite.is_visible(), 'Надписи Сайт проекта не видно'

    with page.expect_popup() as new_page_info:
        prosite.click()
        new_page = new_page_info.value
        new_page.bring_to_front()
        new_page.wait_for_load_state("networkidle")
        expected_url = 'https://juniors.qa/'
        assert new_page.url == expected_url, f"Ожидался URL {expected_url}, но получен {new_page.url}"
        
        assert new_page.title() == "Джуны | Бесплатное тестирование", "Заявленной надписи не видно"

        new_page.close()
