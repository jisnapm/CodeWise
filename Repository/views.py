from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from Repository.models import QuestionDb, SubmissionsDb
from Repository.serializers import QuestionSerializer, SubmissionSerializer

# Create your views here.

class QuestionListCreateView(APIView):
    def get(self, request):
        qs = QuestionDb.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(data = serializer_instance.data)


    def post(self, request):
        form_data = request.data
        serializer_instance = QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data = serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data = {"message": "Question created successfully!"})

        else:
            return Response(data = {"errors": serializer_instance.errors})

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        qs = QuestionDb.objects.get(id=pk)
        serializer_instance = QuestionSerializer(qs)
        return Response(data = serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        s_instance = QuestionSerializer(data=form_data)
        if s_instance.is_valid():
            actual_data = s_instance.validated_data
            QuestionDb.objects.filter(id=pk).update(**actual_data)
            return Response(data = s_instance.data)

        else:
            return Response(data = s_instance.errors)

    def delete(self, request, pk):
        QuestionDb.objects.filter(id=pk).delete()
        return Response(data = {"message": "Question deleted successfully!"})
    
class SubmissionsListCreateView(APIView):
    def get(self, request):
        qs = SubmissionsDb.objects.all()
        submission_instance = SubmissionSerializer(qs, many= True)
        return Response(data= submission_instance.data)

    def post(self, request):
        form_data = request.data
        sub_instance = SubmissionSerializer(data=form_data)
        if sub_instance.is_valid():
            actual_data = sub_instance.validated_data
            SubmissionsDb.objects.create(**actual_data)
            return Response(data={"message": "Answers Submitted!"})
        else:
            return Response(data=sub_instance.errors)

class SubmissionsRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        # qs = SubmissionsDb.objects.get(id = pk)
        qs = get_object_or_404(SubmissionsDb, id=pk)
        s_instance = SubmissionSerializer(qs)
        return Response(data= s_instance.data)

    def put(self, request, pk):
        form_data = request.data
        submission_instance = SubmissionSerializer(data= form_data)
        if submission_instance.is_valid():
            actual_data = submission_instance.validated_data
            SubmissionsDb.objects.filter(id=pk).update(**actual_data)
            return Response(data={"message":"submission updated!"})
        else:
            return Response(data=submission_instance.errors)

    def delete(self, request, pk):
        SubmissionsDb.objects.filter(id=pk).delete()
        return Response(data={"message": "Submission deleted!"})