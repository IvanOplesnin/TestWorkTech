from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.models import Base

if TYPE_CHECKING:
    from backend.models.time_project import TimeProject


class User(Base):
    __tablename__ = 'users'

    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    manager: Mapped[bool] = mapped_column(default=False)
    hash_password: Mapped[str] = mapped_column(nullable=False)

    project_times: Mapped[list["TimeProject"]] = relationship(back_populates='user')
