from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def page_opener(scope="function"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://qa.studio')
        yield page
        context.close()
        browser.close()