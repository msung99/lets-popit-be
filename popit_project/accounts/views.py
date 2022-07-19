from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializer import RegisterSerializer,UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from django.contrib.auth import authenticate

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # jwt token 접근해주기
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            #쿠키에 넣어주기...아직 어떤식으로 해야될지 모르겠는데 이렇게 설정만 우선 해주었다. 
            res.set_cookie("access", access_token, httponly=True) # 유저가 로그인에 성공했을때, 해당 유저를 로그인 기간동안 인증하는 토큰을 cookie에 저장해야 할 경우, HttpResponse 또는 JsonResponse 에 장고에서 제공하는 set_cookie 메소드를 사용하여 토큰을 발행할 수 있다.
            res.set_cookie("refresh", refresh_token, httponly=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AuthView(APIView):
    
    def post(self, request):
        user = authenticate(
            login_id=request.data.get("login_id"), password=request.data.get("password")
        )
        if user is not None:
            serializer = UserSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            return res
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)        