import os

dev_config = {
    'username': 'root',
    'password': 'gJpzkWv9',
    'db_address': 'sh-cynosdbmysql-grp-bjczm24y.sql.tencentcdb.com:26903',
    'SecretId': 'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey': '543z8DNeprhPzMUCi2GKDEG94rW6Wisv',
    'data_base': 'youth_point',
    'app_id': 'wx4f2dbbae1029571a',
    'app_secret': '8f5de26f06c3c42e5eec051738b422b9',
    'dev': True,
    'img_bucket_name': 'vote-img-1259115987',
    'small_img_bucket_name': 'vote-small-img-1259115987',
    'cos_bucket':'7072-prod-8g1tj3ti7395394a-1318978931',
    'cos_region':'ap-shanghai'
}

now_config = dev_config

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
data_base = os.environ.get("DATA_BASE", now_config['data_base'])


API_GATEWAY = os.environ.get("API_GATEWAY", '')

# 腾讯云cos
SecretId = os.environ.get("secret_id", now_config['SecretId'])
SecretKey = os.environ.get("secret_key", now_config['SecretKey'])

app_id = os.environ.get("APP_ID", now_config['app_id'])
app_secret = os.environ.get("APP_SECRET", now_config['app_secret'])

# 微信云托管cos
cos_bucket = os.environ.get("COS_BUCKET",now_config['cos_bucket'])
cos_region = os.environ.get("COS_REGION",now_config['cos_region'])

dev = os.environ.get("DEV", now_config['dev'])
img_bucket_name = os.environ.get("IMG_BUCKET_NAME", now_config['img_bucket_name'])
small_img_bucket_name = os.environ.get("SMALL_IMG_BUCKET_NAME", now_config['small_img_bucket_name'])
