"""Generate sales report showing total melons each salesperson sold."""

# initiate empty lists to keep track of sales people and melons_sold
salespeople = []
melons_sold = []

# open the sales report text and save variable f
f = open('sales-report.txt')
# loop through each line of text in the sales report, divide the text in increments of |
#assing sales person's name using the index number of the word and do the same for the number of melons
# if the sales person is in the list, assign the number of mellons they's sold to the appropriate index in 
# melons sold, for names not yet on the list add their name and melons sold to the lists above. 
# loop through the index of the list and print the sales person's name and number of melon's sold. 
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
