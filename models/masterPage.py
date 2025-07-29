from playwright.sync_api import sync_playwright

class MasterPage:
    def __init__(self, page):
        self.page = page
        self.txtUsername= page.locator('//input[@id="user-name"]')
        self.txtPassword = page.locator('//input[@id="password"]')
        self.btnLogin = page.locator('//input[@id="login-button"]')
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.txtUsername.fill(username)
        self.txtPassword.fill(password)
        self.btnLogin.click()