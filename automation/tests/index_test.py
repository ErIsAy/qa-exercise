import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import unittest
import requests
import time
import json
import dateutil.parser
from datetime import datetime
from helpers import format_date
from selenium import webdriver
from pages.index_page import IndexPage
from pages.edit_page import EditPage
from pages.delcat_page import DeleteCategoryPage

class Index(unittest.TestCase): 
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.64.2/qa-exercise/index.php")

    #Adds new given todo
    def test_add_todo(self):
        driver = self.driver
        index = IndexPage(driver)
        index.enter_todo("dotdash")
        index.select_category("Personal")
        index.select_due_date('24','1','2019')
        index.click_add_todo_button()

    #Adds new given category
    def test_add_category(self):
        driver = self.driver
        index = IndexPage(driver)
        index.add_new_category("Pago","Blue")
        index.click_add_category_add_button()

    #Removes given category
    def test_remove_category(self):
        driver = self.driver
        index = IndexPage(driver)
        index.click_category_to_remove("College")
        delcat = DeleteCategoryPage(driver)
        delcat.click_nevermind_button()

    #Edits to given to do 
    def test_edit_todo(self):
        driver = self.driver
        index = IndexPage(driver)
        edit = EditPage(driver)
        index.click_todo_checkbox(2)
        index.click_edit_todo(4)
        edit.edit_todo("ERISAY PEREZ")
        edit.edit_category("Leisure")
        edit.edit_due_date('22','12','2020')
        edit.click_update_button()

    #Tests a given todo
    def test_complete_todo(self):
        driver = self.driver
        index = IndexPage(driver)
        index.click_todo_checkbox(2)
        index.click_complete_button()
        assert '<strike>!@#$!@#$!#@</strike>' in driver.page_source

    #Tests the toggle all feature
    def test_toggle_all(self):
        driver = self.driver
        index = IndexPage(driver)
        index.click_toggle_all_button()
        index.click_remove_button()

    #Tests the "advanced" feature
    def test_advanced_options(self):
        driver = self.driver
        index = IndexPage(driver)
        adv_tag = driver.find_element(*index.advanced_options_tag)
        index.click_advanced_button()
        assert 'visibility: hidden;' in adv_tag.get_attribute('style')

    #Test service status of the API endpoint
    def test_api_call(self):
        r = requests.get('http://192.168.64.2/qa-exercise/fake-api-call.php')
        print r.status_code
        assert r.status_code == 200

    #Find how many tasks do not have "category" assigned
    def test_api_category(self):
        r = requests.get('http://192.168.64.2/qa-exercise/fake-api-call.php')
        tasks = r.json()
        category_count = 0
        for task in tasks:
            if task['category'] == '':
                category_count += 1
        print("Tasks with unasigned category: %s" %(category_count))

    #Aggregate and print only "task names"
    def test_api_task_name(self):
        r = requests.get('http://192.168.64.2/qa-exercise/fake-api-call.php')
        tasks = r.json()
        for task in tasks:
            print(task['task name'])

    #Read API response and print tasks in descending "due date" order
    def test_api_order_by_date(self):
        r = requests.get('http://192.168.64.2/qa-exercise/fake-api-call.php')
        tasks = r.json()
        unsortedArray = []
        sortedArray = []
        invalidArray = []

        for task in tasks:
            if task['due date'] != "\r\n":
                context = {
                    "id": task['id'],
                    "status": task['status'],
                    "task name": task['task name'],
                    "category": task['category'],
                    "due date": datetime.utcfromtimestamp(int(task['due date'])).strftime('%d-%m-%Y'),
                }
                unsortedArray.append(context)
            else:
                context = {
                    "id": task['id'],
                    "status": task['status'],
                    "task name": task['task name'],
                    "category": task['category'],
                    "due date": '',
                }
                invalidArray.append(context)


        sortedArray = sorted(
                unsortedArray,
                key=lambda x: datetime.strptime(x['due date'], '%d-%m-%Y'), reverse=True
                )

        sortedArray.append(invalidArray)
        print "API Response in descending date \r\n %s" %(sortedArray)
         
    #Count and validate the number of tasks
    def test_api_count_tasks(self):
        r = requests.get('http://192.168.64.2/qa-exercise/fake-api-call.php')
        tasks = r.json()
        task_len = len(tasks)
        print(task_len)
        task_counter = 0
        for task in tasks:
            task_counter += 1
        print(task_counter)
        if task_counter == task_len:
            print("Total number of tasks: %s"%(task_counter))

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()





