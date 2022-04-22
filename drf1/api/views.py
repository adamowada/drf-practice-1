# this response object will take in any python data or already serialized data that we pass into it and will render it out as json data
from rest_framework.response import Response
# bc we're using function based views we'll need api view decorator and we'll use this with all of our views
from rest_framework.decorators import api_view
from base.models import Item
from . serializers import ItemSerializer


# GET method in list of allowed methods
@api_view(['GET'])
def get_data(request):
    # query all the items from our database
    items = Item.objects.all()
    # then we need to serialize these items before we can return them
    # setting many to True tells our serializer that we're going to serialize multiple items
    # whereas if we only wanted to return back 1 item we would set this to False
    serializer = ItemSerializer(items, many=True)
    # this will output as json data
    # return back the .data value
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        # this will create a new item in the database
        serializer.save()
    # return newly created item in response
    return Response(serializer.data)