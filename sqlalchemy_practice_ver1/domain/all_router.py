from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from database import get_db
from models import User, Address
from domain import actual_query
from sqlalchemy import text


router = APIRouter(
    prefix="/api/user",
)

# # 작성한 get_question_list 함수를 사용할 수 있도록 질문 목록 라우터 함수를 수정
# @router.get("/list")
# def user_list(db: Session = Depends(get_db)):
#     _user_list = actual_query.get_user_list(db)
#     return _user_list


# # Fastapi의 Depends를 사용, 더 간단하게 표현가능
# @router.get("/list")
# def user_list(db: Session = Depends(get_db)):
#     _user_list = db.query(User).order_by(User.id.desc()).all()
#     return _user_list


# # database.py에 의존성 주입, database.py의 get_db함수 사용
# @router.get("/list")
# def user_list():
#     with get_db() as db:
#         _user_list = db.query(User).order_by(User.id.desc()).all()
#     return _user_list


# # Original 버전 코드
# @router.get("/list")
# def user_list():
#     db = SessionLocal()
#     _user_list = db.query(User).order_by(User.id.desc()).all()
#     db.close() # 세션을 커넥션 풀에 반환
#     return _user_list

# @router.get("/num1")
# def user_id42(db: Session = Depends(get_db)):
#     _user_id42 = actual_query.get_user_id42(db)
#     return _user_id42

# @router.get("/num2")
# def user_all(db: Session = Depends(get_db)):
#     _user_all = actual_query.get_user_all(db)
#     return _user_all

# @router.get("/num3")
# def oneuser_name(db: Session = Depends(get_db)):
#     _oneuser_name = actual_query.get_oneuser_name(db)
#     return _oneuser_name

# @router.get("/num4")
# def firstuser_name(db: Session = Depends(get_db)):
#     _firstuser_name = actual_query.get_oneuser_name(db)
#     return _firstuser_name

# 6번
@router.get("/join_test")
def join_test(db: Session = Depends(get_db)):
    _join_test = actual_query.get_join_test(db)
    return _join_test

# 5번
@router.get("/joinedload_test")
def joinedload_test(db: Session = Depends(get_db)):
    _joinedload_test = actual_query.get_joinedload_test(db)
    return _joinedload_test

# 8-1번
@router.get("/contains_eager_test")
def contains_eager_test(db: Session = Depends(get_db)):
    _contains_eager_test = actual_query.get_contains_eager_test(db)
    return _contains_eager_test

# 8-2번
@router.get("/populate_existing_test")
def populate_existing_test(db: Session = Depends(get_db)):
    _populate_existing_test = actual_query.get_populate_existing_test(db)
    
    # db 수정 쿼리 실행
    actual_query.add_address(db)
    
    return _populate_existing_test

# 9번
@router.put("/synchronize_session_test")
def synchronize_Session_test(db: Session = Depends(get_db)):
    _synchronize_Session_test = actual_query.put_synchronize_Session_test(db)
    return _synchronize_Session_test

# 7번
@router.get("/from_statement_test")
def from_statement_test(db: Session = Depends(get_db)):
    _from_statement_test = actual_query.get_from_statement_test(db)
    return _from_statement_test

# 10번
@router.get("/count_test")
def count_test(db: Session = Depends(get_db)):
    _count_test = actual_query.get_count_test(db)
    return _count_test
