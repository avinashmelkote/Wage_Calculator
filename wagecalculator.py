# Compute weekly pre-tax earnings including potential overtime pay.
# Catch exceptions with try and except

def computepay(hours, rate):
	if hours > 40:
		pay = (40 * rate) + (hours-40)*rate*1.5
		return pay
	elif hours <= 40:
		pay = hours * rate
		return pay

try:
	hours = raw_input('Enter Hours: ')
	hours = float(hours)
	rate = raw_input('Enter Rate: ')
	rate = float(rate)
except:
	print 'Error, please enter numeric input'

pay = computepay(hours, rate)

print 'Your weekly pre-tax earnings are:', pay

if hours > 40:
	print 'You are eligible for overtime pay of','$',(hours-40)*rate*1.5,'for',(hours-40),'hours above 40 this week.'
else:
	print 'You are not eligible for overtime pay because you did not work over 40 hours this week.'

