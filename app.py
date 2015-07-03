import requests, string
from flask import Flask, jsonify, render_template, request
# from model import * 
# from YELP import *

app = Flask(__name__)

#parse location info into longitude/latitude
#map those 2 locations and get distance
#find equidistant place inbetween (20% give?)
#Yelp places in that location 
#Show yelp locations in sidebar and map
#clicking should link to yelp page or direction on google maps

##stretch goals:
###add multiple parties
### filter by food type, open hours etc
### factor in mode of transportation to get somewhere at the same time

#comment out imports before integrating with rest of app

# from flask import Flask, jsonify, render_template, request

API_KEY='AIzaSyAPyQ4vH8xfcrDI5lQ1DiTkaMvL-LP8_KU'


def get_longlat(place):
    url='https://maps.googleapis.com/maps/api/geocode/json?'
    url+='address={}&key={}'.format(place,API_KEY)
    request=requests.get(url)
    # print url
    #check if valid place before query googlemaps
    assert len(request.json()['results'])!=0, "invalid location: {}".format(place)
    result=request.json()['results'][0]['geometry']['location'].values()
    # print result
    r =str(result[0])+', '+str(result[1])
    # if type(r) is str:
    #   print 'r is a string!!!!!!!!!!'
    # else:
    #   print 'r is NOT a string@@@@@@@@'
    # print r, 'return R as a STRINGGGGGGG'
    return r

def get_distance(longlat1,longlat2):
    url='https://maps.googleapis.com/maps/api/distancematrix/json?'
    url+='origins={}&destinations={}'.format(longlat1,longlat2)
    # print '====== GET DISTANCE URL ', url
    request=requests.get(url)
    result=request.json()['rows'][0]['elements'][0]['distance']['text']
    # print request.json()['rows'][0]['elements'][0]
    print '=======Distance btwn longlat1 &2', result
    return result
    
# get_d= get_distance('40.7127837, -74.0059413','40.7127837, -74.0059413')
# print 'get_d', get_d

def find_midpoint(longlat1,longlat2):
    #divide distance by 2 and get longlat of that location
    #input is string, convert to array of integers for math, then back to string 
    print 'string to array========', longlat1.split(',')
    longlat1_list=longlat1.split(',')
    longlat2_list=longlat2.split(',')
    midx=(float(longlat1_list[0])+float(longlat2_list[0]))/2
    midy=(float(longlat1_list[1])+float(longlat2_list[1]))/2
    midxy=str(midx)+', '+str(midy)
    print 'MIDPOINT========= as string: ',midxy
    return midxy

# find_midpoint('0,0', '-200,-200')    

# def yelp_call(foodtype,midxy):
#     foodtype= 'dessert'
#     LL='37.7919615,-122.2287941' #oakland ;replate with midxy later
#     query_yelp()
#     #oauth
#     #pull 
#     url='https://maps.googleapis.com/maps/api/distancematrix/json?'
#     url+='origins={}&destinations={}'.format(longlat1,longlat2)
#     # print '====== GET DISTANCE URL ', url
#     request=requests.get(url)
#     result=request.json()['rows'][0]['elements'][0]['distance']['text']
#     # print request.json()['rows'][0]['elements'][0]
#     print '=======Distance btwn longlat1 &2', result
#     return result









# Routes=======================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    loc1=request.form.get('location1')
    loc2=request.form.get('location2')
    foodtype=request.form.get('foodtype')
    print '=====loc 1',loc1,get_longlat(loc1)
    print '=====loc 2',loc2,get_longlat(loc2)
    print '=====FOODTYPE', foodtype
    longlat1=get_longlat(loc1)
    longlat2=get_longlat(loc2)
    # print '=====TURN TO STRING!======',longlat1
    # print '=====TURN TO STRING!======',longlat2
    # still need to control for error involving multiple cities named hte same thing...
    get_distance(longlat1,longlat2)
    midxy=find_midpoint(longlat1,longlat2)
    
    # yelp_call(foodtype,midxy)
    return render_template('index.html')

    
#check if valid location
    #assert loc1 and loc 2 doesnt return an error
#place markers on map
#calc midway point, radius
    # get_distance(loc1,loc2)
#pull up 10? restaurants in the search radius
#populate restaurants in sidebar
# on marker click, corresponding sidebar entry is highlighted and vice versa
 
if __name__ == '__main__':
    app.run(debug=True)