"""
site_data.py are UI-Map definition of the application under test.
This makes editing of target elements easy - if the UI (and not the workflow) changes.
If workflow changes, you may want to change the associated steps (steps.robot) and
keyword (helper.robot) file
"""

# =============================================================================
# YELLOW ONLINE PAGE ELEMENTS
# =============================================================================
# Common Page Elements
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Home Page
# -----------------------------------------------------------------------------
home_consumer_tab_find_a_business_section      = "css=section.find-a-business"

# -----------------------------------------------------------------------------
# My Yellow
# -----------------------------------------------------------------------------
my_navlogin_loggedinusername                   = "css=.loggedin-user-email"

# -----------------------------------------------------------------------------
# Navigation login elements
# -----------------------------------------------------------------------------
navloginpanel_navlogin                         = "css=div.yellow-nav-tools nav.nav-login a[data-action='show-login']"
navloginpanel_email                            = "css=input[name='email']"
navloginpanel_password                         = "css=input[name='password']"
navloginpanel_signup                           = "css=.login-panel-footer p a"
navloginpanel_login                            = "css=.login-panel-form-controls button"
url_consumer_main_page                         = "/find-a-business/"
home_consumer_tab_find_a_business_section      = "css=section.find-a-business"
login_modal_backdrop                           = "css=.modal-backdrop"
my_navlogin_dropdown_arrow                  = "css=section.header-business a.nav-logged-in span.loggedin-user-email"
my_navloginpanel_signout                    = "css=section.header-business .logged-in-panel li.log-out"