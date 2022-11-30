def test_log_in_normal_user(open_login_page):
    login_page = open_login_page
    login_page.set_email('standard_user').set_password('secret_sauce').log_in_click()
    assert login_page.menu_is_displayed()


def test_try_to_login_locked_user(open_login_page):
    login_page = open_login_page
    login_page.set_email('locked_out_user').set_password('secret_sauce').log_in_click()
    assert login_page.error_message()

