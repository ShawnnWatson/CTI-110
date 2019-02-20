# This program a sales prediction based on total sales
# 02/11/2018
# CTI-110 P2T1 - Sales Prediction
# Shawnn Watson


# Total sales input

total_sales = float(input('Enter the projected sales:'))

# Calculates the profit as 23 percent of the total sales

profit = total_sales * 0.23

# Displays the profit

print('The profit is $', format(profit, ',.2f'))
