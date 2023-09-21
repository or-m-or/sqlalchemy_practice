from models import User, Address
from sqlalchemy.orm import Session, joinedload, contains_eager
from sqlalchemy import text, create_engine, select, update, func


# # test query
# def get_user_list(db: Session):
#     _user_list = db.query(User)\
#     .order_by(User.id.desc())\
#     .all()
#     return _user_list

# 1. User 테이블에서 ID가 42인 사용자를 가져와서, 해당 사용자 객체를 반환
def get_user_id42(db: Session):
    _user_id42 = db.get(User, 42)
    return _user_id42


# 2. User 테이블의 모든 레코드를 가져와서 리스트로 반환
def get_user_all(db: Session):
    # _user_all = db.execute(
    # select(User)
    # ).scalars().all()
    # or
    _user_all = db.scalars(select(User)).all()
    return _user_all


# 3. User 테이블에서 'name'='some user'인 단일 사용자 레코드를 가져와서 반환 (하나여야만 함) 
#    같은 이름이 둘이면 에러 발생함. (sqlalchemy.exc.MultipleResultsFound: Multiple rows were found when exactly one was required)
def get_oneuser_name(db: Session):
    _oneuser_name = db.execute(
    select(User).
    filter_by(name="some user")
 ).scalar_one()
    return _oneuser_name


# 4. User 테이블에서 'name'='some user'인 첫 번째 사용자 레코드를 가져와서 반환하며, 결과가 없으면 None을 반환.
def get_firstuser_name(db: Session):
    _firstuser_name = db.scalars(
    select(User).
    filter_by(name="some user").
    limit(1)
    ).first()
    return _firstuser_name


# 5. User 테이블의 모든 레코드를 가져오면서 각 User 레코드와 관련된 addresses 속성을 미리 로드하여 리스트로 반환 - 한번더 체크필요
def get_user_address(db: Session):
    _user_address = db.scalars(
    select(User).
    options(
    joinedload(User.address)
    )
    ).unique().all()
    return _user_address


# 6. User와 Address 테이블을 조인하고, Address 테이블의 이메일 주소가 'e@sa.us'인 사용자 정보를 검색
def get_address_sameemail(db: Session):
    _address_sameemail = db.execute(
    select(User).
    join(Address).
    where(Address.email == 'e@sa.us')
    ).scalars().all()
    return _address_sameemail

# 7. 데이터베이스에서 "select * from users" SQL 쿼리를 실행하여 모든 User 레코드를 가져와서 리스트로 반환
def get_user_selectfrom(db: Session):
    _user_selectfrom = db.scalars(
    select(User).
    from_statement(
    text("select * from user")
    )
    ).all()
    return _user_selectfrom


# 8. 데이터베이스에서 User와 관련된 Address 레코드를 조인하고, 
# User 객체에 연결된 address 관계를 미리 로드하여 
# 이미 로드된 데이터를 사용하여 모든 User 레코드를 가져와서 리스트로 반환
def get_user_address_join(db: Session):
    _user_address_join = db.execute(
        select(User).
        join(User.address).
        options(contains_eager(User.address)).
        execution_options(populate_existing=True)
    ).scalars().unique().all()   # .unique()
    return _user_address_join

# 9. 데이터베이스에서 name이 'foo'인 모든 User 레코드의 fullname을 "Foo Bar"로 업데이트하고, 세션의 상태를 업데이트
# synchronize_session="evaluate" 옵션은 세션 내부 상태를 업데이트하는 방식을 지정하는 것으로, 
# "evaluate" 옵션은 세션 내부 상태를 업데이트하지만 데이터베이스에는 아직 커밋하지 않음을 의미합니다.
# 즉, 이 쿼리문은 User 테이블에서 name이 'foo'인 레코드의 fullname 값을 "Foo Bar"로 변경하는 작업을 수행하며, 
# 이 변경 사항은 세션 내부에 적용되고, 나중에 커밋할 수 있도록 준비됩니다. 커밋을 수행하면 데이터베이스에 변경 사항이 적용됩니다.
def put_foo2foobar(db: Session):
    _foo2foobar = db.execute(
    update(User).
    where(User.name == 'foo').
    values(fullname="Foo Bar").
    execution_options(synchronize_session="evaluate")
    )
    # db.commit()
    return _foo2foobar

# 10. 데이터베이스에서 User 테이블의 레코드 수를 가져와서 반환
def get_user_count(db: Session):
    _user_count = db.scalar(select(func.count()).select_from(User))
    # _user_count = db.scalar(select(func.count(User.id)))
    return _user_count