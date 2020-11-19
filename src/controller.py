from src.database import adapters


def create_user(user, db):
    ua = adapters.UserAdapter()
    return ua.create_user(db=db, user=user)


def read_users(skip, limit, db):
    ua = adapters.UserAdapter()
    return ua.get_users(db=db, skip=skip, limit=limit)


def read_user(user_id, db):
    ua = adapters.UserAdapter()
    db_user = ua.get_user(db=db, user_id=user_id)
    return db_user
