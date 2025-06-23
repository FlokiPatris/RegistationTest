import pytest
from playwright.sync_api import sync_playwright

#scope function? rather session why are you testing me? :D
@pytest.fixture(scope="function")
# better naming what page?
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()