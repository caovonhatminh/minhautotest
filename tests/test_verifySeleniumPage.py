from playwright.sync_api import sync_playwright
import pytest, time, sys, os
from models.FirstPage import FirstPage
from models.SecondPage import SecondPage
URL_web = "https://compendiumdev.co.uk/"
def test_login(): # Đổi tên hàm để pytest nhận diện
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL_web)
        first_page = FirstPage(page)
        connect_page= first_page.gotoEvilTesterpage()
        
        second_page = SecondPage(connect_page)
        
        second_page.verify_SecondPage_display()
        # second_page.screenshot(path="data/eviltester2.png", full_page=False)

        second_page.click_Contact_on_Menubar()
        
       
        
        
        