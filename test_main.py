
import pytest
from playwright.sync_api import Page, expect, sync_playwright
import allure

@allure.title("Test 1")
def test_wiki1(page):
    with allure.step("Goto https://www.wikipedia.org/"):
        page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='Русский').click()
    expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()

@allure.title("Test 2")
def test_wiki2(page: Page):
    with allure.step("Goto https://www.wikipedia.org/"):
        page.goto('https://www.wikipedia.org/')
    page.locator("#js-link-box-ru").click()
    expect(page.locator(".main-top-header.mw-html-heading")).to_contain_text("Добро пожаловать в")

@allure.title("Test 3")
def test_wiki3(page: Page):
    with allure.step("Goto https://www.wikipedia.org/"):
        page.goto('https://www.wikipedia.org/')
    page.locator("#js-link-box-ru").click()
    page.get_by_role('link', name='Википедию').click()
    expect(page.locator(".firstHeading.mw-first-heading")).to_contain_text("Википедия")
