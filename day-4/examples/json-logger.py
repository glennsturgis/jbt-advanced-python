import json
from datetime import datetime


class Logger:

    def __init__(self, service_name):
        self.service = service_name
        self.addons = {}

    def with_fields(self, **kwargs):
        self.addons.update(kwargs)
        return self

    def log(self, **kwargs):
        kwargs = {**kwargs, **self.addons, 'service_name': self.service, 'timestamp': datetime.utcnow().isoformat()}
        print(json.dumps(kwargs))


l = Logger('stdout')
l.with_fields(service_name='filebeat')
l.log(message='Hello World', level='INFO', min=0, max=123)