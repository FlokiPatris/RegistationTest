from playwright.sync_api import sync_playwright, ViewportSize
import pytest

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        viewport: ViewportSize = {"width": 1920, "height": 1080}
        context = browser.new_context(viewport=viewport)
        page = context.new_page()
        page.set_default_timeout(60000)

        yield page

        browser.close()