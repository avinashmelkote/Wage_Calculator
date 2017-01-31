#Calculate weekly pre-tax earnings including 1.5*wage for each hour above 40.
hours = raw_input('Enter the number of hours you worked this week: ')
rate = raw_input('Enter your hourly rate of pay: ')
if hours <= 40:
	try:
		pay = float(hours) * float(rate)
		print 'Your total pre-tax earnings this week are:','$',pay
	except:
		print 'Please enter a numeric input in both fields.'
		quit()
elif hours > 40:
	try:
		pay = 40*float(rate) + (float(hours)-40)*1.5*float(rate)
		print 'Your total pre-tax earnings this week are:','$',pay
		print 'You are eligible for overtime pay of','$',(float(hours)-40)*1.5*float(rate),'for',(float(hours)-40), 'hours in excess of 40 hours this week.'
	except:
		print 'Please enter a numeric input in both fields.'
		quit()
