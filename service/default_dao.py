import uuid

from sqlalchemy.exc import SQLAlchemyError

from run import db
from sqlalchemy import or_, and_
from datetime import datetime
import logging

class CRUDMixin:
    def __init__(self):
        self.__mapper__ = None

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            value = getattr(self, key)
            if isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            result[key] = value
        return result

    @classmethod
    def create(cls, **kwargs):
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid.uuid4()).replace("-", "")
        instance = cls(**kwargs)
        instance.save()
        return {'id':kwargs['id']}

    @classmethod
    def createByAuto(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return {'data':'ok'}

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        if commit:
            self.save()
        return self


    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            try:
                db.session.commit()
            except SQLAlchemyError:
                db.session.rollback()
                raise

    @classmethod
    def get(cls, **kwargs):
        query = cls.query
        result = query.filter_by(**kwargs).first()
        query.session.close()
        return result

    @classmethod
    def query(cls):
        return cls.query

    @classmethod
    def get_all(cls, **kwargs):
        query = cls.query
        result = query.filter_by(**kwargs).all()
        query.session.close()
        return result

    @classmethod
    def count(cls,**kwargs):
        query = cls.query
        result = query.filter_by(**kwargs).count()
        query.session.close()
        return result

    @classmethod
    def filter(cls, *criterion):
        return cls.query.filter(*criterion)

    @classmethod
    def all(cls):
        return cls.query.all()

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except SQLAlchemyError:
                db.session.rollback()
                raise
        return self

    @classmethod
    def search(cls, keyword = '',page=None, rows=None,order_method='desc',**kwargs):
        start_time = '2022-01-01 23:59:59'
        end_time = '2100-01-01 23:59:59'
        if 'start_time' in kwargs:
            start_time = kwargs['start_time']
            del kwargs['start_time']
        if 'end_time' in kwargs:
            end_time = kwargs['end_time']
            del kwargs['end_time']
        query = cls.query
        if hasattr(cls, 'search_fields') and keyword:
            query = query.filter(or_(*[getattr(cls, field).ilike(f'%{keyword}%') for field in cls.search_fields]))
        if order_method == 'desc':
            query = query.filter(and_(cls.create_time.between(start_time, end_time), *[getattr(cls, key) == value for key, value in kwargs.items()])).order_by(cls.create_time.desc())
        else:
            query = query.filter(and_(cls.create_time.between(start_time, end_time), *[getattr(cls, key) == value for key, value in kwargs.items()])).order_by(cls.create_time)
        total = query.count()
        if page is None or rows is None:
            page=1
            rows=10
            items = query.all()
            result = [item.to_dict() for item in items]
        else:
            page = int(page)
            rows = int(rows)
            items = query.paginate(page, rows, error_out=False)
            result = [item.to_dict() for item in items.items]
        query.session.close()
        return {
            'page': page,
            'rows': rows,
            'total': total,
            'list': result
        }

