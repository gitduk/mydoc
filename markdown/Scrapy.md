# Scrapy

### 实用的 Command line tool

```shell
# 列举蜘蛛模板列表
$ scrapy genspider -l
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed

# 实用默认模板创建蜘蛛
$ scrapy genspider example example.com
Created spider 'example' using template 'basic'

# 自定义模板创建蜘蛛
$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'

# 输出蜘蛛列表
$ scrapy list
spider1
spider2

# 开启一个scrapy shell
$ scrapy shell [url]
# 不开启日志
$ scrapy shell --nolog [url]
# 禁用重定向
$ scrapy shell --no-redirect --nolog [url]
```





### scrapy 数据流向







### 参考网址

- https://docs.scrapy.org/en/latest/intro/tutorial.html