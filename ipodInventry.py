class Ipods:
    def __init__(self,country,quantityOfIpods,prize):
        self.country=country
        self.quantityOfIpods=quantityOfIpods
        self.prize=prize
brazil=Ipods('brazil',100,100)
argentina=Ipods('argentina',100,50)
country='argentina'
ipod=300

if country=='brazil' and (ipod>=10 and ipod%10==0):
    if ipod<=100:
        costOfIpod=ipod*brazil.prize
        brazil.quantityOfIpods-=ipod
        print(costOfIpod, ":", brazil.quantityOfIpods, ':', argentina.quantityOfIpods)
    elif ipod<=200:
        ipodsRequiredFromArgentina=ipod-brazil.quantityOfIpods
        costOfIpodInBrazil=100*brazil.prize
        costOfIpodInArgentina=(ipodsRequiredFromArgentina*argentina.prize)+((ipodsRequiredFromArgentina//10)*400)
        costOfIpod=costOfIpodInArgentina+costOfIpodInBrazil
        brazil.quantityOfIpods=0
        argentina.quantityOfIpods-=ipodsRequiredFromArgentina
        print(costOfIpod, ":", brazil.quantityOfIpods, ':', argentina.quantityOfIpods)
    else:
        print('out of stock')
elif country=='argentina' and (ipod%10==0):
    if ipod<=100:
        costOfIpod=ipod*argentina.prize
        argentina.quantityOfIpods-=ipod
        print(costOfIpod, ":", brazil.quantityOfIpods, ':', argentina.quantityOfIpods)
    elif ipod<=200:
        ipodsRequiredFromBrazil=ipod-argentina.quantityOfIpods
        costOfIpodInArgentina=100*argentina.prize
        costOfIpodInBrazil=(ipodsRequiredFromBrazil*brazil.prize)+((ipodsRequiredFromBrazil//10)*400)
        costOfIpod=costOfIpodInArgentina+costOfIpodInBrazil
        argentina.quantityOfIpods=0
        brazil.quantityOfIpods-=ipodsRequiredFromBrazil
        print(costOfIpod, ":", brazil.quantityOfIpods, ':', argentina.quantityOfIpods)
    else:
        print('out of stock')
else:
    print("enter valid input")


