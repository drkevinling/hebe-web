from bs4 import BeautifulSoup
import requests
import selenium

chrome_driver_path = "/Users/tpa/Developer/web_dev/chromedriver_mac_arm64/chromedriver"



response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
h_tag = soup.find(id="score_35323960")
bae = h_tag.getText()

print(bae)
