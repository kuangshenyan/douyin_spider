#code:utf-8
import requests
from bs4 import BeautifulSoup
import json
session = requests.session()
url = ''
filename = "urls.txt"
def download(userid,count):
    url = 'https://www.douyin.com/aweme/v1/aweme/favorite/?user_id='+str(userid)+'&count='+str(count)+'&max_cursor=0&aid=1128'
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    myjson = json.loads(str(soup))
    with open(filename,"a+") as f:
        for i in range(count):
            video_url = myjson['aweme_list'][i]['video']['play_addr']['url_list'][0]
            print (myjson['aweme_list'][i]['video']['play_addr']['url_list'][0])
            f.write(video_url+"\n")
    f.close()

if __name__ == '__main__':
    download(88409121422,31)
