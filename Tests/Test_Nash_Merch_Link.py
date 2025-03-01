def test_nash_merch_link(page_opener):
    page = page_opener

    @pytest.mark.regression
    merch = page.locator("#sbs-803921749-1716199614614").get_by_role("link", name="Наш мерч")
    assert merch.is_visible(), "Ссылки на Наш мерч не видно"
    merch.click()

    nashmerch = page.locator('[id="rec747735895"]')
    nashmerch.wait_for(state='visible')
    assert nashmerch.is_visible(), 'Страница не открылась'
