#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def notify(message):
	payload = {'message':message}
	return _lineNotify(payload)

def notifyPicture(message,url):
	payload = {'message':message,'imageThumbnail':url,'imageFullsize':url}
	return _lineNotify(payload)

def notifySticker(message,stickerID,stickerPackageID):
	payload = {'message':message,'stickerPackageId':stickerPackageID,'stickerId':stickerID}
	return _lineNotify(payload)

def _lineNotify(payload):
	import requests
	url = 'https://notify-api.line.me/api/notify'
	token = '5TnTbap9pQ6NdDlxpnePC8w0QncxvidtoH6a8w'
	headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
	return requests.post(url, headers=headers, data=payload)

print (notify('สวัสดี hello'))
print (notifySticker("สวัสดี ทดสอบส่งสติกเกอร์",2,1))
print (notifyPicture("สวัสดี ทดสอบส่งรูปภาพ","URL:Picture"))
