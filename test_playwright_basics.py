from playwright.sync_api import Page, expect

def test_saucedemo_login(page: Page):
    # 1. Navigate to the website
    page.goto("https://www.saucedemo.com/")
    
    # 2. Fill in the username and password (Playwright auto-waits for these to appear!)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    
    # 3. Click the login button
    page.click("#login-button")
    
    # 4. Verify we successfully logged in by checking the new URL
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    print("\nSuccessfully logged into Swag Labs using Playwright!")




def test_add_item_to_cart(page: Page):
    # 1. Login to the store
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # 2. Click the specific "Add to cart" button for the Sauce Labs Backpack
    page.click("#add-to-cart-sauce-labs-backpack")
    
    # 3. VERIFY: Target the little red circle on the shopping cart and assert it says "1"
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")
    
    print("\nSuccessfully verified the shopping cart updated to 1 item!")