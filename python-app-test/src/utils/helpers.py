import sys
sys.path.append("/usr/src/app")
from datetime import datetime
import json
import random
import logging
import os, socket

from fluent import asynchandler as handler
from fluent import handler as fluent_handler
import msgpack
from io import BytesIO
from src.utils import constants as cst

# ///// BEGIN LOGGER ////////
# Logs pending
def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)

# Logger handler configuration
def getlogger(name, log_file, log_level="INFO"):
    importer_logger = logging.getLogger(name)
    importer_logger.setLevel(log_level)

    # Handler to send logs in files
    fh = logging.FileHandler(filename=log_file)
    fh.setLevel(log_level)
    formatter_file = logging.Formatter('%(asctime)s - %(msecs)d - %(funcName)s - %(lineno)d : %(levelname)s : %(message)s')
    fh.setFormatter(formatter_file)
    importer_logger.addHandler(fh)

    # Handler to send logs in Elasticsearch
    flh = handler.FluentHandler(name, host=cst.FLUENT_CONFIGURATION["SERVER"], port=cst.FLUENT_CONFIGURATION["PORT"], buffer_overflow_handler=overflow_handler)

    custom_format = {
      'host': '%(hostname)s',
      'where': '%(module)s.%(funcName)s',
      'type': '%(levelname)s',
      'stack_trace': '%(exc_text)s',
      'lineno': '%(lineno)s',
      'pathname':'%(pathname)s',
    }
    formatter_flh = fluent_handler.FluentRecordFormatter(custom_format)
    flh.setFormatter(formatter_flh)
    importer_logger.addHandler(flh)
    return importer_logger

# ///// END  LOGGER ////////

# ///// BEGIN COMMON METHODS ////////
def getDefaultdatetime():
    return datetime.utcnow()

# Format log message template
def formatLogMessage(message='',request_identifier={},metadata =''):
    request_timestamp = str(getDefaultdatetime())
    metadata = json.dumps(metadata)
    extra = {'message': message,'request_identifier': request_identifier, "request_timestamp": request_timestamp, "metadata": metadata}
    return extra

# generate ids
def generate_sharable_id(length=10, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for _ in range(length))

# Generate request id
def getRequestIdentifiers():
    request_id = generate_sharable_id(length=20)
    my_nodename = (os.uname().nodename) if os.uname().nodename is not None else ''
    my_host = socket.gethostname()
    myhost_ip = socket.gethostbyname(socket.gethostname())
    return {'request_id': request_id,'nodename': my_nodename, 'host': my_host, 'host_ip': myhost_ip}

# ///// END COMMON METHODS ////////

