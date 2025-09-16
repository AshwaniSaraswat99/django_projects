from django.shortcuts import render, redirect
from django.contrib import messages
from chat.models import Room, Chatmessage
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def room(request, room):
    user_name = request.GET.get("username")
    room_details = Room.objects.get(name=room)
    messages = Chatmessage.objects.filter(room=room_details).order_by('date')
    return render(request, "room.html", {
        'room': room,
        'user_name': user_name,
        'room_details': room_details,
        'messages': messages
    })
def checkview(request):
    if request.method=="POST":
        room_name=request.POST["room_name"]
        user_name=request.POST["username"]

        if Room.objects.filter(name=room_name).exists():
            return redirect("/"+room_name+"/?username="+user_name)
        else:
            new_room=Room.objects.create(name=room_name,user_name=user_name)
            new_room.save()
            messages.info(request, "new room have been created")
            return redirect("/"+room_name+"/?username="+user_name,{'room':room_name,'user_name':user_name})
    return render(request, "checkview.html")

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send(request):
    if request.method == "POST":
        message = request.POST.get('message', '')
        user_name = request.POST.get('user_name', '')
        room_id = request.POST.get('room_id', '')
        try:
            room_instance = Room.objects.get(id=room_id)
            Chatmessage.objects.create(message=message, user_name=user_name, room=room_instance)
            return HttpResponse("✅ Message saved")
        except Room.DoesNotExist:
            return HttpResponse("❌ Room not found", status=404)
    return HttpResponse("❌ Invalid request", status=400)

def getmessages(request, room):
    room_details=Room.objects.get(name=room)
    messages=Chatmessage.objects.filter(room=room_details).order_by('date')
    return JsonResponse({
        "messages": [
            {"user_name": msg.user_name, "message": msg.message, "date": msg.date.strftime("%Y-%m-%d %H:%M:%S")}
            for msg in messages
        ]
    })