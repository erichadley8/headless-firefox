import os
import datetime
from colorama import Fore, Back
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

while True:
	try:
		### Firefox Parameters
		executable_path = os.getcwd() + "/geckodriver"

		### Firefox Options
		options = Options()
		options.headless = True
		
		### Proxy Configuration
		'''
		proxy = "34.203.142.175:80"
		webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
			"httpProxy": proxy,
			"ftpProxy":proxy,
			"sslProxy":proxy,
			"proxyType":"MANUAL",
		}
		'''
		### Firefox Webdriver
		browser = webdriver.Firefox(options=options, executable_path=executable_path)
		
		### Webdriver Logic
		browser.get('http://www.porngifs.xyz/')
		print(Fore.GREEN + browser.page_source)

		### Popunder 
		body = browser.find_element_by_tag_name("body")
		body.click()
		browser.save_screenshot("popunder.png")
		print(Fore.CYAN + "Clicked for popunder")
		ct = datetime.datetime.now() 
		print("current time:-", ct) 
		browser.switch_to.window(browser.window_handles[1])
		print("Switched back from popunder")
		ct = datetime.datetime.now() 
		print("current time:-", ct) 


		### Ads
		print(Fore.YELLOW + "Getting ads and clicking ads")
		ct = datetime.datetime.now() 
		print("current time:-", ct) 
		elements = browser.find_elements_by_tag_name('iframe')
		for element in elements:
			try:
				if "jads" in element.get_attribute("src"):
					try:
						element.click()
						print("Clicked " + str(element))
						ct = datetime.datetime.now() 
						print("current time:-", ct) 
					except:
						print("Failed to click " +str(element))
						ct = datetime.datetime.now() 
						print("current time:-", ct) 
			except:
				print("Element detached from dom")
		page = 1
		print(Fore.RED + "Closing ads and tabs")
		ct = datetime.datetime.now() 
		print("current time:-", ct) 
		try:
			for tab in browser.window_handles:
				try:
					browser.switch_to.window(tab)
					browser.save_screenshot(str(page) + "_page.png")
					browser.close()
					print("Closed " + str(tab))
					ct = datetime.datetime.now() 
					print("current time:-", ct) 
					page = page + 1
				except:
					print("Failed to close")
					ct = datetime.datetime.now() 
					print("current time:-", ct)
		except:
			print("Failed to close all tabs") 
	finally:
		try:
			browser.quit()
		except:
			pass
