#Author: Jordan Ehlinger
#Assignment Number & Name: HW6 Stock Prices
#Due Date: N/A
#Program Description: Allows the user to search for a specific time period of Apple's stock price in 2019 and discover the average change as well as the highest and lowest weeks for a change in the stock price during this period.


##INPUT VALIDATION METHODS
#function to validate start week input
def check_start_week():
    start_week=-1
    while start_week < 1 or start_week > 52:
        try:
            start_week = input("Please enter the start week: ")
            if start_week == "":
                start_week = 1
                start_week = int(start_week)
                return start_week
            else:
                start_week = int(start_week)
                if start_week < 1 or start_week > 52:
                    print("The week must be between 1 and 52")
                    start_week=-1
                else:
                    return start_week
        except Exception:
            print("The week must be a valid integer between 1 and 52")
            start_week=-1

#function to validate end week input
def check_end_week():
    end_week=-1
    while end_week <= start_week or end_week > 52:
        try:
            end_week = input("Please enter the end week: ")
            if end_week == "":
                end_week = 52
                end_week=int(end_week)
                return end_week
            else:
                end_week = int(end_week)
                if end_week <= start_week or end_week > 52:
                    print("The week must be greater than the start week and between 1 and 52")
                    end_week=-1
                else:
                    return end_week
        except Exception:
            print("The week must be a valid integer between 1 and 52")
            end_week=-1


##CREATE AND FILL 2-DIMENSIONAL LIST
#initialize list
stock_price_list = []

#open the file
apple_file = open("ApplePrices.txt",'r')

#create a variable for the start week and price
week = 1
price = float(apple_file.readline())

#initialize a loop counter
i = 0

#while loop to fill out list with weeks, prices, and price change
while price != '':
    stock_price_list.append([0,0,0])
    
    stock_price_list[i][0] = week
    stock_price_list[i][1] = float(price)

    if (week == 1):
        stock_price_list[i][2] = 0
    else:
        stock_price_list[i][2] = stock_price_list[i][1] - stock_price_list[i-1][1]

    #read the next line
    price = apple_file.readline()

    #add to the counter
    i += 1

    #go to next week
    week += 1


#call on input validation functions to ask the user what weeks they want to start and end
start_week = check_start_week()
end_week = check_end_week()

#show start and end week the user has selected          
print("Start Week:", start_week)
print("End Week:", end_week)


##FIND AVERAGE, MAX, AND MIN VALUES
#adjust the weeks to the correct index number    
start_week = start_week - 1
end_week = end_week - 1

#initialize variables for loop
maxChange = 0
minChange = 0
maxIndex = 0
minIndex = 0
total = 0
count = 0

#for loop to find min and max value and their corresponding week
for j in range(start_week, end_week+1):
    #adds first change to maxChange variable and then compares each change in the range to this value, replacing the variable when the change is larger. Also creates a variable for the week the change occurred
    if stock_price_list[j][2] >= maxChange:
        maxChange = stock_price_list[j][2]
        maxIndex = j
    #adds first change to minChange variable and then compares each change in the range to this value, replacing the variable when the change is smaller. Also creates a variable for the week the change occurred
    if stock_price_list[j][2] <= minChange:
        minChange = stock_price_list[j][2]
        minIndex = j

    #add to total and count
    total += stock_price_list[j][2]
    count += 1

#calculate average
average = total /count


##DISPLAY AVERAGE, MAX, AND MIN VALUES
print ("The average change is $", format(average, '.2f'), sep='')
print ("The week with the highest change is week " , stock_price_list[maxIndex][0], " with a change of $" , format(maxChange, '.2f'), sep='')
print ("The week with the lowest change is week " , stock_price_list[minIndex][0], " with a change of $" , format(minChange, '.2f'), sep='')

#close the file
apple_file.close()
