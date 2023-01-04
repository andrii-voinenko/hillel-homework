import pytest


@pytest.mark.parametrize('social', ('Twitter', 'Linkedin', 'Facebook'))
def test_click_all_social_media(social, open_footer):
    open_footer.click_social_icon(social)
