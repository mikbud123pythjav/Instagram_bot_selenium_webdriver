#this program was created to automatize liking and following people on the instagram
#developed by @mikbud123phyjava
#thank you for your attension

#this programm version is based on Chrome version !!! 103.0.5060.114 (official version) (64-bits) !!!
#I have to add that i have fully clear varsion of chrome. (It means for me that I have never used instagram before in this browser)


#initialization libraries and webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from random import randint

class Instabot:
    #constructor
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')  #between quotation marks you have to write your path to webdriver

    def login(self):
        #time for refreshing the browser#
        time.sleep(3)
        self.browser.get('https://www.instagram.com')
        time.sleep(3)

        #code for clicking the cookies accept#
        self.acceptbutton = self.browser.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]")
        time.sleep(3)
        self.acceptbutton.click()
        time.sleep(3)

        #the part of logging#
        self.login = ""    #<------ you have to write there an email to your instagram #
        self.password = ""                     #<------ you have to write there a password to your instagram #

        #email#
        self.emailForm = self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        self.emailForm.click()
        self.emailForm.send_keys(self.login)

        #password#
        self.passwordForm = self.browser.find_element(By.XPATH,'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        self.passwordForm.click()
        self.passwordForm.send_keys(self.password)

        #clicking login button, saving a logging button and notifications#
        self.loginbutton = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
        time.sleep(3)
        self.loginbutton.click()
        time.sleep(3)
        self.savingbutton = self.browser.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/div/button")
        time.sleep(3)
        self.savingbutton.click()
        time.sleep(3)
        self.notyfiactionbutton = self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")
        time.sleep(3)
        self.notyfiactionbutton.click()
        time.sleep(3)

    #object which select random hastags to search. It prepares for automative likes#
    def serching_hastags(self):

        #randomize selecting hastags#
        self.hashtags = ['butik', 'sklep', 'vinted', 'polishgirl', 'fashion']
        self.number = len(self.hashtags) - 1
        self.rand_tags = randint(0, self.number)
        self.browser.get("https://www.instagram.com/explore/tags/" + self.hashtags[self.rand_tags] +"/")
        time.sleep(8)

    #this object gives#
    def opening_photos(self):
        self.left = random.randint(1, 3)
        self.left = str(self.left)
        self.downIndex = random.randint(1, 3)
        self.downIndex = str(self.downIndex)
        time.sleep(3)
        self.photo = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[2]/div/div[" + self.left + "]/div[" + self.downIndex + "]/a/div/div[2]")
        self.photo.click()
        time.sleep(3)

    #object which is created to like and skip the photo
    def liking_photo(self):
        time.sleep(2)
        self.liking = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")
        self.liking.click()



    #this object leads to skip liked photo
    def skip_photo(self):
        time.sleep(2)
        self.skip = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
        self.skip.click()

    #this object leads to opening and watching stories
    def stories(self):
        self.instagram_button = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[1]/div/div/a/div/div/i")
        self.stories = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/section/div[1]/div[2]/div/div/div/div/ul/li[3]/div/button/div[1]/span/img")

        self.instagram_button.click()
        self.stories.click()

    #this object leads to change  hash
    def change_hash(self):
        self.hashtags_rand = random.randint(0, self.liczba - 1)
        time.sleep(2)
        self.browser.get('https://www.instagram.com/explore/tags/' + self.hashtags[self.hashtags_rand] + '/')
        print('# changed to # ' + self.hashtags[self.hashtags_rand])
        time.sleep(5)

    #this object is created to make a realx for 3 hours
    def relax(self):
        self.start_time = time.time()
        self.seconds = 10800

        while True:
            self.current_time = self.time.time()
            self.elapsed_time = self.current_time - self.start_time

            if self.elapsed_time > self.seconds:
                break

    #this object leads to follow accounts to make bigger reach
    def follow(self):
        self.instagram_button = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[1]/div/div/a/div/div/i")
        self.instagram_button.click()
        time.sleep(1)
        self.profil_button = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
        self.profil_button.click()
        time.sleep(1)
        self.followers_button = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[3]/a/div/span")
        self.followers_button.click()
        #profile
        time.sleep(2)
        self.profil =  self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/ul/div/li[166]/div/div[1]/div[2]/div[1]/span/a/span")
        self.profil.click()
        #colocation with profile follow
        time.sleep(2)
        self.add_follow = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[3]/button")
        self.add_follow.click()
        #following
        self.i = 0
        self.div = [3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34]
        while 28 >= self.i:
            self.follwing = self.browser.find_element(By.XPATH,
                                                      "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[2]/div[2]/div/div/div/ul/li[3]/div/div/div/div/div[4]/button")
            self.following.click()
            time.sleep(1.5)
            self.i += 1


    #object which log you out form the instagram
    def logout(self):
        time.sleep(2)
        self.stories = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span/img")
        self.stories.click()
        time.sleep(1)
        self.out = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div")
        self.out.click()

    #obcject which connect object like liking photos and skipping
    def connector(self):
        self.i = 0
        while 30 >= self.i:
            if self.i == 15:
                self.serching_hastags()
                self.opening_photos()
                self.i += 1
            else:
                self.liking_photo()
                time.sleep(2)
                self.skip_photo()
                self.i +=  1



Bot = Instabot()
Bot.login()
Bot.serching_hastags()
Bot.opening_photos()
Bot.connector()
Bot.stories()
