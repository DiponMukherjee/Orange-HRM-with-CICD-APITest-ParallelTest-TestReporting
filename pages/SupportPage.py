from playwright.sync_api import expect

class SupportPage:
    def __init__(self, page):
        self.page = page
        self.profile_button = page.get_by_role("banner").get_by_role("img", name="profile picture")
        self.support_button = page.get_by_role("menuitem", name="Support")
        self.customer_support_header = page.locator("#app")
        self.support_email = page.locator("#app")


    def navigate_to_support_page(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        self.profile_button.click()
        self.support_button.click()

    def verify_customer_support_header(self):
        expect(self.customer_support_header).to_contain_text("Customer Support")

    def verify_support_email(self):
        expect(self.support_email).to_contain_text("ossupport@orangehrm.com")

