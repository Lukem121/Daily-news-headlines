from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from github import Github

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
newArtics = ""
for news in news_list:
    newArtics += "### **" + news.title.text + "**\n#### " + news.pubDate.text + " - Link to article: [Here](" + news.link.text +")\n---\n"

file_path = "README.md"
g = Github(GITHUB_TOKEN)
repo = g.get_repo("Lukem121/Daily-news-headlines")

file = repo.get_contents(file_path)  # Get file from branch
data = file.decoded_content.decode("utf-8")  # Get raw string data
data += newArtics
repo.update_file(file.path, "your_coemmit_message", data, file.sha)
print("Done")


