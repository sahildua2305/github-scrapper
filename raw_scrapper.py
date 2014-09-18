import requests
import json
from pprint import pprint

def print_user_details(user_json):
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

def print_repo_details(repo):
    print "NAME : "+str(repo['name'])
    print "HTML-URL : "+str(repo['html_url'])
    print "FORK COUNT : "+str(repo['forks_count'])
    print "STARGAZERS COUNT : "+str(repo['stargazers_count'])
    print "WATCHERS COUNT : "+str(repo['watchers_count'])
    print "OPEN ISSUES : "+ str(repo['open_issues'])
    print "LANGUAGE : "+str(repo['language'])
    print
    print "*************************************************"

login_params = {'username': 'sahildua2305',
                'password': ''}
#response = requests.get('https://api.github.com/', params=login_params)

username = raw_input()
user = requests.get('https://api.github.com/users/'+username)
#user = requests.get('https://api.github.com/search/users/', params={'q':'sahil'})
user_json = json.loads(user.content or user.text)
print_user_details(user_json)
#pprint(user_json)

repos = requests.get('https://api.github.com/users/'+username+'/repos', params={'type':'owner','sort':'pushed'})
repos_json = (json.loads(repos.content))

for i in repos_json:
    print_repo_details(i)

#response = requests.get('https://api.github.com/repos/sahildua2305/tweetogram/forks')
#pprint(json.loads(response.content))

