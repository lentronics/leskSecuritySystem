# Created by Pedro Costa
# Based on Quickstart Requests Tutorial
# http://docs.python-requests.org/en/latest/user/quickstart/

import requests
import json

url = 'http://iampedrocosta.com/iampcwebapi/';

#reqData = '{"video":"somevideo", "recorded_date":"dd/mm/YYYY hh:ii:ss", "videosize":"879kb"}'

fileData = {'file': ('video.mp4', read('video.mp4'), 'media/vidapp-mp4', {'Expires': 0})}

#response = requests.post(url, data=json.dumps(reqData))
response = requests.post(url, files=fileData)

if(response.raise_for_status() == ""){
	# video has been uploaded
}else{
	# error when uploading the video through IAMPC Web API
}

print(r.text)

