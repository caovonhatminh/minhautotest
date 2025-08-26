from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import expect,Page
class FirstPage:
    def __init__(self, page):
        self.page = page
        self.linkEvilTesterpage = page.locator('//a[@href="https://eviltester.com"]')
        
    def gotoEvilTesterpage(self):
        with self.page.context.expect_page() as second_page_info:
            self.linkEvilTesterpage.click()
        new_page = second_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page
    
class FirstPagewithTalotics:
    def __init__(self, page:Page):
        self.page = page
        self.link_Talotics_page = page.locator('(//a[@href="https://talotics.com"])[1]')

    def gotoTaloticsPage(self):
        with self.page.context.expect_page() as third_page_info:
            self.link_Talotics_page.click()
        new_page = third_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page