from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class TypeRacerBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="F:\\Documents\\Coding\\geckodriver.exe")
        self.driver.get("https://www.typeracer.com")
        sleep(2)
        self.actions = ActionChains(self.driver)

    def login(self):
        sign_in = self.driver.find_element_by_xpath("//a[@class=\"promptBtn signIn\"]")
        sign_in.click()
        username = "etaylor234"
        password = "etaylor234"
        username_box = self.driver.find_element_by_xpath("//input[@name=\"username\"]")
        password_box = self.driver.find_element_by_xpath("//input[@name=\"password\"]")
        sleep(2)
        username_box.send_keys(username)
        password_box.send_keys(password)
        sign_in_button = self.driver.find_element_by_xpath("//button[@type=\"button\"]")
        sign_in_button.click()
        sleep(2)
        # close_out_premium_ad = self.driver.find_element_by_xpath("//*[local-name()='svg']/*[local-name()='g']")
        close_out_premium_ad = self.driver.find_element_by_xpath("//div[@class='xButton']")
        close_out_premium_ad.click()
        sleep(1)

    def enter_racetrack_from_lobby(self):
        self.actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('i').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        sleep(1)

    def new_racetrack(self):
        self.actions.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('k').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        sleep(1)

    def wait_for_timer(self):
        time = None
        detected = False
        while True:
            print(detected)
            if (time is None or time.find(":00") != -1) and detected:
                break
            try:
                sleep(0.5)
                # time = self.driver.find_element_by_xpath("//span[@class='time' and not(@title)]//parent::div[@class='timeDisplay']").text
                time = self.driver.find_element_by_xpath("//span[@class='time' and not(@title)]//ancestor::div[@class='popupContent']").text
                if (time is not None):
                    detected = True
                print(time)
                print(type(time))
            except:
                print(time)
                continue
        sleep(1)

    def race(self):
        self.wait_for_timer()
        first = self.driver.find_element_by_xpath("//span[@unselectable=\"on\"]//parent::div[1]").text
        print (first)   #just cause it's cool
        word_list = first.split()
        for word in word_list:
            print(word)
            sleep(0.45)
            temp_chain = ActionChains(self.driver)
            temp_chain.send_keys(word + " ").perform()
        sleep(1)
            

bot = TypeRacerBot()
bot.login()
bot.enter_racetrack_from_lobby()
while(True):
    bot.race()
    bot.new_racetrack()

# bot.race()

