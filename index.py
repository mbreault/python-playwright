#!/usr/bin/env python

# setup
# pip install playwright pytest-playwright 
# python -m playwright install

from playwright.sync_api import Page 

def test_example_is_working(page: Page): 
    page.goto('https://example.com') 
    assert page.innerText('h1') == 'Example Domain'