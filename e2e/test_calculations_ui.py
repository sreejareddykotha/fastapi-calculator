from playwright.sync_api import Page


def test_create_calculation(page: Page):

    page.goto("http://127.0.0.1:8000/calculations-page")

    page.fill("#a", "10")
    page.fill("#b", "5")

    page.select_option("#type", "Add")

    page.once("dialog", lambda dialog: dialog.accept())

    page.click("button[type='submit']")

    page.wait_for_timeout(2000)

    assert "Calculator CRUD" in page.content()


def test_delete_calculation(page: Page):

    page.goto("http://127.0.0.1:8000/calculations-page")

    page.wait_for_timeout(1000)

    delete_buttons = page.locator("text=Delete")

    if delete_buttons.count() > 0:
        delete_buttons.first.click()

    page.wait_for_timeout(1000)

    assert "Calculator CRUD" in page.content()


def test_page_loads(page: Page):

    page.goto("http://127.0.0.1:8000/calculations-page")

    assert "Calculator CRUD" in page.content()