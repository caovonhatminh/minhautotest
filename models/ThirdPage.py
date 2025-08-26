from playwright.sync_api import expect, Page
from playwright.sync_api import sync_playwright
import time
class ThirdPage:
    def __init__(self, page:Page):
        self.page = page
        self.verify_Talotics_page = page.locator('//img[@src="/images/greenGreyWords.png"]')
        self.text_Tools_for_Testing_UTM_Links = page.locator('//h1[contains(text(),"Tools for Testing UTM Links")]')
        self.text_Tools_for_Testing_UTM_Links_in_page = page.locator('(//h1[contains(text(),"Tools for Testing UTM Links")])[1]')
    def verify_ThirdPage_display(self):
        expect(self.verify_Talotics_page).to_be_visible()
        time.sleep(5)
    def click_Tools_for_Testing_UTM_Links(self):
        self.text_Tools_for_Testing_UTM_Links.click()
        time.sleep(5)
    def verify_Tools_for_Testing_UTM_Links_page(self):
        expect(self.text_Tools_for_Testing_UTM_Links_in_page).to_be_visible()
        time.sleep(5)
    