from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, Float,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.orm import sessionmaker

from modules.domain import model

metadata = MetaData()

total_cost = Table(
    'total_cost', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user', String(255)),
    Column('transaction_date', Date),
    Column('cost_center', String(255)),
    Column('total_cost', Float)
)

def start_mappers():
    mapper(model.TotalCost, total_cost)    
