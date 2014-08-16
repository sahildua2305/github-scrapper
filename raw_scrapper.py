import requests
import json
from pprint import pprint

login_params = {'username': 'sahildua2305',
                'password': '*********'}
#response = requests.get('https://api.github.com/', params=login_params)

username = raw_input()
user = requests.get('https://api.github.com/users/'+username)
user_json = json.loads(user.content or user.text)
#pprint(user_json)
print "         DETAILS OF THE USER "
print "USERNAME : "+str(user_json['name'])
print "GITHUB LINK : "+str(user_json['html_url'])
print "LOCATION : "+str(user_json['location'])
print "EMAIL : "+str(user_json['email'])
print "BIO : "+str(user_json['bio'])
print "FOLLOWERS : "+str(user_json['followers'])
print "FOLLOWING : "+str(user_json['following'])
print "PUBLIC REPOS : "+str(user_json['public_repos'])
print "PUBLIC GISTS : "+str(user_json['public_gists'])
print
print "*************************************************"

repos = requests.get('https://api.github.com/users/'+username+'/repos', params={'type':'owner','sort':'pushed'})
repos_json = (json.loads(repos.content))

for i in repos_json:
    print "NAME : "+str(i['name'])
    print "HTML-URL : "+str(i['html_url'])
    print "FORK COUNT : "+str(i['forks_count'])
    print "STARGAZERS COUNT : "+str(i['stargazers_count'])
    print "WATCHERS COUNT : "+str(i['watchers_count'])
    print "OPEN ISSUES : "+ str(i['open_issues'])
    print "LANGUAGE : "+str(i['language'])
    print
    print "*************************************************"

#response = requests.get('https://api.github.com/repos/sahildua2305/tweetogram/forks')
#pprint(json.loads(response.content))

