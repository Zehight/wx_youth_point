from run import db
from sqlalchemy import or_
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
        print('aaaa')
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        db.session.commit()
        return self


    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
        db.session.close()

    @classmethod
    def get(cls, **kwargs):
        query = cls.query
        result = query.filter_by(**kwargs).first()
        query.session.close()
        return result

    @classmethod
    def get_all(cls, **kwargs):
        query = cls.query
        result = query.filter_by(**kwargs).all()
        query.session.close()
        return result

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def filter(cls, *criterion):
        return cls.query.filter(*criterion)

    @classmethod
    def all(cls):
        return cls.query.all()

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    @classmethod
    def search(cls, keyword = '',page=None, rows=None,**kwargs):
        query = cls.query
        if hasattr(cls, 'search_fields') and keyword:
            query = query.filter(or_(*[getattr(cls, field).ilike(f'%{keyword}%') for field in cls.search_fields]))
        query = query.filter_by(**kwargs).order_by(cls.create_time.desc())
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