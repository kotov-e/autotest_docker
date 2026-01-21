
import pytest
import json
import allure
import os
from logging import getLogger, basicConfig, DEBUG, ERROR, CRITICAL, INFO, FileHandler, StreamHandler, Formatter


from playwright.sync_api import Page, expect, sync_playwright



log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'data.log')

logger = getLogger(__name__)
logger.setLevel(DEBUG)
FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
file_handler = FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(DEBUG)
file_handler.setFormatter(Formatter(FORMAT))

console = StreamHandler()
console.setLevel(CRITICAL)
console.setFormatter(Formatter(FORMAT))

if logger.handlers:
    logger.handlers.clear()

logger.addHandler(file_handler)
logger.addHandler(console)


@allure.title("Test 1")
def test_wiki1(page):
    logger.debug("Rut Test 1")
    with allure.step("Goto https://www.wikipedia.org/"):
        logger.info("Goto https://www.wikipedia.org/")
        page.goto('https://www.wikipedia.org/')
    logger.info("Click on link")
    page.get_by_role('link', name='Русский').click()
    logger.info("Check that text is visible")
    expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()
    logger.debug("Test 1 is done")
    logger.critical("INFO CRITICAL MESSAGE")

@allure.title("Test 2")
def test_wiki2(page: Page):
    logger.debug("Rut Test 2")
    with allure.step("Goto https://www.wikipedia.org/"):
        logger.info("Goto https://www.wikipedia.org/")
        page.goto('https://www.wikipedia.org/')
    logger.info("Click on link")
    page.locator("#js-link-box-ru").click()
    logger.info("Contain text")
    expect(page.locator(".main-top-header.mw-html-heading")).to_contain_text("Добро пожаловать в")
    logger.debug("Test 2 is done")
    logger.critical("INFO CRITICAL MESSAGE")

@allure.title("Test 3")
def test_wiki3(page: Page):
    logger.debug("Rut Test 3")
    with allure.step("Goto https://www.wikipedia.org/"):
        logger.info("Goto https://www.wikipedia.org/")
        page.goto('https://www.wikipedia.org/')
    logger.info("Click on link")
    page.locator("#js-link-box-ru").click()
    logger.info("Click on link")
    page.get_by_role('link', name='Википедию').click()
    logger.info("Contain text")
    expect(page.locator(".firstHeading.mw-first-heading")).to_contain_text("Википедия")
    logger.debug("Test 3 is done")
    logger.critical("INFO CRITICAL MESSAGE")

