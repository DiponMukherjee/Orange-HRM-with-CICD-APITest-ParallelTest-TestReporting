from pages.DashboardPage import DashboardPage
from pages.AdminPage import AdminPage
from pages.Admin_AddUser_Page import Admin_AddUser_Page


def test_add_admin_user(authenticated_page):

#Defining the page objects
    dashboard_page = DashboardPage(authenticated_page)
    admin_page = AdminPage(authenticated_page)
    add_user_page = Admin_AddUser_Page(authenticated_page)

#Navigate to the Dashboard Page
    dashboard_page.navigate_to_dashboard_page()

#Go to the Admin Page - Verifying Clicking on the Admin button also
    dashboard_page.click_admin_link()

#Go to the Add User Page
    admin_page.click_add_user_button()

#Fill Up the Form
    add_user_page.select_user_role_admin() # User Role is Admin
    add_user_page.select_status_disabled() #Status is Disabled

