from playwright.sync_api import expect


def test_add_operation(page):
    page.goto("http://127.0.0.1:8000")
    page.fill("#num1", "2")
    page.fill("#num2", "3")
    page.click("text=Add")
    expect(page.locator("#result")).to_have_text("5")


def test_subtract_operation(page):
    page.goto("http://127.0.0.1:8000")
    page.fill("#num1", "10")
    page.fill("#num2", "4")
    page.click("text=Subtract")
    expect(page.locator("#result")).to_have_text("6")


def test_multiply_operation(page):
    page.goto("http://127.0.0.1:8000")
    page.fill("#num1", "6")
    page.fill("#num2", "7")
    page.click("text=Multiply")
    expect(page.locator("#result")).to_have_text("42")


def test_divide_operation(page):
    page.goto("http://127.0.0.1:8000")
    page.fill("#num1", "8")
    page.fill("#num2", "2")
    page.click("text=Divide")
    expect(page.locator("#result")).to_have_text("4")


def test_divide_by_zero(page):
    page.goto("http://127.0.0.1:8000")
    page.fill("#num1", "8")
    page.fill("#num2", "0")
    page.click("text=Divide")
    expect(page.locator("#result")).to_have_text("Cannot divide by zero")