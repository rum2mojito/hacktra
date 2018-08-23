import globalVar

class resource:
    def __init__(self, session, id, href, name = '', level = 0, needLumber = 0, needClay = 0, needIron = 0, needCrop = 0):
        self.id = id
        self.session = session
        self.href = href
        self.name = name
        self.level = level
        self.lumber = needLumber
        self.clay = needClay
        self.iron = needIron
        self.crop = needCrop
        self.ready = False

    def getContent(self, baseurl):
        print (baseurl)
        s = self.session.get(baseurl, verify=False)
        content = s.text.encode('utf-8')
        return s.text

    def update(self, needLumber = 0, needClay = 0, needIron = 0, needCrop = 0, level = 0):
        self.level = level
        self.lumber = needLumber
        self.clay = needClay
        self.iron = needIron
        self.crop = needCrop

    def getElement(self, text, pattern):
        match = re.findall(pattern, text)
        return match