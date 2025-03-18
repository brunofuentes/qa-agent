from sqlalchemy import String, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from ..base import Base


class TestLog(Base):
    __tablename__ = "test_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    feature_description: Mapped[str] = mapped_column(String, nullable=False)
    gherkin_scenario: Mapped[str] = mapped_column(Text, nullable=False)
    browser_test: Mapped[str] = mapped_column(Text, nullable=False)
    playwright_test: Mapped[str] = mapped_column(Text, nullable=False)
    test_result: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.UTC)
    )
    ai_model: Mapped[str] = mapped_column(String, nullable=True)
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        onupdate=lambda: datetime.datetime.now(datetime.UTC),
        default=lambda: datetime.datetime.now(datetime.UTC),
    )

    def __repr__(self) -> str:
        return f"<TestLog(id={self.id}, feature='{self.feature_description[:20]}...', result='{self.test_result[:20]}...')>"  # noqa: E501
