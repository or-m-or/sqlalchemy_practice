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

@router.get("/num5")
def user_address(db: Session = Depends(get_db)):
    _user_address = actual_query.get_user_address(db)
    return _user_address

@router.get("/num6")
def address_sameemail(db: Session = Depends(get_db)):
    _address_sameemail = actual_query.get_address_sameemail(db)
    return _address_sameemail

@router.get("/num7")
def user_selectfrom(db: Session = Depends(get_db)):
    _user_selectfrom = actual_query.get_user_selectfrom(db)
    return _user_selectfrom

@router.get("/num8")
def user_address_join(db: Session = Depends(get_db)):
    _user_address_join = actual_query.get_user_address_join(db)
    return _user_address_join

@router.get("/num8_1")
def user_address_join(db: Session = Depends(get_db)):
    _user_address_join_2 = actual_query.get_user_address_join_2(db)
    return _user_address_join_2



@router.put("/num9")
def foo2foobar(db: Session = Depends(get_db)):
    _foo2foobar = actual_query.put_foo2foobar(db)
    return _foo2foobar

@router.get("/num10")
def user_count(db: Session = Depends(get_db)):
    _user_count = actual_query.get_user_count(db)
    return _user_count
