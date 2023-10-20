import uuid
from datetime import datetime
from service.default_dao import CRUDMixin
from run import db

class User(db.Model, CRUDMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    user_name = db.Column(db.String(50))
    nike_name = db.Column(db.String(50))
    pwd = db.Column(db.String(255))
    phone = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True,nullable = False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_ip = db.Column(db.String(255))
    search_fields = ['real_name','nike_name', 'phone','email']

class WxLogin(db.Model, CRUDMixin):
    __tablename__ = 'wxlogin'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    open_id = db.Column(db.String(50))
    user_id = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())

class Activity(db.Model,CRUDMixin):
    __tablename__ = 'activity'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    name = db.Column(db.String(255), nullable=False)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    remark = db.Column(db.String(255))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['title', 'content','create_by']

class File(db.Model,CRUDMixin):
    __tablename__ = 'file'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    status = db.Column(db.String(1), nullable=False, default="0")  # 删除为1，不删除为0
    file_name = db.Column(db.String(100), nullable=False)
    small_type = db.Column(db.String(1), nullable=False, default="0") #0:原图  1：缩放后的图
    small_id = db.Column(db.String(50))
    create_by = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    search_fields = ['file_name']

class Round(db.Model,CRUDMixin):
    __tablename__ = 'round'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    activity_id = db.Column(db.String(50))
    name = db.Column(db.String(50))
    show_time = db.Column(db.DateTime)
    start_vote_time = db.Column(db.DateTime)
    end_vote_time = db.Column(db.DateTime)
    freeze_type = db.Column(db.String(1),default="0")
    remark = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)

class Group(db.Model,CRUDMixin):
    __tablename__ = 'group'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    round_id = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    vote_num = db.Column(db.Integer(), nullable=False)
    promoted_num = db.Column(db.Integer(), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)

class Role(db.Model,CRUDMixin):
    __tablename__ = 'role'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    name = db.Column(db.String(255), nullable=False)
    zone = db.Column(db.String(1)) # 赛区
    code = db.Column(db.String(50)) # 编码
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)
    search_fields = ['name']

class GroupRoleRelation(db.Model,CRUDMixin):
    __tablename__ = 'group_role_relation'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    group_id = db.Column(db.String(255))
    role_id = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)


class RoleFileRelation(db.Model,CRUDMixin):
    __tablename__ = 'role_file_relation'
    id = db.Column(db.String(50), primary_key=True,default=lambda: str(uuid.uuid4()).replace("-",""))
    role_id = db.Column(db.String(50))
    file_id = db.Column(db.String(50))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)

class RoleHistaryRelation(db.Model,CRUDMixin):
    __tablename__ = 'role_histary_relation'
    id = db.Column(db.String(255), primary_key=True)
    role_id = db.Column(db.String(50))
    title = db.Column(db.String(50))
    remark = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)


class voteLog(db.Model,CRUDMixin):
    __tablename__ = 'vote_log'
    id = db.Column(db.String(255), primary_key=True)
    role_id = db.Column(db.String(50))
    user_id = db.Column(db.String(50))
    remark = db.Column(db.String(255))
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)

class borrow_book_log(db.Model,CRUDMixin):
    __tablename__ = 'borrow_book_log'
    id = db.Column(db.String(50), primary_key=True, default=lambda: str(uuid.uuid4()).replace("-", ""))
    name = db.Column(db.String(50))
    borrow_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now())
    create_by = db.Column(db.String(255), nullable=False)

db.create_all()
