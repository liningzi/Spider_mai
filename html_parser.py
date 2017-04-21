# -*- coding:utf-8 -*-
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):


    def _get_new_urls(self, page_url, soup):
        print 'in parse def _get_new_urls'
        new_urls = set()
        #/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6,re.compile(r"/item/" http://baike.baidu.com/item/Python/item/GPL.html
        links = soup.find_all('a',href = re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            print "full url is",new_full_url
            new_urls.add(new_full_url)
            #print new_full_url,page_url,new_url
        return new_urls


    def _get_new_data(self, page_url, soup):

        print 'in parse def _get_new_data'

        res_data = {}
        #url
        res_data['url'] = page_url


        #<dd class="lemmaWgt-lemmaTitle-title"><h1>*******</h1></dd>

        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #<div class="para" label-module="para">*******</div>
        summary_node = soup.find('div',class_ = "lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_count):
        print "in html_parser def parse"
        if page_url is None or html_count is None:
            return

        soup = BeautifulSoup(html_count,'html.parser',from_encoding='utf-8')

        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        #print 'paser over'
        #print new_urls


        return new_urls,new_data