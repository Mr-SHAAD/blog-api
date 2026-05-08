from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer, RegisterSerializer
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'User created successfully'},
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list_view(request):
    
    # GET — sare posts lao
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    # POST — naya post banao
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail_view(request, pk):
    
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(
            {'error': 'post not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # PUT
    if request.method == 'PUT':
        if post.author != request.user:
            return Response(
                {'error': ' you don not have Permission'},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # DELETE
    if request.method == 'DELETE':
        if post.author != request.user:
            return Response(
                {'error': ' you don not have Permission'},
                status=status.HTTP_403_FORBIDDEN
            )
        post.delete()
        return Response(
            {'message': 'Post deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_view(request, pk):
    
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(
            {'error': 'post not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(
            author=request.user,
            post=post
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_view(request, pk):
    
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(
            {'error': 'post not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    
    if not created:
        like.delete()
        return Response({'message': 'Successfully unliked'})
    
    return Response({'message': 'Successfully liked'})



