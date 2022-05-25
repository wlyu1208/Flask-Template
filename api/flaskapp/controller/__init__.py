from flask import Blueprint

from flask_restx import Api

Entry = Blueprint('Entry', __name__, url_prefix='/')

def create_endpoints(app):
    api = Api(Entry,
        version='0.1',
        title="Flask Template",
        description="Template for Flask API Server",
        terms_url="/terms",
        contact="wlyu125@gmail.com"
    )

    @Entry.route('/hello')
    def hello():
        return 'This is Flask Template'
    
    from .TemplateController import Template

    api.add_namespace(Template, '/template')

    app.register_blueprint(Entry)