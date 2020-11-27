Crawling Module
==================

## ⚡ Simple Crawling Module using Python Selenium

✔ CDN URL: http://duuboo.net/cdn/cm.py<br/>
✔ Copy this code to use my cdn

``` python
import urllib.request

with urllib.request.urlopen('http://duuboo.net/cdn/cm.py') as response:
    code = response.read()
    exec(code)

# do something
```

## 1. Open Chromedriver & Chromedriver Settings
``` python
driver = chromedriver_settings(header=True, gpu=False, log=False, driver_root='chromedriver.exe')
```
> - header: show chrome window
> - gpu: gpu settings
> - log: show DevTools message
> - driver_root: chromedriver path

## 2. Scroll
### 2.1. Scroll Page Smoothly
``` python
scroll_smooth(driver, range_n, sleep_t)
```
> - driver: chromedriver object
> - range_n: scroll repeat number
> - sleep_t: sleep time

### 2.2. Scroll Page Smoothly Using tqdm (Progress Bar)
``` python
scroll_smooth_tqdm(driver, range_n, sleep_t)
```
> - driver: chromedriver object
> - range_n: scroll repeat number
> - sleep_t: sleep time

### 2.3. Scroll Part of Page Smoothly
``` python
scroll_smooth_divided(driver, range_n, sleep_t, divide_cnt)
```
> - driver: chromedriver object
> - range_n: scroll repeat number
> - sleep_t: sleep time
> - divide_cnt: number of divide current page

## 3. Tab
### 3.1. Open New Tab & Switch New Tab
``` python
new_tab_open(driver, href, sleep_t)
```
> - driver: chromedriver object
> - href: open url
> - sleep_t: sleep time

### 3.2. Close Current Tab & Switch Prev Tab
``` python
new_tab_close(driver, sleep_t):
```
> - driver: chromedriver object
> - sleep_t: sleep time

## 4. Download
### 4.1. Download Images
``` python
download(src, save_root, idx)
```
> - src: image resource
> - save_root: save path
> - idx: image idx

### 4.2. Download BASE64 Images
``` python
download_base64(src, save_root, idx)
```
> - src: image resource
> - save_root: save path
> - idx: image idx

## 5. Button Click
### 5.1. Button click
``` python
click(driver, selector)
```
> - driver: chromedriver object
> - selector: page element selector

### 5.2. Button argument click
``` python
click_arg(driver, selector)
```
> - driver: chromedriver object
> - selector: page element selector
