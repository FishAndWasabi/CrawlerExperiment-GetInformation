# CrawlerExperiment-Get-Information
# 爬虫实验： 获取信息

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

非常简单的爬取程序

## Table of Contents

- [Time](#time)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [License](#license)

## Time

记录了一下时间：
- 编写: 20 min
- 封装：10 min


## Background

在这个程序中，主要用到下列知识：

- 抓包分析

## Install

### 环境

暂无python2支持
- python == 3.9
- conda == 4.9.2



### 下载

由于该程序的主体仅一个函数，将代码下载至本地即可

```
git clone https://github.com/FishAndWasabi/CrawlerExperiment-Get-Information.git
cd CrawlerExperiment-Get-Information
```


## Usage

```python
from crawler import Crawler
crawler.run('储水式电热水器 2008版', '产品型号', 'bbb')
print(crawler.result)
```

## Maintainers

[@FishAndWasabi](https://github.com/FishAndWasabi).



## License

[MIT](LICENSE) © Yuming Chen