import requests

import json

def uest(sub):
    selftext = ''
    title = ''
    photo = ''
    res2str = '<Response [429]>'
    params = {'limit' : 1}
    while res2str != '<Response [200]>':
       print(res2str)
       res = requests.get(f"https://old.reddit.com/r/{sub}/top.json", params = params)
       res2str = str(res) 
       if res2str == '<Response [404]>':
          break 
       if res2str == '<Response [403]>':
          break

    for post in res.json()['data']['children']:
       title = post['data']['title']
       try:
          selftext = post['data']['selftext']
          photo = post['data']['url_overridden_by_dest']
       except: 
          photo = 'no photo'        
    print(title)

    with open('text.txt', 'w') as output_file:
       output_file.write(title)
       output_file.write(selftext)
    with open('url.txt', 'w') as output_file:
       output_file.write(photo)

'''
   while title == '':
      test += 1
      print(f'test {test}')
      try:
         for post in res.json()['data']['children']:
            title = post['data']['title']
            print(title)
      except KeyError:
         continue
'''
