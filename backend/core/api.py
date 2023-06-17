from ninja_extra import NinjaExtraAPI, Router
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("", quiz_api)
