from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())


# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')
#all_images = soup.find_all('img')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye') #class must have an underscore since it is a reserved word in python

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')


#print('list items:', all_list_items)
#print('------')
#print('divs:', all_divs)
#print('------')
#print('goodbye elements:', all_goodbye_elements)
#print('------')
#print('french stuff:', all_french_list_items)
#print('------')
#print('hello id elements:', all_hello_elements)
#print('------')

#print(type(all_list_items[0])) #<class 'bs4.element.Tag'>
#print('------')


#for li in all_list_items: #just gets us the strings within the tags
#  print(li.string)
#print('------')


#for child in all_hello_elements[0].children:
#  print(child.string) #None because the first child of our <div> is just the string “We say Hello!”
#print('------')


#find_all way:
#print('List items within the hello tag')
hello_list_items = all_hello_elements[0].find_all('li')
#print (hello_list_items)
#print('------')

#better way:
the_hello_element = soup.find(id='hello-list')
#print(the_hello_element)
#print('------')


img_tag = soup.find('img') #accesses attributes (something inside the tag) of a tag by treating the tag as a dictionary
#print('The img source:')
#print(img_tag['src'])
#print('------')


goodbye_list_items = all_goodbye_elements[0].find_all('li')
print("These are the elements of the goodbye list:")
for li in goodbye_list_items:
    print(li.string)
print('------')
print("The image width is:")
print(img_tag['width'])
print('------')
print("The url that the a-tag points to is:")
a_tag = soup.find('a')
print(a_tag['href'])
print('------')
