import inspect
import json
import exception

exc = []
for e in dir(exception):
    if inspect.isclass(getattr(exception, e)):
        if not e.startswith('_') and issubclass(getattr(exception, e), exception.CinderException):
            exc.append({'name': e,
                      'code': getattr(exception, e).code,
                      'msg': getattr(exception, e).message})



print json.dumps({'cinder': exc})
