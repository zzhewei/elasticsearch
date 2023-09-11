from flask import Blueprint
from flask_restx import Api

from .search.views import Search

v1 = Blueprint("v1", __name__, url_prefix="/API")
api = Api(
    v1,
    version="1.0",
    title="Search Engine API",
    description="Just API",
)

api.add_namespace(Search)
