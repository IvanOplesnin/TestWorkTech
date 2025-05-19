from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, MappedColumn, DeclarativeBase, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.models import Base

if TYPE_CHECKING:
    from backend.models import TimeProject, User


class Project(Base):
    __tablename__ = 'projects'

    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    time_users: Mapped[list["TimeProject"]] = relationship(back_populates='project')
