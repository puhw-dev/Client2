############################################################
#
# PUHW Client2 - a simple console client for PUHW project
#
# Author:	Pawel Zadrozniak
# version 1.01 (06/2014)
#
# note: this script requires "requests" library for Python
#
############################################################

import json
import requests
import sys
import time
import os
import base64

def anim():
	anim=[]
	anim.append("DQosLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0uDQp8byBeIF9fX19fX19fX19fX19fX19fXyAgIG98DQp8LSAuJyAgICAgJy4gICAgLicgICAgICcuIC18DQp8IC8gICAqeCogICBcICAvICAgKngqICAgXCB8DQp8IHwgICooXykqIDo6Ojo6OiAqKF8pKiAgfCB8DQp8IFwgICAqeCogICAvICBcICAgKngqICAgLyB8DQp8XHwnLiBfX19fXydfX19fJ19fX19fIC4nfC98DQp8LnwgIC8gICAgICAgb28gICAgICAgXCAgfC58DQp8bygpL19fT3xvfF9fX19fX3xvfE9fX1woKW98")
	anim.append("DQosLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0uDQp8byBeIF9fX19fX19fX19fX19fX19fXyAgIG98DQp8LSAuJyAgICAgJy4gICAgLicgICAgICcuIC18DQp8IC8gICAqKnggICBcICAvICAgKip4ICAgXCB8DQp8IHwgICooXykqIDo6Ojo6OiAqKF8pKiAgfCB8DQp8IFwgICB4KiogICAvICBcICAgeCoqICAgLyB8DQp8XHwnLiBfX19fXydfX19fJ19fX19fIC4nfC98DQp8LnwgIC8gICAgICAgb28gICAgICAgXCAgfC58DQp8bygpL19fT3xvfF9fX19fX3xvfE9fX1woKW98")
	anim.append("DQosLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0uDQp8byBeIF9fX19fX19fX19fX19fX19fXyAgIG98DQp8LSAuJyAgICAgJy4gICAgLicgICAgICcuIC18DQp8IC8gICAqKiogICBcICAvICAgKioqICAgXCB8DQp8IHwgIHgoXyl4IDo6Ojo6OiB4KF8peCAgfCB8DQp8IFwgICAqKiogICAvICBcICAgKioqICAgLyB8DQp8XHwnLiBfX19fXydfX19fJ19fX19fIC4nfC98DQp8LnwgIC8gICAgICAgb28gICAgICAgXCAgfC58DQp8bygpL19fT3xvfF9fX19fX3xvfE9fX1woKW98")
	anim.append("DQosLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0uDQp8byBeIF9fX19fX19fX19fX19fX19fXyAgIG98DQp8LSAuJyAgICAgJy4gICAgLicgICAgICcuIC18DQp8IC8gICB4KiogICBcICAvICAgeCoqICAgXCB8DQp8IHwgICooXykqIDo6Ojo6OiAqKF8pKiAgfCB8DQp8IFwgICAqKnggICAvICBcICAgKip4ICAgLyB8DQp8XHwnLiBfX19fXydfX19fJ19fX19fIC4nfC98DQp8LnwgIC8gICAgICAgb28gICAgICAgXCAgfC58DQp8bygpL19fT3xvfF9fX19fX3xvfE9fX1woKW98")
	s=len(anim)
	for x in range(0,5):
		for n in range(0,s):
			os.system('cls' if os.name == 'nt' else 'clear')
			print '\n          Loading PUHW console...'
			print base64.b64decode(anim[n]).replace("\n","\n".ljust(10))
			print '\n          Please do not eject the tape.'
			time.sleep(0.05)
	os.system('cls' if os.name == 'nt' else 'clear')

def json_get(url):
	r = requests.get(url, timeout=3)
	data=json.loads(r.text)
	return data;

def get_hosts(mon_url):
	try:
		d=json_get(mon_url+'/hosts');
		hosts=[]
		for host in d['hosts']:
			hosts.append(host['hostname'])
			return hosts
	except:
		return False
		
def get_sensors(mon_url,host):
	try:
		d=json_get(mon_url+'/hosts/'+host+'/sensors')
		sensors=[]
		for sensor in d['sensors']:
			sensors.append(sensor['sensorname'])
		return sensors
	except:
		return False

def get_metrics(mon_url,host,sensor):
	try:
		d=json_get(mon_url+'/hosts/'+host+'/sensors/'+sensor+'/metrics')
		metrics=[]
		for metric in d['metrics']:
			metrics.append(metric['name'])
		return metrics
	except:
		return False

def get_metric(mon_url,host,sensor,metric,count):
	try:
		count=int(count)
		d=json_get(mon_url+'/hosts/'+host+'/sensors/'+sensor+'/metrics/'+metric+'/data?n='+str(count))
		#print d['metrics'][2]['data']
		return d['metrics'][2]['data']
	except:
		return False;

def puhw_print(mon_url):
	hosts = get_hosts(mon_url)
	if not isinstance(hosts,list):
		print "\nCould not retrieve host list.\nCheck the monitor address."
		return
	for host in hosts:
		print 'HOST:',host
		sensors = get_sensors(mon_url,host)
		for sensor in sensors:
			print "\tSENSOR:",sensor
			metrics=get_metrics(mon_url,host,sensor)
			for metric in metrics:
				data=get_metric(mon_url,host,sensor,metric,1)
				print "\t\tMETRIC:",metric,"\t\tVAL:",data[0].values()[0]

def header():
	os.system('cls' if os.name == 'nt' else 'clear')
	sys.stdout.write(''.ljust(8,"\xdb")+"\xb2\xb2\xb1\xb1\xb0\xb0"+' PUHW console '+"\xb0\xb0\xb1\xb1\xb2\xb2"+''.ljust(45,"\xdb")+"\n")
def puhw_display(mon_url,sensor,metric):
	hosts = get_hosts(mon_url)
	if not isinstance(hosts,list):
		header()
		print "\nCould not retrieve host list.\nCheck the monitor address."
		return
	valid={}
	invalid=[]
	for host in hosts:
		data=get_metric(mon_url,host,sensor,metric,1)
		if (data==False):
			invalid.append(host)
		else:
			valid[host]=data[0].values()[0]
	valid_s=[]
	#try numeric sort
	try:
		valid_c={}
		for host in valid.keys():
			valid_c[host]=float(valid[host])
		valid_s = sorted(valid_c, key=valid_c.__getitem__)
	except:
		#numeric sort failed - sort strings
		valid_s = sorted(valid, key=valid.__getitem__)
	
	host_column=50
	header()
	print '====[ METRIC: '+ (sensor+'\\'+metric)[0:40].ljust(40) +' ]=====[ HOSTS: '+str(len(hosts))[0:4].ljust(4)+' ]==='
	print ''
	for host in valid_s:
		sys.stdout.write('+ '+host[0:host_column].ljust(host_column+1)+valid[host]+"\n")
	if len(valid): print ' '
	for host in invalid:
		sys.stdout.write('+ '+host[0:host_column].ljust(host_column+1)+"Invalid sensor/metric\n")
	sys.stdout.flush()

def usage():
	print "PUHW console client\nUSAGE:\n\tpuhwclient.py <MONITOR> - lists all available hosts and sensors\n\tpuhwclient.py <MONITOR> <SENSOR> <METRIC> [TIME] -\n\t      - displays information in [TIME] interval"

argc=len(sys.argv)
if (argc<2 or argc==3):
	usage()
	exit()

MONITOR='89.68.69.22:8889'
SENSOR="Sensor SysLoad-1"
METRIC="cpuUtilization"

monitor=sys.argv[1].replace('/','')
sensor=''
metric=''

interval=5
if argc>=4:
	sensor =sys.argv[2].replace('/','')
	metric =sys.argv[3].replace('/','')
	if monitor=='':
		print 'Invalid monitor address.'
		exit(-1)
	if sensor=='':
		print 'Invalid sensor name.'
		exit(-1)
	if metric=='':
		print 'Invalid metric name.'
		exit(-1)
	if argc>=5:
		try:
			print 'II'
			interval=int(sys.argv[4])
			if interval<1 or interval>999: raise 1
		except:
			interval=5
			print 'Warning: invalid interval value. Using defailt:',interval


#sensor=SENSOR
#metric=METRIC
mon_url='http://'+monitor
print 'Connecting to monitor: '+mon_url+'...'

if (sensor==''):
	puhw_print(mon_url)
	exit()

anim()

while(1):
	try:
		sys.stdout.write('   ===[ working... ]===')
		sys.stdout.flush()
		puhw_display(mon_url,sensor,metric)
		time.sleep(interval)
	except KeyboardInterrupt:
		exit(0)
	
exit()




