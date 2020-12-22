from windrose import WindroseAxes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import gc

wd = np.random.random(500) * 360
ws = np.random.random(500) * 6

def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

def generate_figure(wd,ws,file_name):
	bins_range = np.arange(1,6,1) # this sets the legend scale
	fig,ax = plt.subplots()

	ax = WindroseAxes.from_ax()
	ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
	ax.set_legend()

	plt.savefig(file_name)

	#in case of memory leakage, which will always happen when running for many times
	plt.close('all') 
	gc.collect()


def get_angle(x,y):
	#a for the receptor and b for the pollution source
	vertical=y
	horizontal=x
	angle=0
	if(vertical>=0 and horizontal>=0):
		angle = math.atan( vertical/horizontal )
	elif(vertical>=0 and horizontal<0):
		angle = math.pi + math.atan(vertical/horizontal)
	elif(vertical<0 and horizontal>0):
		angle= 2*math.pi + math.atan(vertical/horizontal)
	else:
		angle= math.pi + math.atan(vertical/horizontal)
	return angle*180/math.pi


def get_prevailing_wind(wd,ws):
	x=0
	y=0
	for i in range(len(wd)):
		x=x+ws[i]*math.cos(math.pi*wd[i]/180)
		y=y+ws[i]*math.sin(math.pi*wd[i]/180)

	angle = get_angle(x,y)
	direction = round((angle/22.5),0)*22.5
	return direction


choice='daily' #choose one from 'daily', 'monthly' and 'seasonal'

winds={}

'''
#draw windrose for 30 years
wd_result=[]
wd_result=np.array(wd_result)
ws_result=[]
ws_result=np.array(ws_result)
for year in range(1990,2021):
	if(year==2003):
		continue
	print('30 years',year)
	#input_source='G:/GEO project/NARR wind speed and direction/'+str(year)+'.xlsx'
	input_source='G:/GEO project/navojo wind speed and direction/'+str(year)+'.xlsx'
	data = pd.read_excel(input_source)
	if(leap_year(year)):
		last_day=366
	else:
		last_day=365
	if(year==2020):
		last_day=121 #305
	
	for i in range(1,last_day+1):
		direction_header='time '+str(i)+' wind direction'
		speed_header='time '+str(i)+' wind speed'
		wd = data[direction_header].to_numpy()
		ws = data[speed_header].to_numpy()
		#print(type(wd),type(ws))
		#result.append(get_prevailing_wind(wd,ws))
		wd_result = np.concatenate((wd_result,wd),axis=None)
		ws_result = np.concatenate((ws_result,ws),axis=None)
		
		if(i<10):
			output_source='G:/GEO project/navojo windrose/'+str(year)+'-00'+str(i)+'.png'
		elif(i<100):
			output_source='G:/GEO project/navojo windrose/'+str(year)+'-0'+str(i)+'.png'
		else:
			output_source='G:/GEO project/navojo windrose/'+str(year)+'-'+str(i)+'.png'
		
		generate_figure(wd,ws,output_source)
		
	
	file=str(year)+'.txt'	
	with open(file, 'w') as filehandle:
		count=1
		for each in result:
			target='day '+str(count)+": "+str(each)
			filehandle.write(target+'\n')
			count=count+1
	
print(len(wd_result))
print(len(ws_result))

generate_figure(wd_result,ws_result,'30 years.png')


#draw 12 windrose of 30 years for each month
for month in range(1,13):
	wd_result=[]
	wd_result=np.array(wd_result)
	ws_result=[]
	ws_result=np.array(ws_result)
	for year in range(1990,2021):
		if(year==2003):
			continue
		print('30 years',year)
		#input_source='G:/GEO project/NARR wind speed and direction/'+str(year)+'.xlsx'
		input_source='G:/GEO project/navojo wind speed and direction/'+str(year)+'.xlsx'
		data = pd.read_excel(input_source)
		if(leap_year(year)):
			last_day=366
		else:
			last_day=365
		if(year==2020):
			last_day=121 #305
		if(leap_year(year)):
			start=[0,1, 32,61,92, 123,154,184,215,246,276,307,338]
			end = [0,31,60,91,122,153,183,214,245,275,306,337,366]
		else:
			start=[0,1, 32,61,92, 123,154,184,215,246,276,307,338]
			end = [0,31,59,90,121,152,182,213,244,274,305,336,365]
		if(end[month]>last_day):
			break
		for i in range(start[month],end[month]+1):
			direction_header='time '+str(i)+' wind direction'
			speed_header='time '+str(i)+' wind speed'
			wd = data[direction_header].to_numpy()
			ws = data[speed_header].to_numpy()
			#print(type(wd),type(ws))
			#result.append(get_prevailing_wind(wd,ws))
			wd_result = np.concatenate((wd_result,wd),axis=None)
			ws_result = np.concatenate((ws_result,ws),axis=None)
	output_file='month '+str(month)+'.png'
	generate_figure(wd_result,ws_result,output_file)

'''

#draw 4 windrose of 30 years for each season
for season in range(1,5):
	wd_result=[]
	wd_result=np.array(wd_result)
	ws_result=[]
	ws_result=np.array(ws_result)
	for year in range(1990,2021):
		if(year==2003):
			continue
		print('30 years',year)
		#input_source='G:/GEO project/NARR wind speed and direction/'+str(year)+'.xlsx'
		input_source='G:/GEO project/navojo wind speed and direction/'+str(year)+'.xlsx'
		data = pd.read_excel(input_source)
		if(leap_year(year)):
			last_day=366
		else:
			last_day=365
		if(year==2020):
			last_day=121 #305
		
		start=[0,1, 91, 182,273]
		end = [0,90,181,272,last_day]
		for i in range(start[season],end[season]+1):
			if(year==2020 and start[season]>90):
				break
			direction_header='time '+str(i)+' wind direction'
			speed_header='time '+str(i)+' wind speed'
			wd = data[direction_header].to_numpy()
			ws = data[speed_header].to_numpy()
			#print(type(wd),type(ws))
			#result.append(get_prevailing_wind(wd,ws))
			wd_result = np.concatenate((wd_result,wd),axis=None)
			ws_result = np.concatenate((ws_result,ws),axis=None)
	seasons=['spring.png','summer.png','fall.png','winter.png']
	output_file=seasons[season-1]
	generate_figure(wd_result,ws_result,output_file)