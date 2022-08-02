"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import ProvenancedResource


PROVENANCED_BLUEPRINT = Blueprint('provenanced', __name__)
Api(PROVENANCED_BLUEPRINT).add_resource(ProvenancedResource, '/provenanced/<string:action>')