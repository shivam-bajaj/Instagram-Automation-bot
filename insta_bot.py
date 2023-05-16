from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

'''

4. Explicit Wait
5. multi-user
6. Excpetion Handling

'''

'''
Can also scrap data from public or following accounts by adding parameter
'''


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.sign_in()

    def sign_in(self):

        self.driver.get('https://instagram.com')
        sleep(2)

        # self.browser.implicitly_wait(10) # seconds

        # useranme and password input
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
            self.driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        except:
            print("Error finding login Form")
        # Log in Button
        try:
            self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
            sleep(5)
            self.driver.get('https://instagram.com/'+self.username+'/')
            sleep(5)
        except:
            print('Problem with sign in...')

    def log_out(self):

        self.driver.get('https://instagram.com/'+self.username+'/')
        sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/button').click()
        sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/button[6]').click()
        sleep(10)

    def get_followers(self):

        self.driver.get('https://instagram.com/'+self.username+'/followers/')
        sleep(5)
        last_ht, ht = 0, 1
        try:
            scrollbox = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        except:
            print('cant find scroll box')
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scrollbox)
            links = scrollbox.find_elements_by_tag_name('a')

        names = []
        names = [name.text for name in links if name.text != '']
        print(names)
        print(len(names))
        sleep(2)
        return names

    def get_following(self):
        self.driver.get('https://instagram.com/'+self.username+'/following/')
        sleep(5)
        last_ht, ht = 0, 1
        scrollbox = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scrollbox)
            links = scrollbox.find_elements_by_tag_name('a')

        names = []
        names = [name.text for name in links if name.text != '']
        print(names)
        print(len(names))
        sleep(2)
        return names

    def get_followers_info(self):

        followers = self.get_followers()
        sleep(2)
        following = self.get_following()
        not_following_back = [
            user for user in following if user not in followers]
        fans = [user for user in followers if user not in following]

        print(not_following_back)
        print(fans)

        # remove verified signs
        b = '\nVerified'
        for i in range(0, len(not_following_back)):
            if b in not_following_back[i]:
                not_following_back[i] = not_following_back[i].replace(b, '')

        return not_following_back, fans

    def unfollow_user(self, user):

        sleep(2)
        self.driver.get('https://instagram.com/'+user+'/')
        sleep(2)
        try:
            check_following = self.driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div/div[1]')
            if check_following.text == 'Following':
                check_following.click()
                sleep(2)
                self.driver.find_element(
                    By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]').click()
                sleep(2)
            else:
                print('Unable to unfollow')
        except Exception as e:
            print(e)


# username and password
a = InstaBot('', '')
not_following_back, fans = a.get_followers_info()
print(not_following_back)
for user in not_following_back:
    a.unfollow_user(user)
a.log_out()
