'''import py
from py locals *import'''
#Get HTML page

from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div',class+='card')

    for course in course_cards:
        course_name = course.h5.text
        course_price= course.a.text.split()[-1]

        print(course_name)
        print(course_price)

