from flask import Flask, request, render_template, jsonify, session
from yelp import *
import json, urllib, urllib2

# class Car(object):
#     """Represents an automobile"""
#     def __init__(self, year, make, model):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_details(self):
#         print "{} {} {}".format(self.year, self.make, self.model)
#     def query_yelp(term,loc):
#       print 'inside query yelp fxn______________'
#       query_api(term,loc)

# my_car = Car(1990,'honda','accord')
# my_car.print_details()


# print '============ full biz'
# print biz

# print '============ BIZ NAME: ', biz[0]['name']
# print '============ BIZ URL: ', biz[0]['mobile_url']
# print '============ BIZ stars: ', biz[0]['rating_img_url']
# address= biz[0]['location']['display_address']
# address_string= ', '.join(address)
# print ' =======ADDRESS AS STRING: ', address_string

# # print '============ BIZ category', biz[0]['categories']
# categories=biz[0]['categories']
# print '=============BIZ category as list: ', categories
# categories_list=[]
# for c in categories:
#   categories_list.append(''.join(c[0]))
# categories_string=', '.join(categories_list)
# print '=============BIZ category as STRING: ',categories_string
# print '============ BIZ longlat: ', biz[0]['location']['coordinate']['longitude']+','+biz[0]['location']['coordinate']['latitude']


####SAVE RESULTS OF THUS QUERY IN A JSON

# print '============ BIZ longlat: ', str(biz[0]['location']['coordinate']['longitude'])+', '+str(biz[0]['location']['coordinate']['latitude'])


# class Biz_attr(object):
#     def __init__(self, Obj):
#         self.name = biz[0]['name']
#         self.mobile_url = biz[0]['mobile_url']
#         self.stars = biz[0]['rating_img_url']
#         #format category from array in an array to string
#         categories=biz[0]['categories']
#         categories_list=[]
#         for c in categories:
#           categories_list.append(''.join(c[0]))
#         categories_string=', '.join(categories_list)
#         self.category = categories_string
#         # format address from array to string
#         address= str(biz[0]['location']['display_address'][0])+', '+str(biz[0]['location']['display_address'][2])
#         self.address = address
#         self.longlat= str(biz[0]['location']['coordinate']['longitude'])+', '+str(biz[0]['location']['coordinate']['latitude'])

# find_biz=Biz_attr(biz)


# print 'BIZ ATTRs =======', find_biz.name
# print 'BIZ ATTRs =======', find_biz.mobile_url
# print 'BIZ ATTRs =======', find_biz.stars
# print 'BIZ ATTRs =======', find_biz.category
# print 'BIZ ATTRs =======', find_biz.address

# class Biz_attr(object):
#     def __init__(self, Obj):
        # self.name = biz['name']
        # self.mobile_url = biz['mobile_url']
        # self.stars = biz['rating_img_url']
        # #format category from array in an array to string
        # categories=biz['categories']
        # categories_list=[]
        # for c in categories:
        #   categories_list.append(''.join(c[0]))
        # categories_string=', '.join(categories_list)
        # self.category = categories_string
        # # format address from array to string
        # address= str(biz['location']['display_address'][0])+', '+str(biz['location']['display_address'][2])
        # self.address = address

# find_biz=Biz_attr(biz)

# print'=============== biz loop test'

# for i,b in enumerate(biz):
#     print'==============='
#     print i['name']
#     # print i['mobile_url']
#     # print i['rating_img_url']
#     # print 'using an object___________'
#     # print find_biz.name


# print'=============== biz loop test END '


biz=query_api('coffee', '37.7615898, -122.2452818')['businesses']
list_of_dict=[]
for b in biz:
    list_of_dict.append(b)

class Business_info(object):
    def __init__(self, Obj):
        self.name = Obj['name']
        self.mobile_url = Obj['mobile_url']
        self.stars = Obj['rating']
        categories=Obj['categories'] #format category from array in an array to string
        categories_list=[]
        for c in categories:
          categories_list.append(''.join(c[0]))
        categories_string=', '.join(categories_list)
        self.category = categories_string
        addr=Obj['location']['display_address'] # format address from list to string
        str1 = ', '.join(str(e) for e in addr)
        # addr=str(Obj['location']['display_address'][0]) +', '+ str(Obj['location']['display_address'][2])
        self.address = str1
        self.longlat= str(Obj['location']['coordinate']['longitude'])+', '+str(Obj['location']['coordinate']['latitude'])

list_of_obj=[]
for d in list_of_dict:
    b=Business_info(d)
    list_of_obj.append(b)


print '=========looping==='  

for b in list_of_obj:

    print b.name
    print b.category
    print b.longlat
    print b.mobile_url
    print b.address
    print b.stars, ' Stars'

    print '==================='


# for b in biz:
#     print 'BIZ ATTRs =======', find_biz.name
#     print 'BIZ ATTRs =======', find_biz.mobile_url
#     print 'BIZ ATTRs =======', find_biz.stars
#     print 'BIZ ATTRs =======', find_biz.category
#     print 'BIZ ATTRs =======', find_biz.address

# ERROR MSG//list indices must be integers, not dict
