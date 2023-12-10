from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer,UserTaskSerializer
from .models import Task
from django.contrib.auth import authenticate
from app.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return{
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }

# @desc Register the user
# @route POST /api/users/register/
# @access public

class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # token = get_tokens_for_user(user)
            return Response({ 'msg' : 'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @desc Login the user
# @route POST /api/users/login/
# @access public

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg' : 'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {"non_field_errors":["Email or Password is not valid"]} },status=status.HTTP_404_NOT_FOUND)

# @desc Profile of the user
# @route GET /api/users/profile/
# @access private

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        print(serializer.data['id'])
        return Response(serializer.data, status=status.HTTP_200_OK)




class UserTasksView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    # @desc Create a Task
    # @route POST /api/users/tasks/
    # @access private

    def post(self,request,format=None):
        serializer = UserTaskSerializer(data= request.data)
        if serializer.is_valid():
            # print(request.user)
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # @desc Retrieve Tasks
    # @route GET /api/users/tasks/
    # @access private

    def get(self, request, title=None):
        user_info = UserProfileSerializer(request.user)
        tasks = Task.objects.filter(user=user_info.data['id'])
    
        if(len(tasks)>0):
            serializer = UserTaskSerializer(tasks,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"No tasks are there to retrieve"}, status=status.HTTP_400_BAD_REQUEST)

class UserTaskView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    # @desc Get a Task
    # @route GET /api/users/tasks/<str:title>
    # @access private

    def get(self, request, title=None):
        user_info = UserProfileSerializer(request.user)
        if(title==None):
            return Response({"mesg":"Please search with title of the task"},status=status.HTTP_200_OK)
        else:
            tasks = Task.objects.filter(user=user_info.data['id'],title=title)
        if(len(tasks)>0):
            serializer = UserTaskSerializer(tasks,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"No such tasks are there"}, status=status.HTTP_400_BAD_REQUEST)
    
    # @desc Partially Update a Task
    # @route PATCH /api/users/tasks/<str:title>
    # @access private

    def patch(self, request, title=None):
        user_info = UserProfileSerializer(request.user)
        if(title==None):
            return Response({"msg":"Please search with title of the task"},status=status.HTTP_200_OK)
        else:
            task = Task.objects.filter(user=user_info.data['id'],title=title)
        if(len(task)>0):
            serializer = UserTaskSerializer(task,data=request.data,partial=True)
            if(serializer.is_valid()):
                serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"No such tasks are there"}, status=status.HTTP_400_BAD_REQUEST) 

    # @desc Update a Task
    # @route PUT /api/users/tasks/<str:title>
    # @access private

    def put(self, request, title=None):
        user_info = UserProfileSerializer(request.user)
        task = ''
        if(title==None):
            return Response({"msg":"Please search with title of the task"},status=status.HTTP_200_OK)
        else:
            task = Task.objects.filter(user=user_info.data['id'],title=title)
        
        if(len(task)>0):
            serializer = UserTaskSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"msg":"Please search with title of the task"}, status=status.HTTP_400_BAD_REQUEST)

    # @desc Delete a Task
    # @route DELETE /api/users/tasks/<str:title>
    # @access private

    def delete(self, request, title=None):
        user_info = UserProfileSerializer(request.user)

        if(title==None):
            return Response({"msg":"Please search with title of the task"},status=status.HTTP_200_OK)
        else:
            task = Task.objects.filter(user=user_info.data['id'],title=title)
            if(len(task)>0):
                task.delete()
                return Response({"msg":"Task Removed \nNow you no need to do this task"}, status=status.HTTP_200_OK)  
            return Response({"msg":"No such tasks are there"}, status=status.HTTP_200_OK)  
