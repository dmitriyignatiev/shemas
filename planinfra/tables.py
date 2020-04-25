import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData


metadata = MetaData()

association_t = Table('association_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('mainresource_id', Integer, ForeignKey('mainresource.id')),
    Column('contract_id', Integer, ForeignKey('contract.id'))
)


mainresource = Table(
    'mainresource', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
)


contract = Table(
    'contract', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
)



plan = Table(
    'plan', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255), nullable=False),
    Column('contract_id', Integer, ForeignKey('contract.id'))
)


user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255))
)

lessons = Table(
    'lessons', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255)),
    Column('user_id', Integer, ForeignKey('user.id'))
)

teacher = Table(
    'teacher', metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String(255)),
    Column('lesson_id', Integer, ForeignKey('lessons.id'))
)
