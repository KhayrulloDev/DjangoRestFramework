from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog, Hashtag
from .serializer import BlogSerializer
from rest_framework.permissions import IsAuthenticated

# Fork example functionbasedview
# @api_view(['GET'])
# def home(request):
#     return Response({'message':'Hello World'})


class HomeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        blogs = Blog.objects.all().order_by('-created_at')
        blog_serializer = BlogSerializer(blogs, many=True)
        # blogs_data = []               ### change to dict
        # for blog in blogs:
        #     blog_dict = {
        #         'id': blog.id,
        #         'title': blog.title,
        #         'description': blog.description,
        #         'created_at': blog.created_at
        #     }
        #     blogs_data.append(blog_dict)
        return Response(blog_serializer.data)