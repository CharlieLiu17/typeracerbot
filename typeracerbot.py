from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class TypeRacerBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\Charlie\\Documents\\Coding\\Python Code\\geckodriver.exe")
        self.driver.get("https://www.typeracer.com")
        sleep(2)
        self.actions = ActionChains(self.driver)
        sleep(3)
        self.actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('o').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()

    def Race(self):
        sleep(2)
        first = self.driver.find_element_by_xpath("//span[@unselectable=\"on\"]//parent::div[1]").text
        print (first)   #just cause it's cool
        sleep(4)
        self.actions.send_keys(first).perform()

bot = TypeRacerBot()
bot.Race()

