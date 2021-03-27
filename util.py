from selenium.webdriver.common.keys import Keys

# BrowserUtil class, Takes in the current instance of the browser object which is the webdriver we instantiated in
# main.py

class BrowserUtil:
    def __init__(self,browser):
        self.util = browser

    # Disables Microphone upon joining a meet
    def disableMic(self):
        mic = self.util.find_element_by_class_name("oTVIqe")
        mic.send_keys(Keys.CONTROL + 'd')

    # Disables Camera when joining a meet
    def disableCamera(self):
        camera = self.util.find_element_by_class_name("oTVIqe")
        camera.send_keys(Keys.CONTROL + 'e')
