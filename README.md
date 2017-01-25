# Wage_Calculator
# Here is a calculator of your total weekly wages including overtime of 1.5*(hourly wage) for every hour over 40 hours. The final output specifies the number of hours worked overtime, along with the amount of money specifically dedicated to overtime pay. 
hours  = raw_input('Enter the number of hours you have worked this week: ')
rate = raw_input('Enter your hourly wage rate: ')
hours = float(hours)
rate = float(rate)
if hours > 40:
	try: 
		weeklypay = (40 * rate) + ((hours-40) * 1.5 * rate)
		print weeklypay
		overtime = (hours-40) * 1.5 * float(rate)
		print 'Your total pay for the week is:','$',weeklypay
		print 'This includes','$',overtime,'for',(hours-40), 'hours worked overtime.'
	except: 
		print 'Please enter a numerical value for both options.'
elif hours <= 40:
	try: 
		weeklypay = hours * float(rate)
		print 'Your total pay for the week is:','$',weeklypay
		print 'You are not eligibile for overtime pay because you worked less than 40 hours this week.'
	except: 
		print 'Please enter a numerical value for both options.'
