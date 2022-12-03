from utilities.config_parser import ReadConfig


def test_log_in_normal_user(open_login_page):
    login_page = open_login_page
    creds_normal = ReadConfig.get_creds()
    login_page.set_email(creds_normal[0]).set_password(creds_normal[1]).log_in_click()
    assert login_page.menu_is_displayed()


def test_try_to_login_locked_user(open_login_page):
    login_page = open_login_page
    creds_locked = ReadConfig.get_creds_locked()
    login_page.set_email(creds_locked[0]).set_password(creds_locked[1]).log_in_click()
    assert login_page.error_message()
