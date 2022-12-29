import pytest


@pytest.mark.xfail
def test_check_products_name(logg_in):
    assert logg_in.check_products_titles() == True


@pytest.mark.parametrize('element', ('image', 'title'))
def test_open_pdp_clicking_(element, logg_in):
    assert logg_in.click_on_the_element(element)


def test_add_items_to_cart(logg_in):
    logg_in.add_two_items_to_cart()
    assert logg_in.get_cart_counter_qty() == '2'


def test_low_high_sort(logg_in):
    assert logg_in.check_low_high() is True, f'Prices was not sorted from low to high'
