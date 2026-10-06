from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_short_link
from .serializers import ShortenSerializer, LinkSerializer
from rest_framework import generics
from .models import Link
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F



class ShortenView(APIView):
    def post(self, request):
        serializer = ShortenSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        link = create_short_link(serializer.validated_data['url'])
        return Response(
            {"short_code": link.short_code ,
                         "short_url": request.build_absolute_uri(f"/{link.short_code}"),
                        "original_url": link.original_url,}
                      , status=status.HTTP_201_CREATED)


class RecentLinksView(generics.ListAPIView):
    queryset = Link.objects.order_by("-created_at")[:50]
    serializer_class = LinkSerializer



def redirect_view(request, code):
    # NAIVE, jaan-boojh kar: har request pe DB read...
    link = get_object_or_404(Link, short_code=code)
    # ...aur har request pe DB write.
    Link.objects.filter(pk=link.pk).update(click_count=F("click_count") + 1)
    return HttpResponseRedirect(link.original_url)   # 302