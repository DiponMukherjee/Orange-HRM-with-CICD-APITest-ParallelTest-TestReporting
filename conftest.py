from playwright.sync_api import sync_playwright
import pytest


#Defining the authenticated page -- as scoped function -- using the storage state
@pytest.fixture(scope="function")
def authenticated_page(browser, page):
    context = browser.new_context(storage_state="auth/state.json")
    page = context.new_page()
    yield page
    context.close()