from urllib.request import urlopen
def count_hello_spider()->int:
    s=urlopen('http://learnspider.vip/view/hello-spider/').read().decode()
    print(s.count('Hello, Spider~'))
count_hello_spider()
