from uuid import UUID

from fastapi import APIRouter, status

from settlements.database import DbSession
from settlements.users.schemas import UserCreate, UserRead, UserUpdate
from settlements.users.services import user_services


router = APIRouter()


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(db: DbSession, user: UserCreate):
    return await user_services.create(db, user)


@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def read_user(db: DbSession, user_id: UUID):
    return await user_services.get(db, user_id)


@router.patch("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def update_user(db: DbSession, user_id: UUID, user: UserUpdate):
    return await user_services.update(db, user_id, user)


@router.delete("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
async def delete_user(db: DbSession, user_id: UUID):
    return await user_services.delete(db, user_id)