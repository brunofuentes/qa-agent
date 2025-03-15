from typing import List, Optional
from sqlalchemy.orm import Session
from ..models.test_log import TestLog
from ..session import get_db


def create_test_log(
    feature_description: str,
    gherkin_scenario: str = "",
    browser_test: str = "",
    playwright_test: str = "",
    test_result: str = "",
    db: Optional[Session] = None,
) -> TestLog:
    """Create a new test log entry"""
    close_db = False
    if db is None:
        db = get_db()
        close_db = True

    try:
        test_log = TestLog(
            feature_description=feature_description,
            gherkin_scenario=gherkin_scenario,
            browser_test=browser_test,
            playwright_test=playwright_test,
            test_result=test_result,
        )
        db.add(test_log)
        db.commit()
        db.refresh(test_log)
        return test_log
    except Exception as e:
        db.rollback()
        raise e
    finally:
        if close_db:
            db.close()


def get_test_log(log_id: int, db: Optional[Session] = None) -> Optional[TestLog]:
    """Get a test log by ID"""
    close_db = False
    if db is None:
        db = get_db()
        close_db = True

    try:
        return db.query(TestLog).filter(TestLog.id == log_id).first()
    finally:
        if close_db:
            db.close()


def get_all_test_logs(db: Optional[Session] = None) -> List[TestLog]:
    """Get all test logs"""
    close_db = False
    if db is None:
        db = get_db()
        close_db = True

    try:
        return db.query(TestLog).order_by(TestLog.created_at.desc()).all()
    finally:
        if close_db:
            db.close()


def update_test_log(
    log_id: int,
    gherkin_scenario: Optional[str] = None,
    browser_test: Optional[str] = None,
    playwright_test: Optional[str] = None,
    test_result: Optional[str] = None,
    db: Optional[Session] = None,
) -> Optional[TestLog]:
    """Update a test log"""
    close_db = False
    if db is None:
        db = get_db()
        close_db = True

    try:
        test_log = db.query(TestLog).filter(TestLog.id == log_id).first()
        if not test_log:
            return None

        if gherkin_scenario is not None:
            test_log.gherkin_scenario = gherkin_scenario
        if browser_test is not None:
            test_log.browser_test = browser_test
        if playwright_test is not None:
            test_log.playwright_test = playwright_test
        if test_result is not None:
            test_log.test_result = test_result

        db.commit()
        db.refresh(test_log)
        return test_log
    except Exception as e:
        db.rollback()
        raise e
    finally:
        if close_db:
            db.close()


def delete_test_log(log_id: int, db: Optional[Session] = None) -> bool:
    """Delete a test log"""
    close_db = False
    if db is None:
        db = get_db()
        close_db = True

    try:
        test_log = db.query(TestLog).filter(TestLog.id == log_id).first()
        if not test_log:
            return False

        db.delete(test_log)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e
    finally:
        if close_db:
            db.close()
