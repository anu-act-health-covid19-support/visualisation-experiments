
func = lambda x:1.0/(x**2+1)

data1 = []
for x in range(30):
	if len(str(x+1))==0:
		data1.append({"value":70*func(x-10) + 90*func((x-30)*0.3), "date":"2020-04-0{}".format(x+1), "l":50*func(x-10) + 60*func((x-30)*0.3), "u":80*func((x-11)*0.7) + 160*func((x-31)*0.3)})
	else:
		data1.append({"value":70*func(x-10) + 90*func((x-30)*0.3), "date":"2020-04-{}".format(x+1), "l":50*func(x-10) + 60*func((x-30)*0.3), "u":80*func((x-11)*0.7) + 160*func((x-31)*0.3)})

for d in data1:
	if d['l']>=d['value']:
		d['l'] = d['value']
	if d['u']<=d['value']:
		d['u']=d['value']

import json

print(json.dumps(data1))


print("")

data1 = []
for x in range(30):
	if len(str(x+1))==0:
		data1.append({"value":110*func(x-8) + 90*func((x-30)*0.1), "date":"2020-04-0{}".format(x+1), "l":80*func(x-8) + 60*func((x-30)*0.1), "u":150*func((x-9)*0.7) + 160*func((x-31)*0.1)})
	else:
		data1.append({"value":110*func(x-8) + 90*func((x-30)*0.1), "date":"2020-04-{}".format(x+1), "l":80*func(x-8) + 60*func((x-30)*0.1), "u":150*func((x-9)*0.7) + 160*func((x-31)*0.1)})

for d in data1:
	if d['l']>=d['value']:
		d['l'] = d['value']
	if d['u']<=d['value']:
		d['u']=d['value']


print(json.dumps(data1))
