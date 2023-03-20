from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import json
import re
import os
import time
import instaloader
import banner
import sys

ua = UserAgent()
ua['google chrome']
head = {'User-Agnet':ua.random}

def check(user):
    ua['google chrome']
    head = {'User-Agent':ua.random }
    us = user
    url = "https://www.instagram.com/"+us+"/?hl=en"
    print(colored('LINK TO THE INSTAGRAM --->>', 'red'),colored(url,'green'))
    print("\n")
    x = requests.get(url, headers=head)
    print(x.status_code)
    soup = BeautifulSoup(x.content, 'html.parser')
    meta = soup.find('title')
    meta = meta.get_text()
    print("\n")
    print(colored("------------------------", 'yellow')+colored("RECON STARTED", 'red')+colored("----------------------------", 'yellow'))
    print("\n")
    if meta == 'Instagram':
        print(colored("NOT FOUND!!!"+"IT IS NOT INSTAGRAM", 'red', attrs=['bold']))
        print(colored("CHECK WITH THE USERNAME!!!", 'red', attrs=['bold']))
        sys.exit()
    else:
        print((colored("FOUND!!!  "+"YES, IT IS IN INSTAGRAM", 'green', attrs=['bold'])))
        print("\n")
        print(colored('username on instagram --> ', 'green', attrs=['dark'])+" "+colored('@'+us, 'red'))
        print("\n")

def followers(user):
    ua['edge']
    head = {'User-Agent':ua.random }
    us = user
    uurl = "https://www.instagram.com/"+us+"/?hl=en"
    response1 = requests.get(uurl, headers=head)
    soup  = BeautifulSoup(response1.content, 'html.parser')
    meta1 = soup.find('meta', property='og:description')
    if meta1:
        content = meta1.get('content')
        counts = re.findall(r'(\d+(?:\.\d+)?(?:K|M)?)\s(Followers|Following|Posts)', content)
        print(colored("DETAILS OF "+user+":", 'red'))
        for count in counts:
            print("\n")
            print(colored(count[1] + ': ' + count[0], 'green'))
   ####
def json_create(user):
    us = user
    url = 'https://www.instagram.com/'+us+'/?hl=en'
    response2 = requests.get(url, headers=head)
    print(response2.status_code)
    soup = BeautifulSoup(response2.text, 'html.parser')
    script = soup.find('script', attrs={'type': 'application/ld+json'})
    json_data = json.loads(script.contents[0])
    print(json_data)
    if os.path.exists(us):
        os.system("rm -rf"+" "+us)
        os.mkdir(us)
    else:
        os.mkdir(us)
    
    os.chdir(us)
    dir = os.getcwd()
    with open('output.json', 'w') as f:
        json.dump(json_data, f)
        print("\n")
        print(colored("DIRECTORY CREATED ->"+dir, 'green'))
         ###
def bio(user):
    time.sleep(5)
    us = user
    with open('output.json', 'r') as R:
        data = json.load(R)
        des = data['description']
        print("\n")
        print(colored("BIO OF"+" "+us,'red')+":"+"\n\n"+" "+colored(des,'blue'))
    ####
def image_download():
    with open('output.json', 'r') as f:
        data = json.load(f)
        image_url = data['author']['image']
        response3 = requests.get(image_url)
        with open('image.jpg', 'wb') as f:
            f.write(response3.content)
            pwd = os.getcwd()
            print("\n")
            print(colored("IMAGE SAVED AT --> "+pwd, 'green'))
            ###
def isprivateornot(user):
    loader = instaloader.Instaloader()
    profile_name = user
    profile = instaloader.Profile.from_username(loader.context, profile_name)
    if profile.is_private:
        print(colored("\n**The profile"+" "+user+" "+"is private\n", 'red'))
    else:
        print(colored("\n**The profile"+" "+user+" "+"is public\n", 'green'))
        ###
def isverify(user):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, user)
    if profile.is_verified:
        print(colored("\n"+"The account is verified", 'green', attrs=['bold']))
    else:
        print(colored("\n"+"The account is not verified", 'red', attrs=['bold']))
        ###
def isbussiness(user):
    with open('output.json', 'r') as f:
        business = json.load(f)
        bus = business['author']['@type']
        if bus == 'Person':
            print(colored("\n"+"The account is Personal Account"+"\n", 'red', attrs=['bold']))
        else:
            print(colored("\n"+"The account is Bussiness Account"+"\n", 'green', attrs=['bold']))
          ###
if __name__ == '__main__':
    fu = input(colored('ENTER AN INSTAGRAM ID--->', 'yellow', attrs=['bold']))
    print("\n")
    check(user = fu)
    #isprivateornot(user = fu)
    followers(user = fu)
    json_create(user = fu)
    bio(user = fu)
    image_download()
    #isverify(user=fu)
    isbussiness(user=fu)

