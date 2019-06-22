#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import requests, re

dict_num = {
	'1' : '社工欺诈',
	'2' : '信息诈骗',
	'3' : '虚假广告',
	'4' : '恶意文件',
	'5' : '博彩网站',
	'6' : '色情内容',
	'7' : '垃圾信息',
	'8' : '非法内容'
}

geturl = requests.get('https://urlsec.qq.com/cgi/risk/getList?_=1561204825663' , timeout=3)
s_code = geturl.status_code
geturl.encoding = 'utf-8'
if s_code == 200:
	print('#访问成功')
	web_page = geturl.text
	pattern = re.compile(r'evilclass":"(\d)","src_url":"(.*?)"}') 
	result1 = pattern.findall(web_page)
	print(result1)
	for weburl in result1:
		with open('腾讯风险网站.txt','a',encoding="utf-8") as f:
			num = weburl[0]
			weburl_text = weburl[1].replace("\\", "")
			write_text = weburl_text + ' ' + dict_num[num] + '\n' 
			f.write(write_text)
else:
	print('！访问失败')
exit()