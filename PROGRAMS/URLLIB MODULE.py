import urllib.request as url

# connection
webUrl=url.urlopen('https://www.github.com/manmay2')

#result
print("result code: "+str(webUrl.getcode()))


#read the data
data=webUrl.read()
print(data)
