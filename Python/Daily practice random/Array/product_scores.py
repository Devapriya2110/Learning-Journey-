'''6.  Count Failed Products Task:

-   Create an integer array with test scores of 10 products.
-   Count how many products scored below 40.
-   Print the total failed products.'''

product_scores = [60,35,30,25,70,100,25,35,20,40]

print("Product scores:",product_scores)

count=0
for i in range (10):
    if product_scores[i]<40:
        count +=1

print("Failed products =",count)