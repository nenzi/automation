from lzma import FORMAT_ALONE
from multiprocessing import AuthenticationError
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AutomationSerializer
from .models import Automation

# Create your views here.


class AutomationView(views.APIView):
    def get(self, request):
        automations = Automation.objects.all()
        response = AutomationSerializer(automations, many=True).data
        return Response(response, status=200)

    def post(self, request):
        serializer = AutomationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def put(self, request):
        return Response({"method": "PUT"})

    def delete(self, request):
        return Response({"method": "DELETE"})


@api_view(["POST"])
def run_automation(request, pk):
    try:
        automation = Automation.objects.get(pk=pk)
        trigger = automation.trigger
        conditions = automation.conditions
        actions = automation.actions

        if trigger == "opt_in":
            if conditions == "":
                pass
            opt_in()
        elif trigger == "time_trigger":
            time_trigger()
        elif trigger == "removed_from_list":
            removed_from_list()
        elif trigger == "purchase_activity":
            purchase_activity()
        elif trigger == "list_trigger":
            list_trigger()
        elif trigger == "page_visited_trigger":
            page_visited_trigger()
        elif trigger == "register_seminar_trigger":
            register_seminar_trigger()

    except Automation.DoesNotExist:
        return Response({"message": "Automation not found"}, status=404)
    automation.status = "running"
    automation.save()
    return Response({"message": "Automation started"}, status=200)


@api_view(["POST"])
def opt_in(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def time_trigger(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def removed_from_list(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def purchase_activity(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def list_trigger(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def page_visited_trigger(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def register_seminar_trigger(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def send_email(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def add_delay(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def add_to_list(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def eject_from_journey(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def apply_tag(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def auto_register_webinar(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def campaign_status(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def is_list_or_segment(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def has_visited_page(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def check_field_list(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def check_purchase_status(request):
    return Response({"method": "POST"})


@api_view(["POST"])
def check_webinar_status(request):
    return Response({"method": "POST"})
