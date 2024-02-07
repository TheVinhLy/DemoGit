#import requests
#from bs4 import BeautifulSoup

#response = requests.get("https://www.xosobinhduong.com.vn/kqxsmiennam?lotdate=2023-02-22")
#soup = BeautifulSoup(response.content, "html.parser")
#titles = soup.findAll('h3', class_='box-title-text')
#print(soup)


'''
import requests
from bs4 import BeautifulSoup

# Gửi yêu cầu HTTP đến trang web
url = 'https://www.xosobinhduong.com.vn/'
response = requests.get(url)

# Kiểm tra trạng thái phản hồi
if response.status_code == 200:
    # Phân tích cú pháp HTML của trang web
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lấy tiêu đề của trang web
    title = soup.title.string
    print('Tiêu đề:', title)

    # Lấy toàn bộ nội dung của thẻ div có class là "content"
    content_div = soup.find('div', class_='content')
    content = content_div.get_text()
    print('Nội dung:', content)
else:
    print('Không thể kết nối đến trang web')
'''

import requests
from bs4 import BeautifulSoup
import lxml

#response = requests.get("https://www.xosobinhduong.com.vn/kqxsmiennam?lotdate=2023-02-22").text
response = requests.get("https://www.minhngoc.net/xo-so-mien-nam.html").text
soup = BeautifulSoup(response, "lxml")
#print(soup.prettify())

'''
titles = soup.findAll('td', class_='tinh')
matinh = soup.findAll('td', class_='matinh')
giai8 = soup.findAll('td', class_='giai8')
giai7 = soup.findAll('td', class_='giai7')
giai6 = soup.findAll('td', class_='giai6')
giai5 = soup.findAll('td', class_='giai5')
giai4 = soup.findAll('td', class_='giai4')
giai3 = soup.findAll('td', class_='giai3')
giai2 = soup.findAll('td', class_='giai2')
giai1 = soup.findAll('td', class_='giai1')
giaidb = soup.findAll('td', class_='giaidb')

giaidb1 = soup.find_all(attrs={"giaidb"})

print(titles)
print(matinh)
print(giai8)
print(giai7)
print(giai6)
print(giai5)
print(giai4)
print(giai3)
print(giai2)
print(giai1)
print(giaidb)
print('----------')
print(giaidb1)
'''

table = soup.find('table',class_='bkqmiennam')
print(table)