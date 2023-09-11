from flask_restx import Namespace, fields


class SearchInit:
    search = Namespace("Search", path="/", description="Search")

    Data = search.model(
        "Data",
        {
            "id": fields.String(readonly=True),
            "firstname": fields.String(),
            "lastname": fields.String,
            "test": fields.Boolean,
        },
    )
