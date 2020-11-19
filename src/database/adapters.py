from sqlalchemy.orm import Session

from src.database import models, schemas


class UserAdapter:
    def create_user(self, db: Session, user: schemas.UserCreate):
        existing_user = self.get_user_by_email(db, email=user.email)
        if existing_user:
            raise Exception("User already Exists")
        fake_hashed_password = user.password + "hash"
        to_create_user = models.User(
            email=user.email, hashed_password=fake_hashed_password
        )
        db.add(to_create_user)
        db.commit()
        db.refresh(to_create_user)
        return to_create_user

    def get_user(self, db: Session, user_id: int):
        user = db.query(models.User).filter(models.User.id == user_id).first()
        if user is None:
            raise Exception("User not found")
        return user

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()
