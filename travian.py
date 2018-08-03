import requests
import re
import globalVar
import resource
import task
import time
from queue import Queue
from bs4 import BeautifulSoup

class travian:
    def __init__(self, url, email, password):
        self.url = url
        self.email = email
        self.password = password
        self.resourceList = []
        self.building = False
        self.q = Queue()

    def doTask(self):
        if (not (self.building)):
            t = self.q.get()
            if (t.type == 'UPDATE'):
                self.resourceUpdate(t.obj)

    def inputTask(self, taskName, taskType, taskObjId = 0):
        self.q.put(task.task(taskName, taskType, taskObjId))

    def check(self):
        for ele in self.resourceList:
            if (ele.lumber <= self.lumber and ele.clay <= self.clay and ele.iron <= self.iron and ele.crop <= self.crop):
                ele.ready = True
            else:
                ele.ready = False

    def resourceUpdate(self, id):
        self.check()
        if (self.resourceList[id-1].ready):
            tmpDorf = self.getContent(self.url + globalVar.BUILDINGID + str(id))
            text = str(tmpDorf)
            try:
                #print (tmpDorf)
                soup = BeautifulSoup(tmpDorf, 'lxml')
                c = str(self.getElement(text, '.*?&amp;c=(.*?)\';.*?')[0])
                href = str(self.getElement(text, '.*?onclick="window.location.href = \'(.*?)a=.*?')[0])
                update_data = {
                    'a': str(id),
                    'c': c,
                }
                headers_base = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
                    'Connection': 'keep-alive',
                    'Host': 'tx2.travian.com',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
                    'Referer': 'https://tx2.travian.com/build.php?id=' + str(id),
                }
                requestUrl = self.url + '/' + href + 'a=' + str(id) + '&' + 'c=' + c
                print(globalVar.LOGINFO + 'Connect to ' + requestUrl)
                content = self.session.post(requestUrl, headers=headers_base, data=update_data)
                # print (globalVar.LOGINFO + 'Connect to ' + updateUrl)
                # self.getContent(updateUrl)
                self.update()
                self.getResourceStatus()
                print (globalVar.LOGINFO + 'UPDATE SUCCESS')
            except Exception as err:
                print(globalVar.LOGFAIL + 'Something error...  ' + err.messege)
                self.update()
                self.check()
                self.resourceUpdate(id)
        else:
            print (globalVar.LOGWARN + 'UNREADY')
            print ('=================================================')
            print ('[RESOURCE]:' + '\t' + self.resourceList[id-1].name + '\t' + '[UPDATE]: ' + '\t' + str(self.resourceList[id-1].level+1))
            print('[LUMBER]:' + '\t' + str(self.lumber) + '/' + str(self.resourceList[id - 1].lumber))
            print('[CLAY]:' + '\t' + str(self.clay) + '/' + str(self.resourceList[id - 1].clay))
            print('[IRON]:' + '\t' + str(self.iron) + '/' + str(self.resourceList[id - 1].iron))
            print('[CROP]:' + '\t' + str(self.crop) + '/' + str(self.resourceList[id - 1].crop))

    def update(self):
        self.dorf1 = self.getContent(self.url + globalVar.RESOURCES)
        self.dorf2 = self.getContent(self.url + globalVar.BUILDINGS)
        self.getResourceStatus()

    def getContent(self, baseurl):
        print (globalVar.LOGINFO + 'Connect to ' + baseurl)
        s = self.session.get(baseurl, verify=False)
        content = s.text.encode('utf-8')
        return s.text

    def cleanNum (self, text):
        res = ''
        for i in text:
            if i >= '0' and i <= '9':
                res += i
        return res

    def getResourceStatus(self):
        content = self.dorf1
        soup = BeautifulSoup(content, 'lxml')
        self.lumber = int(self.cleanNum(soup.find_all(id="l1")[0].text))
        self.clay = int(self.cleanNum(soup.find_all(id="l2")[0].text))
        self.iron = int(self.cleanNum(soup.find_all(id="l3")[0].text))
        self.crop = int(self.cleanNum(soup.find_all(id="l4")[0].text))

        print(globalVar.LOGINFO + '[Lumber]: ' + str(self.lumber) + ' [Clay]: ' + str(self.clay) + ' [Iron]: ' + str(
            self.iron) + ' [Crop]: ' + str(self.crop))

    def resourceInformation(self):
        content = self.dorf1
        soup = BeautifulSoup(content, 'lxml')
        divs = soup.find_all("area")
        for i in range (int(divs.__len__())-1):
            ele = divs[i]
            text = str(ele)
            name = str(self.getElement(text, '.*?title=\'(.*?) &lt;span.*?')[0])
            href = str(self.getElement(text, '.*?href="(.*?)".*?')[0])
            level = int(self.getElement(text, '.*?Level (.*?)".*?')[0])
            #print (level)
            updateWood = int(
                self.getElement(text, '.*?&lt;img class="r1" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
            updateClay = int(
                self.getElement(text, '.*?&lt;img class="r2" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
            updateIron = int(
                self.getElement(text, '.*?&lt;img class="r3" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
            updateCrop = int(
                self.getElement(text, '.*?&lt;img class="r4" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
            try:
                self.resourceList[i].update(updateWood, updateClay, updateIron, updateCrop, level)
            except:
                # self, session, id, href, name = '', level = 0, needLumber = 0, needClay = 0, needIron = 0, needCrop = 0)
                self.resourceList.append(resource.resource(self.session, i, href, name, level, updateWood, updateClay, updateIron, updateCrop))
                print (globalVar.LOGINFO + 'Creat id: ' + str(i) + '\t' + ' Type: ' + name +  '\t'+ ' Level: ' + str(level) + '\t'+ ' Href: ' + href)
        #print (divs[0])

    def buildingInformation(self):
        content = self.dorf2
        soup = BeautifulSoup(content, 'lxml')
        divs = soup.find_all("area")
        #print (divs[0])
        for i in range (int(divs.__len__())-1):
            #print(divs[i])
            ele = divs[i]
            text = str(ele)
            try:
                name = str(self.getElement(text, '.*?title=\'(.*?) &lt.*?')[0])
                href = str(self.getElement(text, '.*?href="(.*?)".*?')[0])
                level = int(self.getElement(text, '.*?Level (.*?)&lt.*?')[0])
                #print (level)
                updateWood = int(
                    self.getElement(text, '.*?&lt;img class="r1" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
                updateClay = int(
                    self.getElement(text, '.*?&lt;img class="r2" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
                updateIron = int(
                    self.getElement(text, '.*?&lt;img class="r3" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
                updateCrop = int(
                    self.getElement(text, '.*?&lt;img class="r4" src="img/x.gif" /&gt;(.*?)\\n.*?')[0])
                try:
                    self.resourceList[i+18].update(updateWood, updateClay, updateIron, updateCrop, level)
                except:
                    # self, session, id, href, name = '', level = 0, needLumber = 0, needClay = 0, needIron = 0, needCrop = 0)
                    self.resourceList.append(resource.resource(self.session, i+18, href, name, level, updateWood, updateClay, updateIron, updateCrop))
                    print (globalVar.LOGINFO + 'Creat id: ' + str(i+18) + '\t' + ' Type: ' + name +  '\t'+ ' Level: ' + str(level) + '\t'+ ' Href: ' + href)
            except:
                self.resourceList.append(resource.resource(self.session, i+18, href='', name='Building site', level=0))
                print(globalVar.LOGINFO + 'Creat id: ' + str(i+18) + '\t' + ' Type: ' + 'Building site' + '\t' + ' Level: ' + str(0) + '\t' + ' Href: ' + '')


    def info(self):
        try:
            for ele in self.resourceList:
                print (globalVar.LOGINFO + '[id]: ' + str(ele.id) + '\t' + '[Type]: ' + ele.name + '\t' + '[Level]: ' + str(ele.level))
        except Exception as err:
            print (globalVar.LOGFAIL + 'Update......   ' + err.messege)
        print(globalVar.LOGINFO + '[Lumber]: ' + str(self.lumber) + ' [Clay]: ' + str(self.clay) + ' [Iron]: ' + str(
            self.iron) + ' [Crop]: ' + str(self.crop))

    def getElement(self, text, pattern):
        match = re.findall(pattern, text)
        return match

    #get login value
    def getLogin(self, url):
        def getContent(url):
            url += '/login.php'
            r = requests.get(url)
            # request.get().content get all content in the page(url)
            return r.content
        content = getContent(url)
        pattern = re.compile('.*?<input type="hidden" name="login" value="(.*?)" />.*?')
        match = re.findall(pattern, str(content))
        login = match[0]
        return login

    def login_(self):
        print (globalVar.LOGINFO + 'Login...')
        self.login(self.url, self.email, self.password)

    def login(self, baseurl, email, password):

        login_data = {
                'name': email,
                'password': password,
                's1': 'Login',
                'w': '1920:1080',
                'login': self.getLogin(baseurl),
        }
        # header information
        headers_base = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
            'Connection': 'keep-alive',
            'Host': 'tx2.travian.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36',
            'Referer': 'https://tx2.travian.com/login.php',
        }



        baseurl += "/dorf1.php"

        content = self.session.post(baseurl, headers = headers_base, data = login_data)
        self.update()

        #print (content.text)
        # s = self.session.get("https://tx2.travian.com/dorf1.php", verify = False)
        # print (s.text.encode('utf-8'))
