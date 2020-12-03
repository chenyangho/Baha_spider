import requests as rq
from bs4 import BeautifulSoup
import time

# def sleeptime(hour,min,sec):
#     return hour*3600 + min*60 + sec

imgfolder = "C:\\Users\\2200432\\Desktop\\python\\chat\\image"
baha_url = 'https://gnn.gamer.com.tw/'

def catch():
	i = 1
	r = rq.get(baha_url)
	if r.status_code == rq.codes.ok:
		soup = BeautifulSoup(r.text, "html.parser")
		url = soup.find_all("div", class_="GN-lbox2B", limit=25)
		for p in url:
			#page_url.append("https:" + p.select_one("a").get("href"))
			img_r = rq.get(p.select_one("img").get("src")).content
			with open('%s\\%s%s.jpg' % (imgfolder, '圖片', i), 'wb') as f:
				f.write(img_r)
			title_text = p.find("h1")
			#title.append(title_text.select_one("a").getText())
			words = p.find("p")
			#text.append(words.getText()[:-8])
			data.append(["https:" + p.select_one("a").get("href"),p.select_one("img").get("src"),title_text.select_one("a").getText(),words.getText()[:-7].strip()])
			i += 1
		print("Finish")
	else:
		print("網址or網頁資料有問題")

def write_in_file():
	with open("BahaData.csv", "w", encoding = "UTF-8-sig") as file:
		file.write("網頁URL,圖片URL,標題文字,內文\n")
		for d in data:
			file.write(str(d) + "\n")

if __name__	== '__main__':
	# page_url = []
	# img_url = []
	# title =[]
	# text = []
	data = []
	catch()
	write_in_file()
