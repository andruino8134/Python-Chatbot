print('***  *  *  ****  *****  ****  ****  *****')
print('*    ****  ****    *    *  *  *  *    *  ')
print('*    *  *  *  *    *    ****  *  *    *  ')
print('***  *  *  *  *    *    *  *  *  *    *  ')
print('                        ****  ****    *  ')
import datetime  
from datetime import date
import pyowm
import webbrowser
import re
import random
from random import randint
from PyDictionary import PyDictionary
import feedparser
print('hello iam Tod!,what can i do for you?')
def time():
    print(datetime.datetime.now())
def date():
    print(datetime.date.today())
def add():
    integers= list(map(int, re.findall('\d+',enter)))
    print('the sum is',sum(integers))
def subtract():
    integers= list(map(int, re.findall('\d+',enter)))
    print('the answer is',integers[1]-integers[0])
def product():
    num= list(map(int, re.findall('\d+',enter)))
    print('the product is',num[0]*num[1])          
def division():
    num=list(map(int, re.findall('\d+',enter)))
    print('the quotient is',num[0]/num[1])
def temp():
    location=input('enter location')
    countryid=input('enter countryid')
    owm=pyowm.OWM('6ec36b52be3e1347f1cf9bf07a73c37d')
    sf=owm.weather_at_place(location+','+countryid)
    weather=sf.get_weather()
    print(weather.get_temperature('celsius')['temp'],'degree celsius')
def temp1():
    countryid=input('enter countryid')
    owm=pyowm.OWM('6ec36b52be3e1347f1cf9bf07a73c37d')
    sf=owm.weather_at_place(location+','+countryid)
    weather=sf.get_weather()
    print(weather.get_temperature('celsius')['temp'],'degree celsius')
def temp2():  #error
    location1=enter[22:]
    countryid=input('enter countryid')
    owm=pyowm.OWM('6ec36b52be3e1347f1cf9bf07a73c37d')
    sf=owm.weather_at_place(location1+','+countryid)
    weather=sf.get_weather()
    print(weather.get_temperature('celsius')['temp'],'degree celsius')
def simple():
    if enter=='how are you':
        print("I'm fine")
    elif enter=='hello':
        print('hi there')
    elif enter=='how are you?':
        print("I'm fine")
    elif enter=='good morning':
        print('good morning')
    elif enter=='good afternoon':
        print('good afternoon')
    elif enter=='good night':
        print('bye go to sleep')
    elif enter=='who made you':
        print('I was made by Andrew')
    elif enter=='who made you?':
        print('I was made by Andrew')
def cointoss():
   flip=random.randint(0,1)
   if flip==1:
       print('i got heads')
   else:
       print('i got tails')
    
def web():
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s'%enter)
def dicti():
    word=enter[22:]
    wordmean=[word]
    dictionary=PyDictionary(wordmean[0])
    print(dictionary.getMeanings())
def news():
    NewsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    entry = NewsFeed.entries[1]
    print(entry.published)
    print("******")
    print(entry.summary)
    print("------News Link--------")
    print(entry.link)
def dicti1():
    word=enter[10:]
    wordmean=[word]
    dictionary=PyDictionary(wordmean[0])
    print(dictionary.getMeanings())
    
while True:
 enter=input('ask me')
 if enter=='tell me the date':
    date()
 elif enter=='whats todays date':
     date()
 elif enter=="what's todays date":
    date()
 elif enter=='what is todays date?':
     date()
 elif enter=='what is todays date':
     date()
 elif enter=='what is the temperature outside':
    temp()
 elif enter=='how are you':
    simple()
 elif enter=='goodmorning':
     simple()
 elif enter=='good afternoon':
     simple()
 elif enter=='good night':
     simple()
 elif enter=='hello':
     simple()
 elif enter=='Hello':
     print('hello')
 elif enter=='good morning':
     simple()
 elif enter=='who made you':
     simple()
 elif enter=='who made you?':
     simple()
 elif enter=='i want to search something':
     enter=input('enter search keyword')
     web()
 elif 'weather in' in enter:
     location=enter[10:]
     temp1()
 elif 'what is the weather' in enter: #error
     temp2()
 elif 'add' in enter:
     add()
 elif 'subtract' in enter:
     subtract()
 elif 'multiply' in enter:
     product()
 elif enter=='date':
     date()
 elif enter=='who are you':
     print('A Chatbot')
 elif enter=='hows life':
     print('very good')
 elif 'divide' in enter:
     division()
 elif 'toss a coin' in enter:   
     cointoss()
 elif enter=='thanks':
     print(' you are welcome!')
 elif enter=='time':
     time()
 elif enter=='what time is it':
     time()
 elif enter=='whats the time':
     time()
 elif enter=='hi':
     print('hi there')
 elif 'what is the meaning' in enter:
     dicti()
 elif 'latest news' in enter:
     news()
 elif 'tell me the news' in enter:
     news()
 elif 'meaning of' in enter:
     dicti1()
 else:
    print('i will search it for you in the web')
    web()
