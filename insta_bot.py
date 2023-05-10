from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager
from time import sleep

class Insta:
    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.sign_in()

    def sign_in(self):
        
        '''
        webdriver will wait for a page to load by default.
          It does not wait for loading inside frames or for ajax requests. It means when you use .get('url'),
        your browser will wait until the page is completely loaded and then go to the next command in the code. But when you are posting an ajax request,
          webdriver does not wait and it's your responsibility to wait an appropriate amount of time for the page or a part of page to load; 
          so there is a module named expected_conditions.
        '''


        self.driver.get('https://instagram.com')
        sleep(2)

        # self.browser.implicitly_wait(10) # seconds


        # useranme and password input
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        
        # Log in Button
        self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()
        sleep(5)
        self.driver.get('https://instagram.com/'+self.username+'/')
        sleep(5)
        self.get_followwers()

    def log_out(self):
        
        self.driver.get('https://instagram.com/'+self.username+'/')
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button').click()
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[6]').click()
        sleep(10)

    def get_followwers(self):

        self.driver.get('https://instagram.com/'+self.username+'/followers/')
        sleep(5)
        last_ht,ht =0,1
        try:                                            
          scrollbox= self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        except:
            print('niche wala') 
            scrollbox = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]')
        while last_ht!=ht:
            last_ht=ht
            sleep(1)
            ht= self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,scrollbox)
            links = scrollbox.find_elements_by_tag_name('a')

        names=[]
        names = [name.text for name in links if name.text != '']
        print(names)
        print(len(names))
        #close box
        sleep(2)
        self.get_follwing()                                            
        
    def get_follwing(self):
        self.driver.get('https://instagram.com/'+self.username+'/following/')
        sleep(5)
        last_ht,ht =0,1
        scrollbox = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        while last_ht!=ht:
            last_ht=ht
            sleep(1)
            ht= self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """,scrollbox)
            links = scrollbox.find_elements_by_tag_name('a')

        names=[]
        names = [name.text for name in links if name.text != '']
        print(names)
        print(len(names))
        #close box
        sleep(2)

        self.log_out()



        



Insta(username,password)
