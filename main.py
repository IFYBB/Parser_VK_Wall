import requests
import csv

def take_1000_posts():
    token = '3220e5bb3220e5bb3220e5bb8132566193332203220e5bb520f1eaf7efaa032aad09f37'
    version = 5.92
    domain = 'skillbox_education'
    offset = 0
    count = 100
    all_posts = []

    while offset<1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count':count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset+=100
        all_posts.extend(data)
    return all_posts

def file_writer(data):
    with open('SB.csv', 'w', encoding='utf-16') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'reposts', 'comments', 'views', 'date', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['reposts']['count'], post['comments']['count'], post['views']['count'], post['date'], post['text'], img_url))

all_posts = take_1000_posts()
file_writer(all_posts)



