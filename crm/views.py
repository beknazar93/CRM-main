from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Employee,Client,SalesPipelineStage
from .serializers import EmployeeSerializer,ClientSerializer,SalesPipelineStageSerializer



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # Метод удаления сотрудника
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    fields = ['id', 'name', 'email', 'phone', 'time_create', 'time_update', 'stage', 'payment', 'price',
              'sport_category', 'trainer', 'year',
              'month', 'day', 'comment']
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    # Метод удаления клиента
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class SalesPipelineStageViewSet(viewsets.ModelViewSet):
    queryset = SalesPipelineStage.objects.all()
    serializer_class = SalesPipelineStageSerializer

# from rest_framework import viewsets, status
# from rest_framework.response import Response
#
# from .models import Employee, Client, SalesPipelineStage
# from .serializers import EmployeeSerializer, ClientSerializer, SalesPipelineStageSerializer
#
# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']
#     # Метод удаления сотрудника
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#
#
# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']
#     # Метод удаления клиента
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#
#
# class SalesPipelineStageViewSet(viewsets.ModelViewSet):
#     queryset = SalesPipelineStage.objects.all()
#     serializer_class = SalesPipelineStageSerializer
#     http_method_names = ['get', 'post', 'put', 'patch', 'delete']
#     # Метод удаления этапа воронки продаж
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"message": "SalesPipelineStage deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
