import os
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from livelocrawler.cssselector import CssSelector

class LiveloCrawler():
    partners_url = os.getenv('LIVELO_PARTNERS_URL')
    selenium_address = f'http://{os.getenv('SELENIUM_HOST')}:{os.getenv('SELENIUM_PORT')}'
    
    def get_partners_data(self):
        try:
            browser = self._get_browser()
            if (browser.current_url != self.partners_url):
                browser.get(self.partners_url)
            cards = browser.find_elements(By.CSS_SELECTOR, CssSelector.LIST_CARD.value)
            partners_data = list(map(lambda card: self._get_card_data(card), cards))
            return self._list_to_dataframe(partners_data)
        except:
            raise 'not able to connect and get data from livelo'
        finally:
            browser.quit()
    
    def save_partners_to_json(self, path = '.'):
        data = self.get_partners_data()
        data.to_json(f'{path}/partners.json', indent=4, orient='records', force_ascii=False)

    def save_partners_to_csv(self, path = '.'):
        data = self.get_partners_data()
        data.to_csv(f'{path}/partners.csv', index=False, sep=';')
    
    def _get_card_data(self, card_el: WebElement):
        logo_el = card_el.find_element(By.CSS_SELECTOR, CssSelector.LIST_CARD_LOGO.value)
        logo_alt = logo_el.get_attribute('alt')
        partner_name = logo_alt.replace('Logo ', '')
        card_wrappers = card_el.find_elements(By.CSS_SELECTOR, CssSelector.LIST_CARD_WRAPPER.value)
        promotext_wrapper = card_wrappers[len(card_wrappers) - 2]
        promotext = promotext_wrapper.text.replace('\n', '')
        return (partner_name, promotext)
    
    def _list_to_dataframe(self, data: list):
        return pd.DataFrame(data, columns=['Partner', 'Score'])
    
    def _get_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless=new')
        browser = webdriver.Remote(command_executor=self.selenium_address, options=chrome_options)
        browser.implicitly_wait(3)
        return browser