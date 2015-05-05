""" Tip Calculator
Prompts user to enter entire amount of restaurant bill, including the tax.
It then asks how the service was and suggests a tip amount.
"""

#receive user input

meal = float(input("How much was your meal, including tax? "))
service = str(input("How was your service? bad; average; good: excellent "))

#assign tip percentage based on user input

if service.lower() == "bad":
    tip = float(.08)
else:
    if service.lower() == "average":
        tip = float(.15)
    else:
         if service.lower() == "good":
             tip = float(.20)
         else:
             if service.lower() == "excellent":
                 tip = float(.25)

#calculate tip and total
                 
tip_suggestion = meal * tip
total = tip_suggestion + meal


    print('Because you received ' + service + ' service, the correct tip would be $'\
        + str(round(tip_suggestion,2)) +', bringing your total to $' + str(round(total,2)) + '.')
    


