from flask import Flask, jsonify, make_response, request
from flask_restful import abort, Api, Resource
from exts import db
import config
import pymysql
from models import GSM, GSE
from utils.commons import ReConverter
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)

api = Api(app)

db.init_app(app)

# 为flask添加自定义的转化器
app.url_map.converters['re'] = ReConverter


class GSESchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = GSE
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    GSE_num = fields.String(required=True)
    Status = fields.String(required=True)
    Title = fields.String(required=True)
    Organism = fields.String(required=True)
    Experiment_type = fields.String(required=True)
    Summary = fields.String(required=True)
    Overall_design = fields.String(required=True)
    Platforms = fields.String(required=True)
    Samples = fields.String(required=True)


class GSMSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = GSM
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    GSM_num = fields.String(required=True)
    Status = fields.String(required=True)
    Source_name = fields.String(required=True)
    Organism = fields.String(required=True)
    Characteristics = fields.String(required=True)
    Extracted_molecule = fields.String(required=True)
    Platform = fields.String(required=True)
    GSE_num = fields.String(required=True)
    Experiment_type = fields.String(required=True)


class GSEall(Resource):
    def get(self):
        page = int(request.args.get('page', 1))
        get_gses = GSE.query.filter()
        gses_page = get_gses.paginate(page=page, per_page=10)
        print(type(gses_page))
        gse_schema = GSESchema(many=True)
        gses = gse_schema.dump(gses_page.items)
        return make_response(jsonify({"GSEs": gses}))



class GSESingle(Resource):
    def get(self, gse_num):
        get_gse = GSE.query.filter(GSE.GSE_num == gse_num)
        print(type(get_gse))
        gse_schema = GSESchema(many=True)
        gse_one = gse_schema.dump(get_gse)
        return make_response(jsonify({"GSE": gse_one}))

    # def get(self, title):
    #     get_gse = GSE.query.filter(GSE.Title.like("%" + title + "%") if title is not None else "")
    #     gse_schema = GSESchema(many=True)
    #     gse_some = gse_schema.dump(get_gse)
    #
    #     return make_response(jsonify({"GSEs": gse_some}))


class GSMall(Resource):
    def get(self):
        get_gsms = GSM.query.all()
        gsm_schema = GSMSchema(many=True)
        gsms = gsm_schema.dump(get_gsms)
        return make_response(jsonify({"GSMs": gsms}))


api.add_resource(GSEall, '/gse')
api.add_resource(GSESingle, '/gse/<gse_num>')
# api.add_resource(GSESingle, '/gse/<title>')
api.add_resource(GSMall, '/gsm')


if __name__ == '__main__':
    app.run()
