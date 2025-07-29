import pandas as pd
from enum import Enum
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class LiveloCrawler():
    url = 'https://www.livelo.com.br/juntar-pontos/todos-os-parceiros'

    class Selector(Enum):
        LIST_CARD = 'div[data-testid="div_PartnerList"] div[data-testid="div_PartnerCard"]'
        LIST_CARD_WRAPPER = 'div > div[data-testid="div_Flex"]'
        LIST_CARD_LOGO = 'img[data-testid="img_PartnerCard_partnerImage"]'
        LIST_SEARCH_INPUT = 'input[data-testid="TextInput_SearchPartner_search_input"]'
        PARTNER_DETAIL_PROMO_TEXT = 'div[data-testid="div_ParityBanner_parity_bau"] span'
        PARTNER_DETAIL_PROMO_TEXT_2 = 'div[data-testid="div_ParityBanner_parity_promotion"] div[data-testid="div_Flex"] span'
        LIST_CARD_PROMOTEXT = 'div[data-testid="div_PartnerCard"] > div:nth-child(3) > div:first-child  > div:first-child'
        LIST_CARD_BTN_RULES = 'button[data-testid="button_PartnerCard_goToPartner"]'
        PARTNER_DETAIL_LEGAL_TERMS = 'div[data-testid="div_LegalTerms"]'
        PARTNER_DETAIL_NAME = 'div.parity-banner__partner-name h1[data-testid="Text_Typography"]'

    def get_partners_data(self):
        browser = self._get_browser()
        if (browser.current_url != self.url):
            browser.get(self.url)
        cards = browser.find_elements(By.CSS_SELECTOR, self.Selector.LIST_CARD.value)
        return self._list_to_dataframe(
            list(
                map(lambda card: self._get_card_data(card), cards)
            )
        )
    
    def save_partners_to_json(self, path = '.'):
        data = self.get_partners_data()
        data.to_json(f'{path}/partners.json', indent=4, orient='records', force_ascii=False)

    def save_partners_to_csv(self, path = '.'):
        data = self.get_partners_data()
        data.to_csv(f'{path}/partners.csv', index=False, sep=';')
    
    def _get_card_data(self, card_el: WebElement):
        logo_el = card_el.find_element(By.CSS_SELECTOR, self.Selector.LIST_CARD_LOGO.value)
        logo_alt = logo_el.get_attribute('alt')
        partner_name = logo_alt.replace('Logo ', '')
        card_wrappers = card_el.find_elements(By.CSS_SELECTOR, self.Selector.LIST_CARD_WRAPPER.value)
        promotext_wrapper = card_wrappers[len(card_wrappers) - 2]
        promotext = promotext_wrapper.text.replace('\n', '')
        return (partner_name, promotext)
    
    def _list_to_dataframe(self, data: list):
        return pd.DataFrame(data, columns=['Partner', 'Score'])
    
    def _get_browser(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        return browser