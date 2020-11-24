"""
===========================================

            CHROMEDRIVER MODULE
    
      'import cm' to use thie module

===========================================
"""

import os
import time
import base64
import requests

from tqdm import trange
from selenium import webdriver


# 1. open chromedriver & setting
def chromedriver_settings(header, gpu, log, driver_root):
    options = webdriver.ChromeOptions()
    if not header: options.add_argument('--headless')
    if not gpu: options.add_argument('--disable-gpu')
    if not log: options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(driver_root, options=options)

    return driver


# 2. Scroll
# 2.1. scroll page smoothly
def scroll_smooth(driver, range_n, sleep_t):
    for i in range(range_n):
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        time.sleep(sleep_t)

# 2.2. scroll page smoothly using tqdm
def scroll_smooth_tqdm(driver, range_n, sleep_t):
    for i in trange(range_n):
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
        time.sleep(sleep_t)

# 2.3. scroll part of page smoothly
def scroll_smooth_divided(driver, range_n, sleep_t, divide_cnt):
    for i in range(range_n):
        driver.execute_script("window.scrollTo({top: document.body.scrollHeight / " + str(divide_cnt) + " * " + str(i) + ", behavior: 'smooth'});")
        time.sleep(sleep_t)

# 3. Tab
# 3.1. open new tab & switch current tab
def new_tab_open(driver, href, sleep_t):
    driver.execute_script("window.open('" + href + "', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(sleep_t)

# 3.2. close current tab & switch previous tab
def new_tab_close(driver, sleep_t):
    time.sleep(sleep_t)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# 4. Download
# 4.1. download images
def download(src, save_root, idx, ext='.jpg'):
    img_data = requests.get(src).content
    inner_download(save_root, img_data, idx, ext)

# 4.2. download base64 images
def download_base64(src, save_root, idx, ext='.jpg'):
    base64_image_data = src.split(',')[1]
    base64_image_data = base64_image_data + '=' * (4 - len(base64_image_data) % 4)
    inner_download(save_root, base64.b64decode(base64_image_data), idx, ext)

def inner_download(save_root, img_data, idx, ext):
    img_save_path = os.path.join(save_root, str(idx + 1) + ext)
    with open(img_save_path, 'wb') as handler:
        handler.write(img_data)

# 5. Btn Click
# 5.1. btn click
def click(driver, selector):
    btn = driver.find_element_by_css_selector(selector)
    btn.click()

# 5.2. btn argument click
def click_arg(driver, selector):
    btn = driver.find_element_by_css_selector(selector)
    driver.execute_script("arguments[0].click();", btn)