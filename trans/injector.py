from bs4 import BeautifulSoup
html = open("template.html").read()
soup = BeautifulSoup(html)
new_div = soup.new_tag('div')
new_div.string="----------------------------------------------------"

soup.html.insert(5, new_div)
print(soup)
		

#if __name__ == "__main__" :
#        addTag()
		