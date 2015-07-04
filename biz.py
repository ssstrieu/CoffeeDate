from yelp import *
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
biz=query_api('coffee', '37.7615898, -122.2452818')['businesses']

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
# print '============ BIZ longlat: ', biz[0]['name']





class Biz_attr(object):
    def __init__(self, Obj):
        self.name = biz[0]['name']
        self.mobile_url = biz[0]['mobile_url']
        self.stars = biz[0]['rating_img_url']
        #format category from array in an array to string
        categories=biz[0]['categories']
        categories_list=[]
        for c in categories:
          categories_list.append(''.join(c[0]))
        categories_string=', '.join(categories_list)
        self.category = categories_string
        # format address from array to string
        address= str(biz[0]['location']['display_address'][0])+', '+str(biz[0]['location']['display_address'][2])
        self.address = address

print'=============== biz loop test'
for b in biz:
    print b['name']

find_biz=Biz_attr(biz)
print 'BIZ ATTRs =======', find_biz.name
print 'BIZ ATTRs =======', find_biz.mobile_url
print 'BIZ ATTRs =======', find_biz.stars
print 'BIZ ATTRs =======', find_biz.category
print 'BIZ ATTRs =======', find_biz.address





