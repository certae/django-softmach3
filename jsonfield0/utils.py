import json, datetime, decimal

class JSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time and decimal types.
    """

    def default(self, obj):
        if isinstance(obj, ( datetime.date, datetime.time, datetime.datetime)):
            return obj.isoformat()

        elif isinstance(obj,  decimal.Decimal ):
            return float( obj )

        else:
            return json.JSONEncoder.default(self, obj)


class JSONBeauty(dict):

    def __repr__(self):
        return json.dumps(self, cls=JSONEncoder, indent=4)
