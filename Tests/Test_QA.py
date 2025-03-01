@pytest.mark.regression
def test_qa(page_opener):
    
    page = page_opener

    firstq = page.locator('text="А что если тестирование окажется не для меня?"')
    assert firstq.is_visible(), 'Первого вопроса не видно'
    firstq.click()
    firsta = page.locator('[id="accordion1_568115970"]')
    firsta.wait_for(state='visible')
    assert firsta.is_visible(), 'Первого ответа не видно'
    firstq.click()
    firsta.wait_for(state='hidden')
    assert firsta.is_hidden(), 'Первый ответ видно'

    secondq = page.locator('text="Много ли вакансий на позицию тестировщика?"')
    assert secondq.is_visible(), 'Второго вопроса не видно'
    secondq.click()
    seconda = page.locator('[id="accordion2_568115970"]')
    seconda.wait_for(state='visible')
    assert seconda.is_visible(), 'Второго ответа не видно'
    secondq.click()
    seconda.wait_for(state='hidden')
    assert seconda.is_hidden(), 'Второй ответ видно'

    thirdq = page.locator('text="Можно ли найти работу на удалёнке?"')
    assert thirdq.is_visible(), 'Третьего вопроса не видно'
    thirdq.click()
    thirda = page.locator('[id="accordion3_568115970"]')
    thirda.wait_for(state='visible')
    assert thirda.is_visible(), 'Третьего ответа не видно'
    thirdq.click()
    thirda.wait_for(state='hidden')
    assert thirda.is_hidden(), 'Третий ответ видно'
