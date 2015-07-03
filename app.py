import requests, string
from flask import Flask, jsonify, render_template, request
# import model 

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
    # 	print 'r is a string!!!!!!!!!!'
    # else:
    # 	print 'r is NOT a string@@@@@@@@'
    # print r, 'return R as a STRINGGGGGGG'
    return r

def get_distance(longlat1,longlat2):
    url='https://maps.googleapis.com/maps/api/distancematrix/json?'
    url+='origins={}&destinations={}'.format(longlat1,longlat2)
    print '====== GET DISTANCE URL ', url
    request=requests.get(url)
    result=request.json()['rows'][0]['elements'][0]['distance']['text']
    # print request.json()['rows'][0]['elements'][0]
    print '=======Distance btwn longlat1 &2', result
    return result
    
# get_d= get_distance('40.7127837, -74.0059413','40.7127837, -74.0059413')
# print 'get_d', get_d


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    loc1=request.form.get('location1')
    loc2=request.form.get('location2')
    print '=====loc 1',loc1,get_longlat(loc1)
    print '=====loc 2',loc2,get_longlat(loc2)
    print '====='
    longlat1=get_longlat(loc1)
    longlat2=get_longlat(loc2)
    # print '=====TURN TO STRING!======',longlat1
    # print '=====TURN TO STRING!======',longlat2

    get_distance(longlat1,longlat2)
    return render_template('index.html')

    
#check if valid location
	#assert loc1 and loc 2 doesnt return an error
#place markers on map
#calc midway point, radius
	# get_distance(loc1,loc2)
#pull up 10? restaurants in the search radius
#populate restaurants in sidebar
# on marker click, corresponding sidebar entry is highlighted and vice versa

    return render_template('index.html')


 
if __name__ == '__main__':
    app.run(debug=True)