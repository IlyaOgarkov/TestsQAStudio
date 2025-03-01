def test_open_junior_middle(page_opener):

    page = page_opener

    buttonjunior = page.locator('[id="tab1_568115906"]')
    assert buttonjunior.get_attribute('aria-selected') == 'true', 'Кнопка База активна'

    buttonmiddle = page.locator('[id="tab2_568115906"]')
    assert buttonmiddle.inner_text() == "Middle", "Текст Мидл кнопки не соответствует"
    assert buttonmiddle.get_attribute('aria-selected') == 'false', 'Кнопка Мидл неактивна'
    buttonmiddle.click()
    instformiddles = page.locator('text="Инструменты для мидла"')
    assert instformiddles.is_visible(), "Текст Инструменты для мидла невидим"
    assert buttonmiddle.get_attribute('aria-selected') == 'true', 'Кнопка Мидл активна'
    assert buttonjunior.get_attribute('aria-selected') == 'false', 'Кнопка База неактивна'

    buttonauto = page.locator('[id="tab3_568115906"]')
    assert buttonauto.inner_text() == "Автотесты", "Текст Автотесты кнопки не соответствует"
    assert buttonauto.get_attribute('aria-selected') == 'false', 'Кнопка Автотесты неактивна'
    buttonauto.click()
    miniautomat = page.locator('text="Маленький автоматизатор"')
    assert miniautomat.is_visible(), "Текст Маленький Автоматизатор невидим"
    assert buttonauto.get_attribute('aria-selected') == 'true', 'Кнопка Автотесты активна'
    assert buttonmiddle.get_attribute('aria-selected') == 'false', 'Кнопка Мидл неактивна'

    buttonresume = page.locator('[id="tab4_568115906"]')
    assert buttonresume.inner_text() == "Резюме", "Текст Резюме не соответствует"
    assert buttonresume.get_attribute('aria-selected') == 'false', 'Кнопка Резюме неактивна'
    buttonresume.click()
    resume = page.locator('text="Подготовка к собесам"')
    assert resume.is_visible(), "Текст Подготовка к собесам невидим"
    assert buttonresume.get_attribute('aria-selected') == 'true', 'Кнопка Резюме неактивна'
    assert buttonauto.get_attribute('aria-selected') == 'false', 'Кнопка Автотесты активна'

    buttonwork = page.locator('[id="tab5_568115906"]')
    assert buttonwork.inner_text() == "Стажировка", "Текст Стажировка не соответствует"
    assert buttonwork.get_attribute('aria-selected') == 'false', 'Кнопка Стажировка неактивна'
    buttonwork.click()
    work = page.locator('[id="rec568115911"]')
    assert work.is_visible(), "Текст Стажировка невидим"
    assert buttonwork.get_attribute('aria-selected') == 'true', 'Кнопка Стажировка неактивна'
    assert buttonresume.get_attribute('aria-selected') == 'false', 'Кнопка Стажировка активна' 