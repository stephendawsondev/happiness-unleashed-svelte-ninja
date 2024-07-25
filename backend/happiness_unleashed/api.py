from ninja import NinjaAPI
from acts_of_kindness.api import router as happiness_app_router
from post.api import router as posts_router

api = NinjaAPI()

api.add_router('/', happiness_app_router)
api.add_router('/', posts_router)
