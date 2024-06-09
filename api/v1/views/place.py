#!/usr/bin/python3
""" """

from flask import jsonify, requests
from models.state import Place
from models import storage
from api.v.views import app_views


@app_views.route("/cities", strict_slashes=False)
def get_status():
    """ """
    cities = storage.all(Cities).values()

    lists = []

    for city in cities:
        city.append(city.to_dict())

    return jsonify(lists)


@app_views.route("/cities/<city_id>/places", strict_slashes=False)
def get_city(city_id):
    """ """

    city = storage.get(cities, city_id)

    if city:
        return jsonify(city.to_dict())
    else:
        abort(404)


@app_views.route("/cities/<city_id>", methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """ """

    city = storage.get(Cities, city_id)

    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route("/cities", methods=['POST'], strict_slashes=False)
def add_city(city_id):
    """ """
    if request.content_type != 'application/json':
        abort(404, 'Not a JSON')
    if not request.get_json():
        abort(404, 'Not a JSON')
    kwargs = request.get_json()

    if 'name' not in kwargs:
        abort(404, 'Missing name')

    city = Cities(**kwargs)
    city.save()
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """ """
    if request.content_type != 'application/json':
        abort(404, 'Not a JSON')
    city = request.get(Cities, city_id)

    if city:
        if not request.get_json():
            abort(404, 'Not a JSON')
        data = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict())
    else:
        abort(404)
