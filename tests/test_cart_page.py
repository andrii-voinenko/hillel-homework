import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_remove_item_from_cart(open_cart_with_items):
    assert open_cart_with_items.click_cart().click_remove_backpack().backpack_deleted()


@pytest.mark.regression
def test_click_continue_shopping_from_cart(open_cart_with_items):
    assert open_cart_with_items.click_cart().click_continue_shopping()


@pytest.mark.smoke
@pytest.mark.regression
def test_do_checkout(open_cart_with_items):
    open_cart_with_items.click_cart().click_checkout()
    assert open_cart_with_items.check_title_info()
    open_cart_with_items.fill_information().click_continue().click_finish_checkout()
    assert open_cart_with_items.check_order_finished()
