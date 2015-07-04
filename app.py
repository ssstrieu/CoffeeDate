from flask import Flask, jsonify, render_template, request
from maps import *
from yelp import *

app = Flask(__name__)  


# #TEST YELP
b=query_api('bar', '37.7615898, -122.2452818')
biz={}
biz.name=b['businesses'][0]

# # test maps    
# get_d= get_distance('los angeles','40.7127837, -74.0059413')
# print 'get_d', get_d

# midxy=find_midpoint(get_longlat('los angeles'),'40.7127837, -74.0059413')
# print 'midxy', midxy


# Routes=======================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():
    loc1=request.form.get('location1')
    loc2=request.form.get('location2')
    foodtype=request.form.get('foodtype')
    # print '=====loc 1',loc1
    # print '=====loc 2',loc2
    # print '=====foodtype',foodtype
    longlat1=get_longlat(loc1)
    longlat2=get_longlat(loc2)
    # print '=====TURN TO STRING!======',longlat1
    # print '=====TURN TO STRING!======',longlat2
    # still need to control for error involving multiple cities named hte same thing...
    get_distance(longlat1,longlat2)
    midxy=find_midpoint(longlat1,longlat2)
    # b=query_api(foodtype,midxy)
    # print b[]
    #need to create error message for no buisnesses found
    #biz= object with queried biz data
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)