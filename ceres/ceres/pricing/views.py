# Create your views here.

import pdb;

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from twilio import twiml

from models import Crop, Department, PriceReport

#from twilio.util import RequestValidator

#AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
#def validate_request(request):
#  validator = RequestValidator(AUTH_TOKEN)
#  # the callback URL you provided to Twilio
#  url = "http://davidykay.com:5000"
#  # the POST variables attached to the request (eg "From", "To")
#  post_vars = request.POST
#  # X-Twilio-Signature header value
#  signature = "HpS7PBa1Agvt4OtO+wZp75IuQa0=" # will look something like that
#  if validator.validate(url, post_vars, signature):
#    print "Confirmed to have come from Twilio."
#  else:
#    print "NOT VALID.  It might have been spoofed!"

def sms_echo(arguments):
  print("sms_get_all")
  r = twiml.Response()
  pdb.set_trace()
  r.sms('Echo: ' + str(arguments))
  xml = str(r)
  pdb.set_trace()
  return HttpResponse(xml, content_type='application/xml')

def sms_get_all(arguments):
  print("sms_get_all")
  r = twiml.Response()
  pdb.set_trace()
  crops = Crop.objects.all()
  r.sms(str(crops))
  xml = str(r)
  pdb.set_trace()
  return HttpResponse(xml, content_type='application/xml')

def sms_upload(text):
  pass

COMMAND_MAP = {
  "get": sms_get_all,
  "post": sms_upload,
  "echo": sms_echo,
}

""" The Master SMS endpoint """
@csrf_exempt
def sms(request):
  print("sms()")
  print("request: " +  str(request))
  r = twiml.Response()
  print("twiml response: " + str(r))

  try:
    myMessage = request.POST['Body']
    print("myMessage: " + myMessage)
    arguments = myMessage.split(',')
    pdb.set_trace()
    command = arguments[0].lower()
    print("command: " + command)

    function = COMMAND_MAP[command]
    function(arguments)
    response = function(command)
    pdb.set_trace()
    return response
  except Exception:
    return HttpResponse("Could not process request.")

  #valid = True
  #if valid:
  #  r.sms('Thanks for inputting!')
  #else:
  #  r.sms('Invalid format. Please use this format: XXX-YYY-ZZZ')
  #xml = str(r)
  #HttpResponse(xml, content_type='application/xml')
