from flask import Flask, jsonify, render_template, request, session
from maps import *
from yelp import *

app = Flask(__name__)  
app.secret_key = 'thisisasecret'

# Routes=======================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def find(): 
    started_search=True
    session['loc1']=request.form.get('location1')
    session['loc2']=request.form.get('location2')
    session['foodtype']=request.form.get('foodtype')
    loc1=session['loc1']
    loc2=session['loc2']
    foodtype=session['foodtype']
    session['offset']=0
    offset=session['offset']

    longlat1=get_longlat(loc1)
    longlat2=get_longlat(loc2)
    midxy=find_midpoint(longlat1,longlat2)
    session['midxy']=midxy
    print '======session xy====', session['midxy']
    print '======1====', session['loc1']
    print '======2====', session['loc2']

    try:
        radius =8000
        biz=query_api(foodtype, midxy, radius, 0)['businesses']
        if len(biz)<1:
            print '0 results found. Searching in greater radius.'
            radius+=8000
            biz=query_api(foodtype, midxy, radius, 0)
            print 'Search Radius is now: ',radius
        list_of_dict=[]
        for b in biz:
            list_of_dict.append(b)
        print '============= list of dict', len(list_of_dict)


        list_of_obj=[]
        for i in list_of_dict:
            list_of_obj.append(Business_info(i))

        print '==============', len(list_of_obj)
        print '==============', list_of_obj

#########FIXXXXXXX if property doesn't exist, don't fail. 

        

        # list_of_obj=[]
        # test=Business_info(list_of_dict[3])
        # print '==============', test
        # print '==============', test.name
        # list_of_obj.append(test)
        # test=Business_info(list_of_dict[0])
        # list_of_obj.append(test)

        # print '==============', len(list_of_obj)

        # for i in list_of_dict: 
        #     b=Business_info(i)
        #     print '==============', b, '=============='
        #     list_of_obj.append(b)
        #     print '==============', b, '=============='
        #     print '==============', len(list_of_obj), '=============='




        # for d in list_of_dict:
        #     b=Business_info(d)
        #     list_of_obj.append(b)

        # print '============= list of obj', len(list_of_obj)
        # print '============= list of obj', list_of_obj




    except:
        print 'broke :('
        error=True
        errormsg='Your search returned no results. Please try a different search.'
        return render_template('index.html',errormsg=errormsg, error=error)

    return render_template('index.html', list_of_obj=list_of_obj, longlat1=longlat1,longlat2=longlat2,loc1=loc1,loc2=loc2, midxy=midxy,started_search=started_search)

@app.route('/more', methods=['POST'])
def find_more():

    started_search=True
    print '======find more session====', session['loc1']
    print '======find more session====', session['loc2']
    print '======find more session====', session['foodtype']
    print '======find more session====', session['midxy']
   
    
    loc1=session['loc1']
    loc2=session['loc2']
    foodtype=session['foodtype']
    midxy=session['midxy']
    session['offset']+= 7
    offset=session['offset']
    print 'offset now is: =====', offset


    try:
        radius =8000
        biz=query_api(foodtype, midxy, radius, offset)['businesses']
        list_of_dict=[]
        for b in biz:
            list_of_dict.append(b)
        print '============= list of dict', len(list_of_dict)
        
        list_of_obj=[]
        for d in list_of_dict:
            b=Business_info(d)
            list_of_obj.append(b)
        print '============= list of obj', len(list_of_obj)
    except:
        print 'broke :('
        error=True
        errormsg='No more results. Please try a different search.'
        return render_template('index.html',errormsg=errormsg, error=error)
    return render_template('index.html', list_of_obj=list_of_obj, loc1=loc1,loc2=loc2, midxy=midxy,started_search=started_search)
    # return render_template('index.html', list_of_obj=list_of_obj, loc1=loc1 )



if __name__ == '__main__':
    app.run(debug=True)
    # find_more()

