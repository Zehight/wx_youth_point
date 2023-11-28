import uuid
from datetime import datetime
from service.default_dao import CRUDMixin
from run import db

class Dept(db.Model,CRUDMixin):
    __tablename__ = 'dept'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    name = db.Column(db.String(50))
    cover_id = db.Column(db.String(50))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class User(db.Model, CRUDMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    real_name = db.Column(db.String(50))
    user_code = db.Column(db.String(50))
    nike_name = db.Column(db.String(50))
    dept_id = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    email = db.Column(db.String(50))
    permission = db.Column(db.String(50),default='user')
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['real_name','nike_name', 'phone','email','user_code']

class Binding(db.Model, CRUDMixin):
    __tablename__ = 'binding'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    open_id = db.Column(db.String(50))
    user_id = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class File(db.Model,CRUDMixin):
    __tablename__ = 'file'
    id = db.Column(db.String(100), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    status = db.Column(db.String(1), nullable=False, default="0")  # 删除为1，不删除为0
    file_name = db.Column(db.String(100), nullable=False)
    small_type = db.Column(db.String(1), nullable=False, default="0") #0:原图  1：缩放后的图
    small_id = db.Column(db.String(50))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['file_name']

class Activity(db.Model,CRUDMixin):
    __tablename__ = 'activity'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    dept_id = db.Column(db.String(50),default="000000")
    block = db.Column(db.String(255),default="活动")
    author = db.Column(db.String(255),default="共青团中央")
    type = db.Column(db.String(255),default='活动')
    activity_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    carousel = db.Column(db.String(1),default='1') #是否轮播
    create_by = db.Column(db.String(50), nullable=False)
    update_by = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    update_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['title','content']

class ActivityFileRela(db.Model,CRUDMixin):
    __tablename__ = 'activity_file_rela'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    activity_id = db.Column(db.String(50))
    file_id = db.Column(db.String(100))
    type = db.Column(db.String(1),default="0") # 0为活动中文件  1为活动中封面
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class Focus(db.Model,CRUDMixin):
    __tablename__ = 'focus'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    activity_id = db.Column(db.String(50))
    type = db.Column(db.String(1), nullable=True)  # 查看为0，点赞为1，收藏为2
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class Borrow(db.Model,CRUDMixin):
    __tablename__ = 'borrow'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    book_name = db.Column(db.String(50))
    type = db.Column(db.String(1), nullable=True, default='0')  # 借书为0，还书为1
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    return_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())



class Question(db.Model,CRUDMixin):
    __tablename__ = 'question'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    input_dept_name = db.Column(db.String(50))
    age = db.Column(db.Integer())
    question_one = db.Column(db.Text())
    question_two = db.Column(db.Text())
    question_three = db.Column(db.Text())
    question_four = db.Column(db.Text())
    question_five = db.Column(db.Text())
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())


class Learn(db.Model,CRUDMixin):
    __tablename__ = 'learn'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    block = db.Column(db.String(255))
    author = db.Column(db.String(255))
    learn_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class Action(db.Model,CRUDMixin):
    __tablename__ = 'action'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    article_id = db.Column(db.String(255))
    type = db.Column(db.String(1), nullable=True, default='0')  # 查看为0，收藏为1，点赞为2
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class Comment(db.Model,CRUDMixin):
    __tablename__ = 'comment'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    activity_id = db.Column(db.String(255))
    reply_id = db.Column(db.String(255))
    content = db.Column(db.String(255))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())


db.create_all()
