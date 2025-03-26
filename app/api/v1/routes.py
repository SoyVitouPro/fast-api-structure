from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.crud.user import (
    create_user, get_users, get_user, update_user, delete_user,
)
from app.db.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)


@router.get("/", response_model=list[UserRead])
async def read_all(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


@router.get("/{user_id}", response_model=UserRead)
async def read(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
async def update(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    existing = await get_user(db, user_id)
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    return await update_user(db, user_id, user)


@router.delete("/{user_id}")
async def delete(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(db, user_id)
    return {"detail": "User deleted"}
