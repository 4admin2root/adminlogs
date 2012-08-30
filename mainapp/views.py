from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
import Image,ImageDraw
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib
import StringIO,Image
from  mainapp.models import syslog_AH_505_ICP_WJ_SEV3 

############3
def line_chart_fs(request):
 t = get_template('line_chart_fs.html')
 fs_list = syslog_AH_505_ICP_WJ_SEV3.objects.filter(type='OS',item1='df',item2='/data')
 html = t.render(Context({'teststring':fs_list}))
 return HttpResponse(html)
