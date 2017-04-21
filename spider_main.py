# -*- coding:utf-8 -*-
from test import html_downloader
from test import html_outputer
from test import html_parser
from test import url_manager


class SpiderMain(object):
    def __init__(self):                       #初始化
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1     #记录当前爬取得是第几个url
        self.urls.add_new_url(root_url)       #将入口url添加到管理器，有待爬去的url
        while self.urls.has_new_url():
            #try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_count = self.downloader.download(new_url)  # 启动下载器下载new_url，储存在count
                new_urls,new_data = self.parser.parse(new_url,html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count = count+1

            #except:
                #print 'craw failed'


        self.outputer.output_html()




if __name__=="__main__":
    root_url = "http://baike.baidu.com/item/python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)