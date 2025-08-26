from playwright.sync_api import sync_playwright
import pytest, time, sys, os
from models.masterPage import PracticePage

def test_login(): # Đổi tên hàm để pytest nhận diện
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        master_page = PracticePage(page)
        master_page.navigate_to_login_page()
        time.sleep(6)
        master_page.login("standard_user","secret_sauce")
        time.sleep(5)
        master_page.sort()
        time.sleep(10)
        master_page.add_to_cart()
        time.sleep(5)
        master_page.check_item_is_added()
        time.sleep(5)
        master_page.go_to_checkout()
        time.sleep(5)
        master_page.fill_checkout_information("Cao", "Minh", "12345")
        time.sleep(5)
        master_page.finish_checkout()
        time.sleep(5)
        master_page.checkout_complete()
        time.sleep(5)

        



        
        
