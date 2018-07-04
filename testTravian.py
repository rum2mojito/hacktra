import travian

url = "https://tx2.travian.com"
email = 'wead3105@sjtu.edu.cn'
password = 'a98741512'
tr = travian.travian(url, email, password)
tr.login_()
tr.resourceInformation()
tr.buildingInformation()
#tr.resourceInformation()

# tr.inputTask( "update21", 'UPDATE', 21)
# tr.doTask()

tr.getResourceStatus()
# tr.info()
# tr.resourceUpdate(1)
