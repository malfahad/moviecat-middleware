
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .serializer import MovieSerializer
from ..s3.client import bucket
from ..jsonrpc.client import jsonrpc_client


class MoviesView(GenericAPIView):
    permission_classes = [AllowAny]
    renderer_class = (JSONRenderer,)
    serializer_class = MovieSerializer

    def post(self, request):
        data = request.get('data')
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        #upload images to s3
        bucket.upload_image(data.get('image_name'), data.get('image'))
        #send payload to JSONRPC
        jsonrpc_client.create_movie(
            data.get('id'),
            data.get('')
        )

        #return user data
        return Response(data=data, status=status.HTTP_201_CREATED)

