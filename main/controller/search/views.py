from flask import abort, current_app, request
from flask_restx import Resource

from main import es

from . import SearchInit

Search = SearchInit.search


@Search.route("/Search")
class SearchOpe(Resource):
    SearchSer = SearchInit.Data

    @Search.marshal_list_with(SearchSer)
    def get(self):
        """取得資料"""
        try:
            search_data = {"match_all": {}}

            # search_data = {"match": {"lastname": "vv"}}

            # 要有75%符合的查詢
            # search_data = {"match": {
            #     "lastname": {
            #         "query": "rap",
            #         "minimum_should_match": "75%"
            #     }
            # }}

            # 多欄位的多條件查詢
            # search_data = {"multi_match": {"query": "rap 吳", "fields": ["lastname", "firstname"]}}
            # reference: https://hackmd.io/@tienyulin?tags=%5B%22Elasticsearch%22%5D

            return_data = es.search(index="customer", query=search_data)
            result = []
            for i in return_data["hits"]["hits"]:
                d = dict()
                d["id"] = i["_id"]
                d["firstname"] = i["_source"]["firstname"] if "firstname" in i["_source"] else None
                d["lastname"] = i["_source"]["lastname"] if "lastname" in i["_source"] else None
                d["test"] = i["_source"]["test"] if "test" in i["_source"] else None
                result.append(d)

            return result
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Search.expect(SearchSer)
    @Search.marshal_with(SearchSer, code=201)
    def post(self):
        """新增資料"""
        try:
            single_data = request.get_json()
            return_data = es.index(index="customer", document=single_data)
            single_data["id"] = return_data["_id"]
            # es.index(index="customer", document=single_data, id=1)  # 指定id
            return single_data
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))


@Search.route("/Search/<string:sid>")
class SearchOpe(Resource):
    SearchSer = SearchInit.Data

    def get(self, sid):
        """新增、更新和刪除多筆 for 測試"""
        try:
            insert_data = [
                {"create": {"_index": "customer"}},
                {"doc": {"firstname": "tea", "lastname": "nice"}},
                {"create": {"_index": "customer", "_id": 3}},
                {"doc": {"firstname": "track", "lastname": "cc"}},
                {"update": {"_index": "customer", "_id": 1}},
                {"doc": {"firstname": "Tom", "lastname": "xx rap"}},
                {"delete": {"_index": "customer", "_id": 2}},
            ]
            return_data = es.bulk(body=insert_data)
            print(return_data)
            return {"Success": True}
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    @Search.expect(SearchSer)
    @Search.marshal_with(SearchSer)
    def put(self, sid):
        """更新資料"""
        try:
            single_data = request.get_json()
            return_data = es.index(index="customer", document=single_data, id=sid)
            single_data["id"] = return_data["_id"]
            return single_data
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))

    def delete(self, sid):
        """刪除資料"""
        try:
            es.delete(index="customer", id=sid)
            return "", 204
        except Exception as e:
            current_app.logger.error(e)
            abort(400, str(e))
