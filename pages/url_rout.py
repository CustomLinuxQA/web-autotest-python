class MainPageUrl():
    BASE_URL = "http://selenium1py.pythonanywhere.com/"

    MAIN_PAGE_LINK = BASE_URL

class ProductPageUrl():
    BASE_URL = "http://selenium1py.pythonanywhere.com/"
    PROMO_URL = "?promo=newYear2019"

    THE_SHELLCODERS_HANDBOOK_ENDPOINT = "catalogue/the-shellcoders-handbook_209/"
    THE_SHELLCODERS_HANDBOOK_LINK = BASE_URL + THE_SHELLCODERS_HANDBOOK_ENDPOINT
    THE_SHELLCODERS_HANDBOOK_PROMO_LINK = BASE_URL + THE_SHELLCODERS_HANDBOOK_ENDPOINT + PROMO_URL

    CODERS_AT_WORK_ENDPOINT = "catalogue/coders-at-work_207/"
    CODERS_AT_WORK_LINK = BASE_URL + CODERS_AT_WORK_ENDPOINT
    CODERS_AT_WORK_PROMO_LINK = BASE_URL + CODERS_AT_WORK_ENDPOINT + PROMO_URL

    THE_CITY_AND_THE_STARS_95_ENDPOINT = "catalogue/the-city-and-the-stars_95/"
    THE_CITY_AND_THE_STARS_95_LINK = BASE_URL + THE_CITY_AND_THE_STARS_95_ENDPOINT
    THE_CITY_AND_THE_STARS_95_PROMO_LINK = BASE_URL + THE_CITY_AND_THE_STARS_95_ENDPOINT + PROMO_URL

class ProductBugPageUrl():
    BASE_URL = "http://selenium1py.pythonanywhere.com/"
    PROMO_URL = "?promo=offer"

    # BUG TUSK lesson3_step4.
    CODERS_AT_WORK_BUG_ENDPOINT = "catalogue/coders-at-work_207/"
    CODERS_AT_WORK_BUG_PROMO_LINK = BASE_URL + CODERS_AT_WORK_BUG_ENDPOINT + PROMO_URL
