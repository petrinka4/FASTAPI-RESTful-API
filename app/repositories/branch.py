from app.repositories.base import BaseRepository
from app.models.branch import branchModel

from sqlalchemy.orm import DeclarativeMeta


class BranchRepository(BaseRepository):
    Model: DeclarativeMeta = branchModel
