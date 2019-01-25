from selenium.webdriver.common.by import By

class DeleteCategoryPage():

    def __init__(self, driver):
        self.driver = driver
        self.yes_button = (By.LINK_TEXT,"Yes")
        self.nevermind_button = (By.LINK_TEXT,"Nevermind")

    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    def click_nevermind_button(self):
        self.driver.find_element(*self.nevermind_button).click()
