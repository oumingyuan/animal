# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne import Iterable
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
import json


class HelloWorldService(ServiceBase):

    # 传入参数是字符串
    @rpc(Unicode, _returns=Iterable(Unicode))
    def ess_information(self, data):
        print("*************" + data)
        dic = {"a": 1, "b": 2}
        return HttpResponse(json.dumps(dic))

    # 传入参数是图片
    @rpc(Unicode, _returns=Iterable(Unicode))
    def picture(self, data):
        print("*************" + data)
        dic = {"a": 1, "b": 2}
        return HttpResponse(json.dumps(dic))


application = Application([HelloWorldService],
                          tns='spyne.examples.hello',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11()
                          )

information_app = csrf_exempt(DjangoApplication(application))
