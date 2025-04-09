from fastapi import APIRouter

from app.routers.account import router_account
from app.routers.bank import router_bank
from app.routers.city import router_city
from app.routers.branch import router_branch
from app.routers.status import router_status
from app.routers.client import router_client
from app.routers.card import router_card
from app.routers.user import router_user

#test
from app.auth.routers import router as router_auth

api=APIRouter()

api.include_router(router_user)
api.include_router(router_bank)
api.include_router(router_city)
api.include_router(router_branch)
api.include_router(router_status)
api.include_router(router_client)
api.include_router(router_account)
api.include_router(router_card)
api.include_router(router_auth)
