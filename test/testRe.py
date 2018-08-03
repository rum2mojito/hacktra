import sys
sys.path.append('home/parallels/Downloads/hacktra/dist')
from dist import getResource
import unittest

#url="http://answers.travian.com"
url="https://t4.answers.travian.com/index.php?view=answers&action=answer&cid=203"
re=getResource.getResource(url)
re.checkLink(url)
re.getContent(url)
#print(re.reList)
re.listFormat()