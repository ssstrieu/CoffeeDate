#comment out imports before integrating with rest of app
import requests
# from flask import Flask, jsonify, render_template, request

API_KEY='AIzaSyAPyQ4vH8xfcrDI5lQ1DiTkaMvL-LP8_KU'
def get_distance(location1,location2):
    url='https://maps.googleapis.com/maps/api/distancematrix/json?'
    url+='origins={}&destinations={}'.format(location1,location2)
    print 'get distance ',url
    request=requests.get(url)
    result=request.json()['rows'][0]['elements'][0]['distance']['text']
    print 'distance', result
    return result
    
# get_d= get_distance('ontario','40.7127837, -74.0059413')
# print 'get_d', get_d


def get_longlat(place):
    url='https://maps.googleapis.com/maps/api/geocode/json?'
    url+='address={}&key={}'.format(place,API_KEY)
    print url
    request=requests.get(url)
    #check if valid place before query googlemaps
    assert len(request.json()['results'])!=0, "invalid location: {}".format(place)
    result=request.json()['results'][0]['geometry']['location'].values()
    print place, result
    return result

get_longlat('london')
