import json
import os
import sys
from io import BytesIO

import requests
from flask import current_app
from service.models import File
from PIL import Image
import config


from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client



response = requests.get("http://api.weixin.qq.com/_/cos/getauth")
info=json.loads(response.text)

print('aa')

# 1. 设置用户属性, 包括 secret_id, secret_key, region 等。Appid 已在 CosConfig 中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
tmp_secret_id = info['TmpSecretId']     # 临时密钥的 SecretId，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
tmp_secret_key = info['TmpSecretKey']   # 临时密钥的 SecretKey，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
token = info['Token']                # 临时密钥的 Token，临时密钥生成和使用指引参见 https://cloud.tencent.com/document/product/436/14048
ExpiredTime = info['ExpiredTime']      # 替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket

print(config.cos_region,tmp_secret_id,tmp_secret_key,token)
cos_config = CosConfig(Region=config.cos_region, SecretId=tmp_secret_id, SecretKey=tmp_secret_key, Token=token)
client = CosS3Client(cos_config)




# 新增
def create_func(real_file, **kwargs):
    file_name = real_file.filename
    file = File.create(file_name=file_name, **kwargs)
    file_id  = file.id
    file_save_name = file_id + '_' + file_name
    client.put_object(
        Bucket=config.cos_bucket,
        Body=real_file.read(),
        Key=file_save_name,
        EnableMD5=False
    )

    small_file = File.create(file_name=file_name, small_type='1', **kwargs)
    small_file_id = small_file.id
    file.update(small_id=small_file_id)
    small_file_save_name = small_file_id + '_' + file_name
    with Image.open(real_file) as small_real_file:
        small_real_file.save(small_file_save_name, optimize=True, quality=20)
        client.put_object_from_local_file(
            Bucket=config.cos_bucket,
            LocalFilePath=small_file_save_name,
            Key=small_file_save_name
        )
        os.remove(small_file_save_name)
    return "操作成功", file_id


# 删除
def delete_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '数据信息错误'
    file = File.get(id=kwargs['id'])
    if file:
        file.delete()
        return "操作成功", '数据删除成功'
    else:
        return "操作失败", '数据不存在'


# 查询
def getinfo_func(**kwargs):
    if 'id' not in kwargs:
        return "操作失败", '参数错误'
    file = File.get(id=kwargs['id'])
    if file:
        return "操作成功", file.to_dict()
    else:
        return "操作失败", '数据不存在'


# 分页查询列表
def getlist_func(**kwargs):
    result = File.search(**kwargs)
    return "操作成功", result
