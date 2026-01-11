# outreach/scraper.py
import time
from typing import Dict, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from outreach.linkedin_driver import get_logged_in_driver
from outreach.db import upsert_investor

FINOVIA_QUERIES: List[str] = [
    "bank CTO",
    "bank CIO",
    "digital banking executive",
    "asset management CTO",
    "asset management CIO",
    "private credit CIO",
    "private credit head of technology",
    "custody operations director",
    "custody platform lead",
    "exchange infrastructure lead",
    "market infrastructure CTO",
    "regulated exchange CTO",
]

POSOVIA_QUERIES: List[str] = [
    "retail CEO",
    "retail COO",
    "director of retail operations",
    "vp of retail operations",
    "franchise owner",
    "multi-unit manager",
    "regional manager retail",
    "store operations director",
    "retail CFO",
    "vp of finance retail",
    "controller retail",
    "pos operations manager",
    "head of store operations",
]

INVESTOR_QUERIES = [
    "fintech investor",
    "saas investor",
    "angel tech investor",
    "private equity tech investor",
    "early stage tech investor",
]

INNOVATIVE_TOPICS = [
    "AI in finance",
    "embedded payments",
    "real time settlement",
    "POS innovation",
    "retail automation",
    "banking modernization",
    "fintech infrastructure",
    "cloud core banking",
    "payment orchestration",
    "digital wallet adoption",
]




def build_search_url(query: str) -> str:
    from urllib.parse import quote_plus

    encoded = quote_plus(query)
    return f"https://www.linkedin.com/search/results/people/?keywords={encoded}"


def parse_search_results_page(driver: WebDriver, source_product: str, query: str):
    cards = driver.find_elements(By.CSS_SELECTOR, "div.entity-result__item")
    for card in cards:
        try:
            name_el = card.find_element(
                By.CSS_SELECTOR,
                "span.entity-result__title-text a span[dir='ltr']",
            )
            name = name_el.text.strip()
        except NoSuchElementException:
            name = ""

        try:
            profile_link_el = card.find_element(By.CSS_SELECTOR, "a.app-aware-link")
            profile_url = profile_link_el.get_attribute("href").split("?")[0]
        except NoSuchElementException:
            profile_url = ""

        try:
            headline_el = card.find_element(
                By.CSS_SELECTOR,
                "div.entity-result__primary-subtitle",
            )
            headline = headline_el.text.strip()
        except NoSuchElementException:
            headline = ""

        if profile_url:
            upsert_investor(
                name=name,
                profile_url=profile_url,
                headline=headline,
                source_product=source_product,
                source_query=query,
            )


def scrape_search_results_for_query(
    driver: WebDriver,
    source_product: str,
    query: str,
    max_pages: int = 3,
):
    url = build_search_url(query)
    driver.get(url)
    time.sleep(3)

    current_page = 1
    while current_page <= max_pages:
        time.sleep(3)
        parse_search_results_page(driver, source_product, query)

        # next page button
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Next']")
            if not next_button.is_enabled():
                break
            next_button.click()
            current_page += 1
            time.sleep(3)
        except NoSuchElementException:
            break


def scrape_all_investor_segments(max_pages_per_query: int = 3):
    """
    High-level entrypoint: mines both Finovia & POSOVIA audiences.
    Called from Celery.
    """
    driver = get_logged_in_driver(headless=False)  # adjust arg signature if different
    try:
        for query in FINOVIA_QUERIES:
            scrape_search_results_for_query(
                driver,
                source_product="finovia",
                query=query,
                max_pages=max_pages_per_query,
            )

        for query in POSOVIA_QUERIES:
            scrape_search_results_for_query(
                driver,
                source_product="posovia",
                query=query,
                max_pages=max_pages_per_query,
            )

    finally:
        driver.quit()
