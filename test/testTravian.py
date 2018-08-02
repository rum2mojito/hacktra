import travian

url = "https://tx2.travian.com"
email = 'solution@aliyun.com'
password = 'sjtumorui1027'
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
