import sys
sys.path.append("/usr/src/app/src")
import falcon
from middlewares.middlewares import (
    ContentEncodingMiddleware,
)
from  resources.v1.OrganizationResourse import *

app = falcon.API(middleware=[
    ContentEncodingMiddleware(),
])

app.add_route('/v1/organization', OrganizationResource())



