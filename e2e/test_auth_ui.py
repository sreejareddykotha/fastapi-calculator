from playwright.sync_api import Page


def test_register_page_loads(page: Page):

    page.goto("http://127.0.0.1:8000/register")

    assert "Register" in page.content()


def test_login_page_loads(page: Page):

    page.goto("http://127.0.0.1:8000/login")

    assert "Login" in page.content()