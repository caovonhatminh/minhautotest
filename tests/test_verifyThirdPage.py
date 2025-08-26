from playwright.sync_api import sync_playwright
import pytest, time, sys, os
from models.FirstPage import FirstPagewithTalotics
from models.ThirdPage import ThirdPage

URL_web = "https://compendiumdev.co.uk/"
def test_gotowebsite():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL_web)
        first_page = FirstPagewithTalotics(page)
        connect_page= first_page.gotoTaloticsPage()
        time.sleep(5)
        third_page = ThirdPage(connect_page)
        third_page.verify_ThirdPage_display()
        time.sleep(5)
        third_page.click_Tools_for_Testing_UTM_Links()
        time.sleep(5)
        third_page.verify_Tools_for_Testing_UTM_Links_page()
        time.sleep(10)