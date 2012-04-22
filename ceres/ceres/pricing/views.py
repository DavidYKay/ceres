# Create your views here.

import pdb;
import random;

from django.views.generic.simple import direct_to_template
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

''' Utilities '''

def array_to_string(array, separator=', '):
  return separator.join(map(str, array))

def string_to_crop(cropName):
  return Crop.objects.get(name__iexact=cropName)

def string_to_department(departmentName):
  return Department.objects.get(name__iexact=departmentName)

def textToSmsXmlResponse(text):
  r = twiml.Response()
  r.sms(text)
  xml = str(r)
  return HttpResponse(xml, content_type='application/xml')

''' Defaults '''

def unknown_command():
  commands = array_to_string(COMMAND_MAP.keys())
  helpMessage = "I didn't understand. Please use one of the following commands: " + commands
  return textToSmsXmlResponse(helpMessage)

''' Views '''

def home(request):
  #return direct_to_template(request, {'template': 'anything.html'})
  return direct_to_template(request, 'anything.html')

def crop_ajax(request):
  responseString = str(random.random())
  return HttpResponse(responseString)

def sms_echo(arguments):
  print("sms_get_all()")
  return textToSmsXmlResponse('Echo: ' + str(arguments))

def sms_help(arguments):
  print("sms_help()")
  helpText = '''
    get crop [maize|papaya|yucca]
    get department [Boaco|Chinandega|Carazo]
    post maize boaco 8
  '''
  return textToSmsXmlResponse('Commands: ' + helpText)

def get_best_prices_for_crop(cropName):
  print("get_best_prices_for_crop")
  crop = string_to_crop(cropName)
  priceReports = PriceReport.objects.filter(crop=crop).order_by('-price')[:5]

  priceStrings = map(PriceReport.department_first, priceReports)
  priceString = array_to_string(priceStrings, separator=' | ')
  return textToSmsXmlResponse(priceString)

def get_best_crops_in_department(departmentName):
  print("get_best_prices_for_department")
  department = string_to_department(departmentName)

  priceReports = PriceReport.objects.filter(department=department).order_by('-price')[:5]
  priceStrings = map(PriceReport.crop_first, priceReports)
  priceString = array_to_string(priceStrings, separator=' | ')

  #return textToSmsXmlResponse('Best prices in %s: %s' % (str(department),priceString))
  return textToSmsXmlResponse("Prices in %s: %s" % (str(department), priceString))

def list_crops():
  print("sms_get_all")
  crops = Crop.objects.all()
  return textToSmsXmlResponse(array_to_string(crops))

def sms_get(arguments):
  print("sms_get")
  #pdb.set_trace()
  if (arguments[1].lower() == 'crop'):
    return get_best_prices_for_crop(arguments[2])
  elif (arguments[1].lower() == 'department'):
    return get_best_crops_in_department(arguments[2])
  else:
    return unknown_command()

def sms_upload(arguments):
  assert len(arguments) >= 4
  crop       = string_to_crop(arguments[1])
  department = Department.objects.get(name__iexact=arguments[2])
  price      = int(arguments[3]) * 100
  report = PriceReport(
      crop=crop,
      department=department,
      price=price,

      submitter=None,
      price_type='local',
      )
  try:
    report.save()
    #pdb.set_trace()
    return textToSmsXmlResponse("Saved report successfully: " + str(report))
  except Exception:
    return textToSmsXmlResponse("Could not SAVE request.")

COMMAND_MAP = {
  "get": sms_get,
  "post": sms_upload,
  "echo": sms_echo,
  "commands": sms_help,
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
    #arguments = myMessage.split(',')
    arguments = myMessage.split(' ')
    command = arguments[0].lower()
    print("command: " + command)

    #pdb.set_trace()
    function = COMMAND_MAP[command]
    response = function(arguments)
    return response
  except Exception:
    return unknown_command()

  #valid = True
  #if valid:
  #  r.sms('Thanks for inputting!')
  #else:
  #  r.sms('Invalid format. Please use this format: XXX-YYY-ZZZ')
  #xml = str(r)
  #HttpResponse(xml, content_type='application/xml')
