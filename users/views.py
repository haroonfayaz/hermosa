from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new User instance with the validated data
            user = User.objects.create_user(
                username=serializer.validated_data['email'],
                password=request.data['password']
            )
            # Save additional fields from the serializer
            user.name = serializer.validated_data['name']
            user.contact = serializer.validated_data['contact']
            user.travel_date = serializer.validated_data['travel_date']
            user.save()
            # Serialize the user data
            serialized_user = UserSerializer(user)
            return Response(serialized_user.data)
        return Response(serializer.errors, status=400)

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer

