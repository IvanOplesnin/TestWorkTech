from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.testing.schema import mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
