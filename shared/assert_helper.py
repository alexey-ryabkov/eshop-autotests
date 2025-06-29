from playwright.sync_api import Page


def assert_page_title_is(title: str, page: Page):
    page_title = page.title()
    assert (
        title in page.title()
    ), f"Expected page title {title}, got {page_title}"
