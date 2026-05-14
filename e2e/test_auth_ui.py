from playwright.sync_api import Page, expect


def test_register_success(page: Page):
    page.goto("http://127.0.0.1:8000/register")

    page.fill("#email", "playwrightuser@example.com")
    page.fill("#username", "playwrightuser")
    page.fill("#password", "password123")
    page.fill("#confirmPassword", "password123")
    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text("Registration successful")


def test_login_success(page: Page):
    page.goto("http://127.0.0.1:8000/login")

    page.fill("#username", "jwtuser1")
    page.fill("#password", "password123")
    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text("Login successful")


def test_register_short_password(page: Page):
    page.goto("http://127.0.0.1:8000/register")

    page.fill("#email", "shortpass@example.com")
    page.fill("#username", "shortpassuser")
    page.fill("#password", "123")
    page.fill("#confirmPassword", "123")
    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text("Password must be at least 6 characters long")


def test_login_wrong_password(page: Page):
    page.goto("http://127.0.0.1:8000/login")

    page.fill("#username", "jwtuser1")
    page.fill("#password", "wrongpassword")
    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text("Invalid username or password")