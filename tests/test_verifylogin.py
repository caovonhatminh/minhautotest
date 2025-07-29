from playwright.sync_api import sync_playwright
import pytest, time, sys, os
#from masterPage import MasterPage

def test_login(): # Đổi tên hàm để pytest nhận diện
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        master_page = MasterPage(page)
        master_page.navigate()
        time.sleep(6)
        master_page.login("standard_user","secret_sauce")
        time.sleep(5)