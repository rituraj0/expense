from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.serializers import Serializer


from .models import Expense

class ExpenseResource(ModelResource):

    class Meta:
        queryset = Expense.objects.all()
        resource_name = 'expense'
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'plist'])
        #http://blog.brabadu.com/2011/06/easy-rest-api-with-django-tastypie.html
        excludes = ['id']
        include_resource_uri = False
    
    def dehydrate(self, bundle):
    	print(" ** * ");
    	print(bundle)
    	print("****")
    	return bundle.data