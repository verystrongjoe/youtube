# youtube

It is a python module to crawl the data from the youtube.

## Objective
First of all, This is really good one trying python scrapy in windows 7 64 bit with firewall. 

Seconcd, you can crawl your favorite and playlists from youtube.

## Prerequisite

These library are dependencies that needs for scrapy to be installed .

### proxy configuration ( set the environment variables)
set http_proxy=http://proxy_ip:proxyport
set https_proxy=https://proxy_ip:proxyport

1. First, install every library where located in "lib-for-windows7-64bit" folder.

2. Second, install every dependencies with the easy_install command.

easy_install w3lib
easy_install queueLib

easy_install enum34   
easy_install ipaddress
easy_install pyasn1

easy_install idna 
easy_install cffi 
easy_install characteristic 
easy_install pyasn1-modules

easy_install service-identity
easy_install cssselect


pip install cffi-0.9.0-cp27-none-win_amd64.whl
pip install cryptography-0.7.2-cp27-none-win_amd64.whl
pip install pyOpenSSL-0.15.1-py2.py3-none-any.whl
pip install Scrapy-1.0.3-py2-none-any.whl


If you are using Anaconda IDE without installing the pure python, please add the registry like the following link.
https://avaminzhang.wordpress.com/2011/11/24/python-version-2-7-required-which-was-not-found-in-the-registry/


