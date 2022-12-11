from selenium import webdriver

# Creates Chrome object since the webdriver will use chrome
driver = webdriver.Chrome()

# Makes a get request to youtube site
driver.get('https://youtube.com')

# Finds xpath of search bar to search something
searchbar = driver.find_element_by_xpath(
    '//*[@id="search"]')

# Allows you to type a phrase in the search box
searchbar.send_keys('Saturday Night Live')

# Finds the xpath of the search button
searchButton = driver.find_element_by_xpath(
    '//*[@id="search-icon-legacy"]')

# Sends a 'click' automation when the search button is clicked
searchButton.click()
