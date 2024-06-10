#!/usr/bin/python3
""" """

from flask import jsonify, requests
from models.state import User
from models import storage
from api.v.views import app_views


@app_views.route("/users", strict_slashes=False)
def get_status():
    """ """
    users = storage.all(User).values()

    lists = []

    for user in users:
        lists.append(user.to_dict())

    return jsonify(lists)


@app_views.route("/users/<user_id>", strict_slashes=False)
def get_city(user_id):
    """ """

    user = storage.get(User, user_id)

    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)


@app_views.route("/users/<user_id>", methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ """

    user = storage.get(User, user_id)

    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route("/users", methods=['POST'], strict_slashes=False)
def add_user(user_id):
    """ """
    if request.content_type != 'application/json':
        abort(404, 'Not a JSON')
    if not request.get_json():
        abort(404, 'Not a JSON')
    kwargs = request.get_json()

    if 'name' not in kwargs:
        abort(404, 'Missing name')

    user = User(**kwargs)
    user.save()
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ """
    if request.content_type != 'application/json':
        abort(404, 'Not a JSON')
    user = request.get(User, user_id)

    if user:
        if not request.get_json():
            abort(404, 'Not a JSON')
        data = request.get_json()
        ignore_keys = ['id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(user, key, value)
        user.save()
        return jsonify(user.to_dict())
    else:
        abort(404)
