'''7.  Replace Defective Product Code Task:

-   Create an integer array with 10 product codes.
-   Replace every occurrence of 0 with 999.
-   Print the updated array.'''

product_codes = [10,500,1000,99,0,20,25,45,0,10]

print("Original Product code", product_codes)

for i in range (10):
    if product_codes[i] == 0:
        product_codes[i] = 999

print("Updated Product code =", product_codes)