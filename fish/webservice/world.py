import suds

from suds.client import Client

ip = "127.0.0.1"
port = "8000"

# url = "http://192.168.1.235:12581/ServiceYuYue.svc?wsdl"
url = "http://%s:%s/information/?wsdl" % (ip, port)

data = "HelloWord"

client = suds.client.Client(url)

result = client.service.ess_information(data)

# getHealthyHeBei是webService提供的方法
# result = client.service.getHealthyHeBei(18210409689)

# 打印出结果
print(result)
