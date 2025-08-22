from enum import Enum

class CssSelector(Enum):
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