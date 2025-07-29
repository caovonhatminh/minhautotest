from playwright.sync_api import sync_playwright
import pytest, time# Thêm dòng này nếu bạn muốn sử dụng các tính năng của pytest

def test_example_page_title(): # Đổi tên hàm để pytest nhận diện
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        time.sleep(5)
        assert "Swag Labs" in page.title()
        print(f"Page title: {page.title()}") # Thêm dòng này để in ra tiêu đề trang
        browser.close()

# Ví dụ một test case khác, nếu bạn muốn
# def test_another_example():
#    assert True