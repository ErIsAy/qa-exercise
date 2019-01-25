from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class IndexPage():

    def __init__(self, driver):
        self.driver = driver
        self.todo_textbox = (By.NAME, "data")
        self.todo_number_edit = (By.XPATH, r"//*[@id='todos-content']/form/ul/li[1]/a")
        self.todo_checkbox = (By.XPATH, r"//[@id='todos-content']/form/ul/li[1]/input")
        self.todo_remove_button = (By.XPATH, "//body/div[3]/input[1]")
        self.todo_complete_button = (By.XPATH, "//body/div[3]/input[2]")
        self.toggle_all_button = (By.NAME, "allbox")
        self.advanced_button = (By.XPATH, "//body/div[3]/a[1]")
        self.todo_add_button = (By.XPATH, "//./div[4]/input[2]")
        self.category_select = (By.NAME, "category")
        self.due_day_select = (By.NAME,"due_day")
        self.due_month_select = (By.NAME,"due_month")
        self.due_year_select = (By.NAME,"due_year")
        self.categories_element = (By.CSS_SELECTOR, "body > div.controls > a > span")
        self.category_textbox = (By.NAME, "categorydata")
        self.category_add_button = (By.XPATH, r"//*[@id='extra']/input[2]")
        self.category_color_select = (By.NAME, "colour")
        self.advanced_options_tag = (By.XPATH, '//*[@id="extra"]')
        
#enters todo in todo input fiels
    def enter_todo(self, todo):
        self.driver.find_element(*self.todo_textbox).clear()
        self.driver.find_element(*self.todo_textbox).send_keys(todo)

#selects category from present categories
    def select_category(self, category):
        select = Select(self.driver.find_element(*self.category_select))
        select.select_by_visible_text(category)

#selects due date
    def select_due_date(self, day, month,year):
        d = Select(self.driver.find_element(*self.due_day_select))
        m = Select(self.driver.find_element(*self.due_month_select))
        y = Select(self.driver.find_element(*self.due_year_select))
        d.select_by_value(day)
        m.select_by_value(month)
        y.select_by_value(year)

#clicks edit todo
    def click_edit_todo(self, todo_id):
        todo = self.driver.find_elements(By.XPATH, "//*[@id='todos-content']/form/ul/li/a[1]")
        todo[todo_id].click()

#clicks wanted checkbox 
    def click_todo_checkbox(self, todo_id):
        checkbox = self.driver.find_elements(By.XPATH, ".//*[@id='todos-content']/form/ul/li/input")
        checkbox[todo_id].click()

#clicks the add button
    def click_add_todo_button(self):
        self.driver.find_element(*self.todo_add_button).click()

#Adds new category
    def add_new_category(self, category, colour):
        self.driver.find_element(*self.category_textbox).clear()
        self.driver.find_element(*self.category_textbox).send_keys(category)
        c = Select(self.driver.find_element(*self.category_color_select))
        c.select_by_visible_text(colour)
        self.driver.find_element(*self.category_add_button).click()

#clicks "Add category" button
    def click_add_category_add_button(self):
        self.driver.find_element(*self.category_add_button).click()

#clicks Remove button
    def click_remove_button(self):
        self.driver.find_element(*self.todo_remove_button).click()

#clicks complete buttton
    def click_complete_button(self):
        self.driver.find_element(*self.todo_complete_button).click()

#click advanced button
    def click_advanced_button(self):
        self.driver.find_element(*self.advanced_button).click()

#click category to delete
    def click_category_to_remove(self, name):
        self.driver.find_element_by_xpath('//div/a/span[contains(text(), {})]'.format(name)).click()


#click toggle all checkbox
    def click_toggle_all_button(self):
        self.driver.find_element(*self.toggle_all_button).get_attribute('checked')
        self.driver.find_element(*self.toggle_all_button).click()

