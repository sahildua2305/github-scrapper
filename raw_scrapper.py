import requests
import json
from pprint import pprint

login_params = {'username': 'sahildua2305',
                'password': 'dauduadua'}
#response = requests.get('https://api.github.com/', params=login_params)

username = raw_input()
user = requests.get('https://api.github.com/users/'+username)
user_json = json.loads(user.content or user.text)
#pprint(user_json)
print user_json['name'], user_json['html_url'], user_json['location'], user_json['email'], user_json['bio'], user_json['followers'], user_json['following'], user_json['public_repos'], user_json['public_gists']

repos = requests.get('https://api.github.com/users/'+username+'/repos', params={'type':'owner','sort':'pushed'})
repos_json = (json.loads(repos.content))

for i in repos_json:
    print i['name'],i['html_url'],i['forks_count'],i['stargazers_count'],i['watchers_count'],i['open_issues'],i['language']

#response = requests.get('https://api.github.com/repos/sahildua2305/tweetogram/forks')
#pprint(json.loads(response.content))
