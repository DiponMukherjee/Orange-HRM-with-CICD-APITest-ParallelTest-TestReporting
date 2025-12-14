from pages.SupportPage import SupportPage

def test_support_page(authenticated_page):

#Defining page object
    support_page = SupportPage(authenticated_page)

#Navigate to support page
    support_page.navigate_to_support_page()


#Verify customer support text and email exist or not

    support_page.verify_customer_support_header()
    support_page.verify_support_email()