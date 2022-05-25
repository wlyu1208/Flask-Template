from flask import current_app

from flask_restx import Resource, Namespace

Template = Namespace('Template')

@Template.route('/<string:string_input>')
class TemplateClass(Resource):
    @Template.response(200, "Successfully Returned Input String")
    @Template.response(500, "Internal Server Error")
    def get(self, string_input):
        current_app.logger.info(f"{string_input} is returned sucessfully")
        return string_input, 200