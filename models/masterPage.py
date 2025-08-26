from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import expect
class PracticePage:
    def __init__(self, page):
        self.page = page
        self.txtUsername= page.locator('//input[@id="user-name"]')
        self.txtPassword = page.locator('//input[@id="password"]')
        self.btnLogin = page.locator('//input[@id="login-button"]')
        self.btnAddToCartBackpack = page.locator('//div//button[@id="add-to-cart-sauce-labs-backpack" and text()="Add to cart"]')
        self.btnAddToCartBikeLight = page.locator('//div//button[@id="add-to-cart-sauce-labs-bike-light" and text()="Add to cart"]')
        self.btnShoppingCart = page.locator('//a[@class="shopping_cart_link"]')
        self.BackpackAvailable = page.locator('//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
        self.BikeLightAvailable = page.locator('//div[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]')
        self.btnCheckout = page.locator('//button[@id="checkout"]')
        self.check_out_is_available = page.locator('//span[@class="title" and text()="Checkout: Your Information"]')
        self.first_name = page.locator('//input[@id="first-name"]')
        self.last_name = page.locator('//input[@id="last-name"]')
        self.postal_code = page.locator('//input[@id="postal-code"]')
        self.btnContinue = page.locator('//input[@id="continue"]')
        self.check_out_overview = page.locator('//span[@class="title" and text()="Checkout: Overview"]')
        self.verify_Backpack = page.locator('//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
        self.verify_BikeLight = page.locator('//div[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]')
        self.btnFinish = page.locator('//button[@id="finish"]')
        self.check_out_complete = page.locator('//span[@class="title" and text()="Checkout: Complete!"]')
        self.btnBackHome = page.locator('//button[@id="back-to-products"]')
        
    def navigate_to_login_page(self):
        self.page.goto("https://www.saucedemo.com/")
    def login(self, username, password):
        self.txtUsername.fill(username)
        time.sleep(1)
        self.txtPassword.fill(password)
        time.sleep(1)
        self.btnLogin.click()
    def sort(self):
        self.page.select_option("select.product_sort_container", value="lohi")
    def add_to_cart(self):
        self.btnAddToCartBackpack.wait_for(state="visible")
        self.btnAddToCartBackpack.click()
        time.sleep(5)
        self.btnAddToCartBikeLight.click()
        time.sleep(5)
    def check_item_is_added(self):
        self.btnShoppingCart.click()
        time.sleep(5)
        expect(self.BackpackAvailable).to_be_visible()
        time.sleep(2)
        expect(self.BikeLightAvailable).to_be_visible()
        time.sleep(2)
    def go_to_checkout(self):
        self.btnCheckout.click()
        time.sleep(2)
        expect(self.check_out_is_available).to_be_visible()
        time.sleep(2)
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        time.sleep(1)
        self.last_name.fill(last_name)
        time.sleep(1)
        self.postal_code.fill(postal_code)
        time.sleep(1)
        self.btnContinue.click()
    def finish_checkout(self):
        expect(self.check_out_overview).to_be_visible()
        time.sleep(2)
        expect(self.verify_Backpack).to_be_visible()
        time.sleep(2)
        expect(self.verify_BikeLight).to_be_visible()
        time.sleep(2)
        self.btnFinish.click()
        time.sleep(5)
    def checkout_complete(self):
        expect(self.check_out_complete).to_be_visible()
        time.sleep(2)
        self.btnBackHome.click()
        time.sleep(2)





    
        

        




        