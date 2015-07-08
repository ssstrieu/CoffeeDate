import requests

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
    # print place,':  return longlat "R" as a STRING====', r 
    return r

def get_distance(longlat1,longlat2):
    url='https://maps.googleapis.com/maps/api/distancematrix/json?'
    url+='origins={}&destinations={}'.format(longlat1,longlat2)
    # print '====== GET DISTANCE URL ', url
    request=requests.get(url)
    result=request.json()['rows'][0]['elements'][0]['distance']['text']
    # print request.json()['rows'][0]['elements'][0]
    # print '=======Distance btwn longlat1 & 2 ====', result
    return result

def find_midpoint(longlat1,longlat2):
    #divide distance by 2 and get longlat of that location
    #input is string, convert to array of integers for math, then back to string 
    # print'string to array========', longlat1.split(',')
    longlat1_list=longlat1.split(',')
    longlat2_list=longlat2.split(',')
    midx=(float(longlat1_list[0])+float(longlat2_list[0]))/2
    midy=(float(longlat1_list[1])+float(longlat2_list[1]))/2
    midxy=str(midx)+', '+str(midy)
    # print 'MIDPOINT========= as string: ',midxy
    return midxy

# # test calling    
# get_d= get_distance('los angeles','40.7127837, -74.0059413')
# print 'get_d', get_d

# midxy=find_midpoint(get_longlat('los angeles'),'40.7127837, -74.0059413')
# print 'midxy', midxy
# get_longlat('14441 tiburon rd, san leandro, ca 94577')



        