from pages.url_rout import ProductPageUrl
from pages.url_rout import ProductBugPageUrl    # BUG TUSK lesson3_step4.
from pages.url_rout import MainPageUrl


class MainTestLink():
    TEST_LINK = [
        (MainPageUrl.MAIN_PAGE_LINK)
    ]


class ProductTestLink():
    TEST_LINK = [
        (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_LINK),
        (ProductPageUrl.THE_SHELLCODERS_HANDBOOK_PROMO_LINK),
        (ProductPageUrl.CODERS_AT_WORK_LINK),
        (ProductPageUrl.CODERS_AT_WORK_PROMO_LINK)
    ]


class ProductBugTestLink():    # BUG TUSK lesson3_step4.
    TEST_LINK = [
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "0",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "1",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "2",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "3",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "4",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "5",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "6",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "7",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "8",
        (ProductBugPageUrl.CODERS_AT_WORK_BUG_PROMO_LINK) + "9"
    ]
