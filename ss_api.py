import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

with open('cinfo.txt') as cinfo:
    lines = cinfo.readlines()

with open('urls.txt') as urlstxt:
    url_lines = urlstxt.readlines()

urls = [url.strip('\n') for url in url_lines]

USERNAME = lines[0].strip('\n')
ACCESS_KEY = lines[1].strip('\n')
API_URL = 'https://www.browserstack.com/screenshots'

print("Username: {}".format(USERNAME))
print("Acess Key: {}".format(ACCESS_KEY))
print("Total number of URLs: {}".format(len(list(urls))))
for i in range(0, len(list(urls))):
    print("URL {}: {}".format(i + 1, urls[i]))


headers = {'content-type': 'application/json', 'Accept': 'application/json'}

with open('browser.json') as browser_file:
    payload = json.load(browser_file)


timestr = time.strftime("%Y%m%d-%H%M%S")

text_file = open(timestr + ".txt", "a")

for i in range(0, len(list(urls))):
    payload.update({"url": urls[i]})
    resp = requests.post(API_URL, auth=(USERNAME, ACCESS_KEY),
                         data=json.dumps(payload), headers=headers,
                         verify=False)
    if resp.json()['screenshots'][0]['state'] != 'done':
        time.sleep(60)
    job_url = API_URL + "/" + resp.json()['job_id']
    text_file.write(job_url + '\n')
    print(job_url)

text_file.close()
