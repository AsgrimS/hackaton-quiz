from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

from quiz.api import quiz_api

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("", quiz_api)
