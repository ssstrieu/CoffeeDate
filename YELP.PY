# YELP- disable imports before combine with app
import argparse
import json
import pprint
import sys
import urllib
import urllib2
import oauth2

API_HOST = 'api.yelp.com'
DEFAULT_TERM = 'RESTAURANT'
DEFAULT_LOCATION = 'San Fransisco'
SEARCH_LIMIT = 3
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'

#search URL parms
RADIUS_FILTER = 8000 #5mi
SORT= 2 # sort entries by highest rating
OFFSET=10 # used to get 10 more entries

# OAuth credential placeholders that must be filled in by users


CONSUMER_KEY='KnkNJZOb3bXivxWtsG7Eow'
CONSUMER_SECRET='z7lfCVyF6ZaU3_dr8LWMlflfuh0'
TOKEN='fwNYpd3zdX_njQ6Ja_DhXnImPMxt5_wM'
TOKEN_SECRET='IsKZxAUeTfSP07dWT5QaAPkKG4Q'



def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': TOKEN,
            'oauth_consumer_key': CONSUMER_KEY
        }
    )
    token = oauth2.Token(TOKEN, TOKEN_SECRET)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    print '===========signed URL: ', signed_url
    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()
    # print '=========this is the request response=== ', response
    return response

def search(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    
    url_params = {
        'term': term.replace(' ', '+'),
        # 'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'radius_filter':RADIUS_FILTER,
        'sort': SORT,
        'radius_filter' : RADIUS_FILTER,
        'offset':OFFSET,
        'll': location

    }
    
    r=request(API_HOST, SEARCH_PATH, url_params=url_params)
    return r

# def get_business(business_id):
#     """Query the Business API by a business ID.
#     Args:
#         business_id (str): The ID of the business to query.
#     Returns:
#         dict: The JSON response from the request.
#     """
#     business_path = BUSINESS_PATH + business_id
#     b=request(API_HOST, business_path)
#     print '=========BUSINESS RESPONSE======='
#     return b

def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(term, location)

    # businesses = response.get('businesses')

    # if not businesses:
    #     print u'No businesses for {0} in {1} found.'.format(term, location)
    #     return

    # business_id = businesses[0]['id']

    # print u'{0} businesses found, querying business info for the top result "{1}" ...'.format(
    #     len(businesses),
    #     business_id
    # )

    # response = get_business(business_id)

    # print u'Result for business "{0}" found:'.format(business_id)
    #########  pprint displates results of query in terminal
    print '========QUERY RESPONSE OBJECT===========', response
    return response
    


# def main():
#     parser = argparse.ArgumentParser()

#     parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM, type=str, help='Search term (default: %(default)s)')
#     parser.add_argument('-l', '--location', dest='location', default=DEFAULT_LOCATION, type=str, help='Search location (default: %(default)s)')

#     input_values = parser.parse_args()
#     # print '===MAIN====input_values=======', input_values
#     # print '===MAIN====input_values.term=======', input_values.term
#     # print '===MAIN====input_values.locaiton=======', input_values.location

#     try:
#         query_api(input_values.term, input_values.location)
#     except urllib2.HTTPError as error:
#         sys.exit('Encountered HTTP error {0}. Abort program.'.format(error.code))

# def query_yelp(foodtype, LL):
#     #just renaming to be more clear
#     query_api(foodtype, LL)

if __name__ == '__main__':
    # main()
    query_api('bar', '37.7615898, -122.2452818')