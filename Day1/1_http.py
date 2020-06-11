'''
1. HTTP请求方式
（1）get请求
    特点：比较简单；明文传输不安全
（2）POST请求
    特点：数据整体没有限制；较为安全；可上传文件
    上述为请求Request首部Header
    Accept：文件的格式
    Accept-Encoding：编码格式
    Connection：长连接 短连接
    Cookie：缓存信息（用户信息）
    Host：主机名
    Referer：上一个页面地址
    User-Agent：浏览器及用户信息

    同时服务器响应报文Response
（3）...

2. 爬虫意义 使用代码模拟用户批量地发送网络请求 批量获取数据

3. 爬虫价值
    i.      买卖数据
    ii.     数据分析
    iii.    流量
    iv.     阿里指数；百度指数

4. 爬虫分类
    i.      通用爬虫
            -使用搜索引擎获取
            -特点：速度快，开放性高；但目标不明确，返回内容大多无效

    ii.     聚焦爬虫（Focused Spider）
            -特点：目标明确，需求准确，返回内容固定
            -增量式（就是爬取目标各个页面）

    iii.    Deep深度爬虫
            -爬取动态书据（JS代码，加密js）
            -静态数据（html,css）
5. Robots 是否允许其他爬虫（通用爬虫）爬取内容
          -对聚焦爬虫无用

6.  反爬虫

7.  工作原理（基本步骤）
    i.      明确目标url
    ii.     使用代码发送请求获取数据
    iii.    解析获取数据
    （以上三步循环）
    iv.     数据存储

8.  使用库
    i.      urlib.request
            -get
                -存在问题：汉子报错
            -open
            -post
            -handle
            -urlError
    ii.     urlib2
    iii.    xpath   bs4
    iv.     request
    v.
    vi.
'''