# Create a new file called data_presenter.py.
# Open the CupcakeInvoices.csv.
invoices = open("CupcakeInvoices.csv")

# Loop through all the data and print each row.
# for line in invoices:
#     # print(line)
# Loop through all the data and print the type of cupcakes purchased.
# for line in invoices:
#     item = line.split(',')
#     print(item[2]);
# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
invoice_total = float(0.0);
for line in invoices:
    item = line.split(',')
    quantity = int(item[3], base = 10);
    price = float(item[4]);
    order_total = price * quantity;
    print(order_total)
    invoice_total += order_total

rounded_inv = round(invoice_total, 2);
print(rounded_inv);
    # Loop through all the data, and print out the total for all invoices combined.

# Close your open file.
invoices.close();
# Challenge: Do some research and see if you can limit your floats to never exceed to characters after the decimal point