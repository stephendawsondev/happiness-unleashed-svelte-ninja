from ninja import NinjaAPI
from happiness_app.api import router as happiness_app_router

api = NinjaAPI()

api.add_router('/', happiness_app_router)
