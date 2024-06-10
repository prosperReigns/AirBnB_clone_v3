#!/usr/bin/python3
""" """

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def show_status():
    """ """
    return jsonify({'status': 'OK'})

@app_views.route('/api/v1/stats')
def get_stat():
    stats = {
            'amenities':storage.count('Amenities'),
            'cities':storage.count('Cities'),
            'state':storage.count('State'),
            'review':storage.count('Reviews'),
            'place':storage.count('Place'),
            'users':storage.count('Users')}

    return jsonify(stats)
    
