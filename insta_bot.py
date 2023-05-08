from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager
from time import sleep

class Insta:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.signIn()

    def signIn(self):
        
        '''
        webdriver will wait for a page to load by default.
          It does not wait for loading inside frames or for ajax requests. It means when you use .get('url'),
        your browser will wait until the page is completely loaded and then go to the next command in the code. But when you are posting an ajax request,
          webdriver does not wait and it's your responsibility to wait an appropriate amount of time for the page or a part of page to load; 
          so there is a module named expected_conditions.
        '''


        self.browser.get('https://instagram.com')
        sleep(2)



        # useranme and password input
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        
        # Log in Button
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(200)

Insta(','')
