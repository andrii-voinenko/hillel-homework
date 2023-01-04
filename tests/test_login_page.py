from time import sleep


def test_log_in_normal_user(open_login_page):
    login_page = open_login_page
    # TODO: get email pass from config
    login_page.set_email('standard_user').set_password('secret_sauce').click_log_in()
    assert login_page.menu_is_displayed()


def test_try_to_login_locked_user(open_login_page):
    login_page = open_login_page
    login_page.set_email('locked_out_user').set_password('secret_sauce').click_log_in()
    assert login_page.error_text()


def test_click_on_x_for_error_message(open_login_page):
    login_page = open_login_page
    login_page.set_email('locked_out_user').set_password('secret_sauce').click_log_in()
    login_page.click_error_button()
    assert login_page.no_error_notification()
