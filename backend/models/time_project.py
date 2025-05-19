import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.models import Base

if TYPE_CHECKING:
    from backend.models.project import Project
    from backend.models.user import User


class TimeProject(Base):
    __tablename__ = 'project_times'

    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id', ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete="CASCADE"))
    date: Mapped[datetime.date] = mapped_column(default=datetime.date.today, nullable=False)
    hours: Mapped[int] = mapped_column(nullable=False)

    project: Mapped['Project'] = relationship(back_populates="time_users")
    user: Mapped['User'] = relationship(back_populates='project_times')
