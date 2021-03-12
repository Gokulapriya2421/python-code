class Sales:
    def __init__(self,product,costOfTheProduct,productType):
        self.product=product
        self.costOfTheProduct=costOfTheProduct
        self.productType=productType
def purchase():
    product=input("enter the product name:").lower()
    costOfTheProduct=eval(input("enter cost of the product:"))
    productType=input("enter whether the product is local or imported:").lower()
    global userEntry
    userEntry=Sales(product,costOfTheProduct,productType)
    return userEntry
NotaxProducts=['book','food','medical']
def findingCost():
    if userEntry.product in NotaxProducts :
        totalCostWithoutTax=userEntry.costOfTheProduct
        totalTax=0
        totalCostWithTax=totalCostWithoutTax+(totalTax*totalCostWithoutTax)
        print("TotalCost=",totalCostWithTax,"TotalTax=",totalTax,"TotalCostWithoutTax=",totalCostWithoutTax)
    elif (userEntry.product not in NotaxProducts) and (userEntry.productType == 'import'):
        totalCostWithoutTax=userEntry.costOfTheProduct
        Tax=0.1*totalCostWithoutTax
        additionalSalesTax=0.05*totalCostWithoutTax
        totalTax=Tax+additionalSalesTax
        totalCostWithTax=totalCostWithoutTax+totalTax
        print("TotalCost=",totalCostWithTax,"TotalTax=",totalTax,"TotalCostWithoutTax=",totalCostWithoutTax)
    else:
        totalCostWithoutTax=userEntry.costOfTheProduct
        totalTax=0.1*totalCostWithoutTax
        totalCostWithTax=totalCostWithoutTax+totalTax
        print("TotalCost=",totalCostWithTax,"TotalTax=",totalTax,"TotalCostWithoutTax=",totalCostWithoutTax)
purchase()
findingCost()

