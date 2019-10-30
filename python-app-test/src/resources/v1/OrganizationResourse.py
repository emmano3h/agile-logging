import sys
sys.path.append("/usr/src/app")
from datetime import datetime
import time, json
from src.utils import helpers as hp

log = hp.getlogger("logs.requests.OrganizationResource", '/usr/src/logs/organization_logic.log')

class OrganizationResource:
    def on_get(self, req, resp):
        request_identifier = hp.getRequestIdentifiers()
        log.info(hp.formatLogMessage(message='API request came at endpoint.',request_identifier=request_identifier))
        resp.body = {
            'result': 'Wow! Resulttttt!:)',
        }
        log.info(hp.formatLogMessage(message='API request returned reponse.',request_identifier=request_identifier, metadata=resp.body))