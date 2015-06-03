import itertools, json 

from django.db import models
from django.utils import six

class JSONAwareQuerySet(models.query.QuerySet):
    def __init__(self, json_fields=[], *args, **kwargs):
        self.json_fields = json_fields
        super(JSONAwareQuerySet, self).__init__(*args, **kwargs)

    def _filter_or_exclude(self, negate, *args, **kwargs):
        extra_lookups = {}

        for lookup in kwargs:
            if lookup.split('__')[0] in self.json_fields:
                extra_lookups[lookup] = kwargs[lookup]

        for key in extra_lookups:
            kwargs.pop(key)

        clone = super(JSONAwareQuerySet, self)._filter_or_exclude(negate, *args, **kwargs)

        result = []

        if extra_lookups.keys():
            len(clone)# Fill the cache

            for item, lookup in itertools.product(self, extra_lookups.keys()):
                if not negate and self._evaluate_json_lookup(item, lookup, extra_lookups[lookup]):
                    result.append(item)
                elif negate and not self._evaluate_json_lookup(item, lookup, extra_lookups[lookup]):
                    result.append(item)

            clone._result_cache = result

        return clone

    def _evaluate_json_lookup(self, item, lookup, value):
        oper = 'exact'

        evaluators = {
            'icontains': lambda item, value: item.lower() in value.lower(),
            'contains': lambda item, value: item in value,
            'in': lambda item, value: item in value,
            'iexact': lambda item, value: item.lower() == value.lower(),
            'exact': lambda item, value: item == value,
            'lt': lambda item, value: item < value,
            'lte': lambda item, value: item <= value,
            'gt': lambda item, value: item > value,
            'gte': lambda item, value: item >= value,
            'range': lambda item, value: item >= value[0] and item <= value[1],
        }

        def _getattr(obj, key):
            if isinstance(obj, dict):
                return obj[key]
            return getattr(obj, key)

        if lookup.split('__')[-1] in evaluators.keys():
            oper = lookup.split('__')[-1]
            lookup = '__'.join(lookup.split('__')[:-1])

        # DGT Verifica que el objeto json se un dictionario o lo convierte          
        field = getattr(item, lookup.split('__')[0])
        if isinstance(field, dict) : 
            jdict = field
        elif isinstance( field, ( six.string_types, six.text_type, bytes)) :
            try:
                jdict = json.loads(field)
            except :
                return False
        else: return False

        for key in lookup.split('__')[1:]:
            try:
                jdict = _getattr(jdict, key)
            except (AttributeError, KeyError):
                return False

        return evaluators[oper](jdict, value)

#     def count(self):
#         return super(JSONAwareQuerySet, self).count()
# 
#     def all(self):
#         return self
# 
#     def order_by(self, *args, **kwargs):
#         return self

    def _clone(self, *args, **kwargs):
        clone = super(JSONAwareQuerySet, self)._clone(*args, **kwargs)
        clone.json_fields = self.json_fields
        return clone


class JSONAwareManager(models.Manager):
    
    def __init__(self, json_fields=[], *args, **kwargs):
        self.json_fields = json_fields
        super(JSONAwareManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        return JSONAwareQuerySet(self.json_fields, self.model)


# https://docs.djangoproject.com/en/1.8/topics/db/managers/#manager-names        