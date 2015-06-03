import json

from django.db import models
from django.utils import six

from .utils import JSONBeauty, JSONEncoder

class JSONField(models.TextField):

    __metaclass__ = models.SubfieldBase

    description = 'JSON Field object'

    def to_python(self, value):
        if value:
            if isinstance(value, dict):
                value = JSONBeauty(value)
            elif isinstance(value, ( six.string_types, six.text_type, bytes)) :
                value = JSONBeauty( json.loads(value) )
        else:
            value = JSONBeauty()
        return value

    def get_db_prep_save(self, value, *args, **kwargs):
        value = json.dumps(value, cls=JSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, *args, **kwargs)


#     def value_to_string(self, obj):
#         value = self._get_val_from_obj(obj)
#         return self.get_db_prep_value(value, None)


