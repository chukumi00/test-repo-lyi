from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.nate.com/')
source = response.text
#print(source)

soup = BeautifulSoup(source, 'html.parser')

#title = soup.select_one('span.txt_rank')

#print(title.text.strip())

#results = soup.select('#olLiveIssueKeyword > li:nth-child(1)') #list형식
results = soup.select('#olLiveIssueKeyword > li') #<li>의 list객체
#print(results)

for li in results:
    span = li.select_one('.txt_rank')
    #print(span)

    if span:
        print(span.get_text(strip=True))


# print(result.span.text)
# print(result[0].span.text)
# print(result[0].text)