def test_open_main_page(page_opener):
        
    page = page_opener

    assert page.title() == "QA Studio — Школа по тестированию", "Заголовок не соответствует заявленному"
    