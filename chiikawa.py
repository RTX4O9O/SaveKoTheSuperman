import requests

URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSfh4xiVkpZZ9pbiVuFwjFmwxBobhKZtdqIdjB81rbcSY6QuZw/formResponse'
DATA = {
	"entry.1458837562": "柯文哲",
	"entry.114924327": "詐騙集團首領",
	"entry.877915436": "1959",
	"entry.1190079061": "你好，我是柯文哲，我没有圖利京華城。我現在人在藏壽司，還差200元就能再抽一次吉伊卡哇。你現在幫我，我承諾出獄後讓你加入民眾黨，並幫你安排一個不分區立委，謝謝。",
}

while True:
    res = requests.post(URL, DATA)
    print(res.status_code, res.reason)