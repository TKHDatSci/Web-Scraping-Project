get_attribute from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\where\you\download\the\chromedriver.exe')
driver = webdriver.Chrome()

driver.get("https://www.glassdoor.com")

# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
csv_file = open('glassdoor.csv', 'w')
writer = csv.writer(csv_file)
# Page index used to keep track of where we are.
index = 1
# Initialize two variables refer to the next button on the current page and previous page.
prev_button = None
current_button = None


#search keyword "data" in searchbox              
elemKey =browser.find_element_by_css_selector('#KeywordSearch')
elemKey.send_keys('data')
              
 #key the location             
loc = browser.find_element_by_css_selector('#LocationSearch')
browser.find_element_by_id('LocationSearch').clear()
loc.send_keys('New York')
#click to go to result page
but = browser.find_element_by_css_selector('#HeroSearchButton').click()
              
              
while True:
	try:
		# We first need to make sure the button on the previous page is not available anymore.
		if prev_button is not None:
			WebDriverWait(driver, 10).until(EC.staleness_of(prev_button))

		print("Scraping Page number " + str(index))
		index = index + 1
		# Find all the reviews on the page
		#wait_review = WebDriverWait(driver, 10)
		wait_page = WebDriverWait(driver, 10)
		rows = wait_page.until(EC.presence_of_all_elements_located((By.XPATH,
									'.//ul[@class="jlGrid hover"]')))


#>>> contlist = brow.find_elements_by_xpath('.//li')
#30
#>>> contlist = ''.join(map(lambda x : x.text,contlist))
#>>> contlist


		for row in rows:
			# Initialize an empty dictionary for each review
			rows_dict = {}
			# Use relative xpath to locate the title, content, username, date.
			# Once you locate the element, you can use 'element.text' to return its string.
			# To get the attribute instead of the text of each element, use 'element.get_attribute()'
			title = row.find_element_by_xpath('.//div[@class="flexbox"]').text
			company = row.find_element_by_xpath('//div[@class="flexbox empLoc"]/div').text
			location = row.find_element_by_xpath('//div[@class="flexbox empLoc"]/div/span').text
			salary = row.find_element_by_xpath('//span[@class="green small"]').text
			rating = row.find_element_by_xpath('.//span[@class="compactStars "]').text




			# There might be multiple paragraphs, so you use find elements instead of find element.
			#content = review.find_elements_by_xpath('.//div[@class="bv-content-summary-body-text"]/p')
			#content = ''.join(map(lambda x: x.text, content))
			#username = review.find_element_by_xpath('.//h3[@class="bv-author"]').text
			#date = review.find_element_by_xpath('.//meta[@itemprop="datePublished"]').get_attribute('content')
			#rating = review.find_element_by_xpath('.//span[@class="bv-rating-stars-container"]/span').text
			#rating = re.search('\d+', rating).group()

			rows_dict['title'] = title
			rows_dict['company'] = company
			rows_dict['location'] = location
			rows_dict['salary'] = salary
			rows_dict['rating'] = rating

			writer.writerow(review_dict.values())

		# Locate the next button on the page.
		wait_button = WebDriverWait(driver, 10)
		current_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'//li[@class="page "]/a').get_attribute('href')))
		prev_button = current_button
		current_button.click()
	except Exception as e:
		print(e)
		csv_file.close()
		driver.close()
		break
