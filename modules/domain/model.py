from typing import List
from datetime import date
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional, List, Set
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, Float, Boolean,
    ForeignKey
)
from sqlalchemy import create_engine
from modules.repository import db_conn

Base = declarative_base()


class TotalCost(Base):

    __tablename__ = 'total_cost'

    id = Column(Integer, primary_key=True)
    user = Column(String)
    transaction_date = Column(Date)
    cost_center = Column(String)
    total_cost = Column(Float)

    def __init__(
            self, user: str, transaction_date: date,
            cost_center: str, total_cost: float):
        self.user = user
        self.transaction_date = transaction_date
        self.cost_center = cost_center
        self.total_cost = total_cost


engine = create_engine(db_conn.Connection().get_postgres_uri())

Base.metadata.create_all(engine)
