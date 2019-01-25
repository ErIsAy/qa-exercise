from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class EditPage():

    def __init__(self, driver):
        self.driver = driver
        self.todo_textbox = (By.NAME, "data")
        self.update_button = (By.NAME, "submit")
        self.category_select = (By.NAME, "category")
        self.due_day_select = (By.NAME,"due_day")
        self.due_month_select = (By.NAME,"due_month")
        self.due_year_select = (By.NAME,"due_year")

#update
    def edit_todo(self, todo):
        self.driver.find_element(*self.todo_textbox).clear()
        self.driver.find_element(*self.todo_textbox).send_keys(todo)
        
#Edit category
    def edit_category(self, category):
        select = Select(self.driver.find_element(*self.category_select))
        select.select_by_visible_text(category)

#update due date
    def edit_due_date(self, day, month,year):
        d = Select(self.driver.find_element(*self.due_day_select))
        m = Select(self.driver.find_element(*self.due_month_select))
        y = Select(self.driver.find_element(*self.due_year_select))
        d.select_by_value(day)
        m.select_by_value(month)
        y.select_by_value(year)

#click Update Button
    def click_update_button(self):
        self.driver.find_element(*self.update_button)