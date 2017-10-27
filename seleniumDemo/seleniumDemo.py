from selenium import webdriver
driver = webdriver.PhantomJS("D:/phantomjs/bin/phantomjs");
driver.set_page_load_timeout(10)
driver.get("http:www.baidu.com")
#获取网页元素的方式
# driver.find_element_by_id('...')
# driver.find_element_by_csss_selector('...')
# driver.find_element_by_tag_name('...')
# driver.find_elements_by_xpath('...')
print(driver.title)

driver.quit()