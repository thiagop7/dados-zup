from typing import Optional
from datetime import date

from modules.domain import model
from modules.domain.model import TotalCost
from modules.repository import unit_of_work


def add_total_cost(
        user: str, transaction_date: date,
        cost_center: str, total_cost: float,
        uow: unit_of_work.AbstractUnitOfWork
):
    with uow:
        uow.totalCosts.add(model.TotalCost(
            user, transaction_date, cost_center, total_cost))
        uow.commit()
