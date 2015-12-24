from locust import HttpLocust, TaskSet, task
import string 
import random
import time

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        #self.comment()

    @task(1)
    def comment(self):
        from splinter import Browser

        with Browser('phantomjs') as browser:
   	  
	# Visit URL
            url = "http://wootest.rtcamp.net/shop/?add-to-cart=70"
            browser.visit(url)
	    url = "http://wootest.rtcamp.net/checkout/"
            browser.visit(url)
            browser.fill('billing_email', 'hello@dfdf.dfdfdfdf')
    # Find and click the 'search' button
            button = browser.find_by_name('woocommerce_checkout_place_order')
    # Interact with elements
            button.click()

class WebsiteUser(HttpLocust):
    weight = 1
    task_set = UserBehavior
#    min_wait=5000
#    max_wait=9000
