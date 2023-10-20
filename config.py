import os

dev_config = {
    'username': 'root',
    'password': 'RZ3WHtJ4',
    'db_address': 'sh-cdb-php1aito.sql.tencentcdb.com:63541',
    'SecretId': 'AKIDeDPTO9i7RitzgVJwYK1a0DIDze5d6Rlt',
    'SecretKey': '543z8DNeprhPzMUCi2GKDEG94rW6Wisv',
    'data_base': 'vote',
    'app_id': 'wxbd53b7860f2c9844',
    'app_secret': '77290c01bd98b4382a9870a2f90785ec',
    'dev': True,
    'img_bucket_name': 'vote-img-1259115987',
    'small_img_bucket_name': 'vote-small-img-1259115987'
}

now_config = dev_config

# 读取数据库环境变量
username = os.environ.get("MYSQL_USERNAME", now_config['username'])
password = os.environ.get("MYSQL_PASSWORD", now_config['password'])
db_address = os.environ.get("MYSQL_ADDRESS", now_config['db_address'])
data_base = os.environ.get("DATA_BASE", now_config['data_base'])
API_GATEWAY = os.environ.get("API_GATEWAY", '')
SecretId = os.environ.get("secret_id", now_config['SecretId'])
SecretKey = os.environ.get("secret_key", now_config['SecretKey'])
app_id = os.environ.get("APP_ID", now_config['app_id'])
app_secret = os.environ.get("APP_SECRET", now_config['app_secret'])
dev = os.environ.get("DEV", now_config['dev'])
img_bucket_name = os.environ.get("IMG_BUCKET_NAME", now_config['img_bucket_name'])
small_img_bucket_name = os.environ.get("SMALL_IMG_BUCKET_NAME", now_config['small_img_bucket_name'])
