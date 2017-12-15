import unittest
import time
from selenium import webdriver

class TestOne(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.driver.set_window_size(1120, 550)

	def test_url(self):
		count = 0
		self.driver.get("http://jobs.kent.edu/cw/en-us/listing/")
		self.driver.find_element_by_id(
			'search-keyword').send_keys("Chemistry")
		#self.driver.find_element_by_id("search_button_homepage").click()
		time.sleep(5)
		self.assertIn(
			"http://jobs.kent.edu/cw/en-us/search/?search-keyword=Chemistry", self.driver.current_url
		)
		name = self.driver.find_element_by_id('search-results-content').find_elements_by_tag_name('tr')
		for i in name:
			row = i.find_elements_by_tag_name('td')
			for s in row[0:5]:
				if(count != 0):
					print(s.text)
				count = count+1
			count = 0
			


	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()