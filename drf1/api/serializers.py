# in this file we're going to need to create model serializers because the response object cannot natively handle complex data types such as django model instances, so we'll first need to serialize this data before we can actually render it out
# we'll create serializers for our item model convert instances of our items from objects into data types that our response object can understand

from rest_framework import serializers
from base.models import Item

# our ItemSerializer will inherit from the serializer class
class ItemSerializer(serializers.ModelSerializer):
    # inner meta class
    class Meta:
        # set two required attributes
        model = Item
        # and the fields we want to serialize
        # we can pass in a list of fields here if we want
        fields = '__all__'
