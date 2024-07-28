from django.urls import path
from .views import ( import_data, attribute_name_data, 
                    attribute_value_data, attribute_data, image_data, 
                    product_data, product_attributes_data, 
                    product_image_data, catalog_data,
                     attribute_name_detail, 
                    attribute_value_detail, attribute_detail, image_detail, 
                    product_detail, product_attributes_detail, 
                    product_image_detail, catalog_detail)
urlpatterns = [
    #Post
    path('import', import_data),
    #Get all data
    path('detail/attributename/', attribute_name_data),
    path('detail/attributevalue/', attribute_value_data),
    path('detail/attribute/', attribute_data),
    path('detail/image/', image_data),
    path('detail/product/', product_data),
    path('detail/productAttributes/', product_attributes_data),
    path('detail/productimage/', product_image_data),
    path('detail/catalog/', catalog_data),
    #Get detail
    path('detail/attributename/<int:id>', attribute_name_detail),
    path('detail/attributevalue/<int:id>', attribute_value_detail),
    path('detail/attribute/<int:id>', attribute_detail),
    path('detail/image/<int:id>', image_detail),
    path('detail/product/<int:id>', product_detail),
    path('detail/productAttributes/<int:id>', product_attributes_detail),
    path('detail/productimage/<int:id>', product_image_detail),
    path('detail/catalog/<int:id>', catalog_detail)
]
