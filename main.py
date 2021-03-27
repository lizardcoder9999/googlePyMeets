# Module imports

from selenium import webdriver
from scedule import Schedule
from googleAuth import GoogleAuth
from util import BrowserUtil
import time

# The Options object
options = webdriver.ChromeOptions()

# Browser options
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")

# Disable selenium chrome outputs
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument("--log-level=3")

# More options to keep mic and camera muted  1 = allow, 2 = block
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1
})

# Browser object with the options passed in as a parameter to the constructor
browser = webdriver.Chrome(options=options)

# Instantiates the Schedule class
classes = Schedule()

# Number of people for when to leave the meeting
numPeopleAllowed = input("How many people should there be for when you want to leave the meet")

# Gets the amount of classes that the student is in
amountOfClasses = input("How many classes would you like to add: ")

i = 0

# For each class the user entered it will get info for it such as the time and link
while i < int(amountOfClasses):
    i += 1
    classes.AddClass()

# This will instantiate the GoogleAuth class I created in googleAuth.py which takes in the current instance of the
# webdriver which in this case is browser

auth = GoogleAuth(browser)

# Will Trigger the login to google method which will get login info and log the user into google.
auth.loginToGoogle()

# Instantiates the BrowserUtil class created in util.py which takes in the current instance of the webdriver in the
# constructor Which in this case is browser
util = BrowserUtil(browser)

# Declaring the current variable
current = None

# While the program is running it will change the current time to the current time in the 24 hour clock.
# If this matches any classes in the schedule array then it will join that class.
# I added a series of time.sleep to prevent google meets from realizing its a bot.
# Then with the util object it will disable the camera and microphone for the user.
# It will then join the meet and constantly check the number of people in the call.
# If the number of people in the call is less than or equal to the amount of people allowed the user specified earlier
# Then it will leave the meet by clicking the hang up button and the process repeats until it joins another meeting
# and so on ...
while True:
    current = time.strftime('%H:%M')
    for classroom in classes.schedule:
        classTime = classroom.time
        if str(current) == str(classTime):
            browser.get(classroom.link)
            time.sleep(4)
            util.disableMic()
            util.disableCamera()
            time.sleep(3)
            joinButton = browser.find_element_by_class_name("NPEfkd")
            joinButton.click();
            time.sleep(2)
            numPeopleInCall = browser.find_element_by_class_name("wnPUne")
            innerSpanNum = numPeopleInCall.get_attribute("innerHTML")
            leaveButton = browser.find_element_by_class_name("I5fjHe")
            if int(innerSpanNum) <= int(numPeopleAllowed):
                time.sleep(1)
                leaveButton.click()










