# ElasticSearch
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Getting Started
**這是簡單實現 ElasticSearch 和 flask 結合的範例 。下面是如何安裝和使用這個工具的步驟。**

### Prerequisites
* python 3.11
* pip
* ElasticSearch 8.8.2

### Installing
**1.clone repository 到 local。**
```shell
git clone https://github.com/zzhewei/elasticsearch.git
```

**2.創建虛擬環境並安裝相關套件**
```shell
python -m venv .venv
. .\.venv\Scripts\activate
pip install -r requirements.txt
```

**3.安裝 ElasticSearch**
```shell
docker-compose up -d
```
**如果出現 max virtual memory areas vm.max_map_count [65530]  is too low, increase to at least [262144]**

**輸入:**
```shell
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```
**reference : https://stackoverflow.com/questions/42111566/elasticsearch-in-windows-docker-image-vm-max-map-count**



### Usage
**1.命令列輸入:**
```shell
python -m flask run --host=0.0.0.0
```
**2.[網址測試](http://127.0.0.1:5000/API/)**

## Authors

* **ZheWei** - *Initial work* - [ZheWei](https://github.com/zzhewei)
