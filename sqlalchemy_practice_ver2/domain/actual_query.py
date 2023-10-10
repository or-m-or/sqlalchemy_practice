from models import User, Address
from sqlalchemy.orm import Session, joinedload, contains_eager
from sqlalchemy import text, create_engine, select, update, func


# 1
def get_user_id42(db: Session):
    _user_id42 = db.get(User, 1)
    return _user_id42


# 2. 
def get_user_all(db: Session):
    _user_all = db.execute(
                  select(User)
                  ).scalars().all()
    # or
    # _user_all = db.scalars(
    #                 select(User)
    #                 ).all()
    return _user_all


# 3.
def get_oneuser_name(db: Session):
    _oneuser_name = db.execute(
                        select(User).filter_by(name="sample1")
                        ).scalar_one()
    return _oneuser_name


# 4. 결과가 없으면 None을 반환.
def get_firstuser_name(db: Session):
    _firstuser_name = db.scalars(
                        select(User).\
                        filter_by(name="sample3")
                        #.limit(1)
                        ).first()
    return _firstuser_name


# 5. 
def get_user_address(db: Session):
    _user_address = db.scalars(
        select(User).\
        options(joinedload(User.address))).unique().all()
    return _user_address


# 6. 
def get_address_sameemail(db: Session):
    _address_sameemail = db.execute(
    select(User).
    join(Address).
    # filter(Address.email.like('%@rbrain.co.kr'))
    where(Address.email.like('%@rbrain.co.kr'))
    ).scalars().all()
    return _address_sameemail

# 7.
def get_user_selectfrom(db: Session):
    _user_selectfrom = db.scalars(
    select(User).
    from_statement(
    text("select * from user")
    )
    ).all()
    return _user_selectfrom


# 8. 
def get_user_address_join(db: Session):
    _user_address_join = db.execute(
        select(User).
        join(User.address).
        options(contains_eager(User.address)).
        execution_options(populate_existing=True)
    ).scalars().unique().all()   # .unique()
    return _user_address_join

# 9.
def put_foo2foobar(db: Session):
    _foo2foobar = db.execute(
    update(User).
    where(User.name == 'sample6').
    values(age=28).
    execution_options(synchronize_session="evaluate")
    )
    # db.commit()
    return _foo2foobar

# 10. 데이터베이스에서 User 테이블의 레코드 수를 가져와서 반환
def get_user_count(db: Session):
    # _user_count = db.scalar(select(func.count()).select_from(User))
    _user_count = db.scalar(select(func.count(User.id)))
    return _user_count