from selenium.webdriver.common.keys import Keys
import time

class GoogleAuth:
    def __init__(self,browser):
        self.auto = browser
        self.email = ""
        self.password = ""

    # Gets users gmail login and will login to there school account
    def loginToGoogle(self):
        print("---please enter your school login for your gmail account---")
        self.email = input("Please enter your email: ")
        self.password = input("Please enter your password: ")
        self.auto.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        emailBox = self.auto.find_element_by_class_name("whsOnd")
        emailBox.send_keys(self.email);
        emailBox.send_keys(Keys.ENTER)
        time.sleep(3)
        passwordBox = self.auto.find_element_by_class_name("whsOnd")
        passwordBox.send_keys(self.password)
        passwordBox.send_keys(Keys.ENTER)



