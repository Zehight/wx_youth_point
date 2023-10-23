import json

import requests
from qcloud_cos import CosConfig, CosS3Client

import config

response = requests.get("http://api.weixin.qq.com/_/cos/getauth")
info=json.loads(response.text)
# 1. 设置用户属性, 包括 secret_id, secret_key, region 等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
tmp_secret_id = info['TmpSecretId']     # 临时密钥的 SecretId，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
tmp_secret_key = info['TmpSecretKey']   # 临时密钥的 SecretKey，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
token = info['Token']                # 临时密钥的 Token，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
ExpiredTime = info['ExpiredTime']      # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
cos_config = CosConfig(Region=config.cos_region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key, Token=token)
client = CosS3Client(cos_config)