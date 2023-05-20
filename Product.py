class Product:

    name = ""
    price = 0
    quantity=0
    giftwrap=False
    
class Discount:

    name = ""
    price = 0

totalQty = 0
totalprice = 0
flat_10_discount = 0
bulk_5_discount = 0
bulk_10_discount = 0
tiered_50_discount = 0
shippingFee = 0
giftWrapFee = 0



productA = Product()
productB = Product()
productC = Product()

productA.name = "Product A"
productA.price = 20

productB.name = "Product B"
productB.price = 40

productC.name = "Product C"
productC.price = 60

products=[]
products.append(productA)
products.append(productB)
products.append(productC)

for product in products:
    product.quantity=int(input("Quantity of "+product.name +" : "))                       
    product.giftwrap=input("Do you want it wrapped as a gift? True or False? : ")
    totalprice = totalprice + product.quantity * product.price
    totalQty = totalQty + product.quantity
    if product.quantity > 10:
        bulk_5_discount = bulk_5_discount + totalprice * 0.05
    if product.giftwrap:
        giftWrapFee = giftWrapFee + product.quantity

if totalprice > 200:
    flat_10_discount = 10
    
if totalQty > 20:
    bulk_10_discount = totalprice*0.1

 
for product in products:
    if totalQty > 30 & product.quantity > 15:
        remainingQty = product.quantity - 15
        tiered_50_discount = tiered_50_discount + 0.5*remainingQty*product.price
                  
bulk_10_dis = Discount()
bulk_10_dis.name = "bulk_5_discount"
bulk_10_dis.price = bulk_10_discount

flat_10_dis = Discount()
flat_10_dis.name = "flat_10_discount"
flat_10_dis.price = flat_10_discount

bulk_5_dis = Discount()
bulk_5_dis.name = "bulk_5_discount"
bulk_5_dis.price = bulk_5_discount

tiered_50_dis = Discount()
tiered_50_dis.name = "tiered_50_discount"
tiered_50_dis.price = tiered_50_discount

discounts = [bulk_10_dis,tiered_50_dis,flat_10_dis,bulk_5_dis]
largestDiscount = Discount()

for discount in discounts:
    if discount.price > largestDiscount.price:
        largestDiscount = discount;
        
shippingFee = int(totalQty/10) * 5

if totalQty%10 != 0:
    shippingFee = shippingFee+5

for product in products:
        print("Product name: ", product.name," | Price: ",product.price ," | Quantity:",product.quantity)
    
print("Subtotal: ", totalprice);
print("Discount name :  ",largestDiscount.name, " | Discount price",largestDiscount.price)
print("Shipping Fee :",shippingFee);
print("Giftwrap Fee :", giftWrapFee);
print("Total : " , totalprice - largestDiscount.price + shippingFee + giftWrapFee) 
     
    



