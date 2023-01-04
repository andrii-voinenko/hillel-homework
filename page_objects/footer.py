from selenium.webdriver.common.by import By

from utilities.web_ui.base_page import BasePage


class Footer(BasePage):
    _linkedin = (By.CSS_SELECTOR, '.social_linkedin')
    _facebook = (By.CSS_SELECTOR, '.social_facebook')
    _twitter = (By.CSS_SELECTOR, '.social_twitter')

    def click_social_icon(self, social_media: str):
        if social_media.lower() == 'facebook':
            self.click(self._facebook)
            assert self.url_changed('https://www.facebook.com/saucelabs')
        elif social_media.lower() == 'linkedin':
            self.click(self._linkedin)
            assert self.url_changed('https://www.linkedin.com/company/sauce-labs/')
        elif social_media.lower() == 'twitter':
            self.click(self._twitter)
            assert self.url_changed('https://twitter.com/saucelabs')


