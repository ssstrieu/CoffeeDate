from flask import Flask, jsonify, render_template, request, session
from maps import *
from yelp import *

app = Flask(__name__)  
# app.secret_key = 'thisisasecret'


# Routes=======================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find():   
    loc1=request.form.get('location1')
    loc2=request.form.get('location2')
    foodtype=request.form.get('foodtype')
    # loc1=session['loc1']
    # loc2=session['loc2']
    # foodtype=session['foodtype']
    longlat1=get_longlat(loc1)
    longlat2=get_longlat(loc2)
    midxy=find_midpoint(longlat1,longlat2)

    biz=query_api(foodtype, midxy)['businesses']
    list_of_dict=[]
    for b in biz:
        list_of_dict.append(b)
    print '============= list of dict', len(list_of_dict)
    
    list_of_obj=[]
    for d in list_of_dict:
        b=Business_info(d)
        list_of_obj.append(b)
    print '============= list of obj', len(list_of_obj)


    return render_template('index.html', list_of_obj=list_of_obj)

# @app.route('/more', methods=['GET'])
# def find_more():
#     print session.get['loc1']
#     pass
#     return render_template('index.html', list_of_obj=list_of_obj)



if __name__ == '__main__':
    app.run(debug=True)