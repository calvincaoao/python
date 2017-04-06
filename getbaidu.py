# -*- coding: utf-8 -*-   
#--------------------------------  
#   program: 百度贴吧爬虫  
#   date: 2014.4.29  
#--------------------------------  
  
from pyquery import PyQuery as pq  
import urllib2  
import re  
  
class tiebaSpider:  
    def __init__(self,link):  
        #只看楼主页面  
        self.url = link+'?see_lz=1'  
        #读取页面  
        self.raw_html = urllib2.urlopen(self.url).read().decode('gbk')  
        #获得贴子标题  
        self.title = re.findall('<h1.*?>(.*?)</h1>',self.raw_html)[0]  
        #总共页数  
        self.total_pages = int(re.findall(r'class="red">(\d+?)<',self.raw_html)[0])  
        self.contents = []  
  
    def get_contents(self):  
        """获取所有页面的内容"""  
  
        page = self.url+'&pn='   
        for i in range(1,self.total_pages+1):  
            #爬取每个页面  
            print u'正在爬取第%d页内容...' %i  
            raw_page = urllib2.urlopen(page+str(i)).read().decode('gbk')  
            raw_contents = re.findall('id="post_content.*?>(.*?)</div>',raw_page)  
            #处理页面，获得楼主的post cotent  
            dealed_contents=pq(raw_contents).map(lambda i,e:pq(e).text())  
              
            for content in dealed_contents:  
                content = (content+'\n\n').encode('utf-8') #忘加encode，调试了许久  
                self.contents.append(content)  
  
    def save_contents(self):  
        """保存content，写入txt文件中"""  
  
        self.get_contents()  
        f = open(self.title+'.txt','w+')  
        f.writelines(self.contents)  
        f.close()  
  
def main():  
    print u"请输入百度贴吧贴子链接"  
    link = str(raw_input())  
    spider = tiebaSpider(link)  
    spider.save_contents()  
  
if __name__ == "__main__":  
    main()  