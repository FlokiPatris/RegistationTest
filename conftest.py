from playwright.sync_api import sync_playwright, ViewportSize
import pytest

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()