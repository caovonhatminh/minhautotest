from playwright.sync_api import expect, Page
from playwright.sync_api import sync_playwright
import time 
class SecondPage:
    def __init__(self, page:Page):
        self.page = page
        self.verify_EvilTester_page = page.locator('//h2[contains(text(),"Recent Blog Posts")]')
        self.btnContact = page.locator('(//a[text()="Contact"])[1]')
        self.verify_contact_page = page.locator('//h1[text()="Contact Alan Richardson @ EvilTester.com"]')
        self.screenshot = page.screenshot
    def verify_SecondPage_display(self):
        expect(self.verify_EvilTester_page).to_be_visible()
        time.sleep(2)
        self.screenshot(path="/data/eviltester.png", full_page=False)
        




        
    def click_Contact_on_Menubar(self):
        self.btnContact.click()
        time.sleep(2)
        expect(self.verify_contact_page).to_be_visible()
        time.sleep(2)