# The purpose of this project is to write a program that asks the user to enter the projected amount of total
# sales and then displays the profit that will be made from that amount
# 25September2018
# CTI-110 P2T1 - Sales Prediction
# Karina Smith
#

#Get projected total sales
#Input the total sales
total_sales = float(input("Enter the projected sales: "))
#Calculate the profit as 23 percent of total sales
profit = total_sales *0.23
#Display the profit
print("The profit is $", format(profit, ",.2f"))
