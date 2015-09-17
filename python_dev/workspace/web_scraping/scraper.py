# coding: utf-8

from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "/home/acetakwas/dev/python_dev/workspace/web_scraping/test_page/index.html/"
	
SEC_URL = "file:///home/acetakwas/dev/python_dev/workspace/web_scraping/test_page/index.html#table-of_contents"


def get_toc_links(section_url):
	# section_url is the url to the section of the page to be fetched; usually a <DIV></DIV>
	html = urlopen(section_url).read()
	soup = BeautifulSoup(html, "lxml")
	simple = soup.find("ul", "simple")	#here we find the <UL> element with an id  - "simple"
	toc_links = [BASE_URL +li.a["href"] for li in simple.findAll("li")]
	print "\n\tI got", toc_links
	return toc_links


# As a demo, get table of contents links
get_toc_links(SEC_URL)
