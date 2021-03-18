class Hotel:
    def __init__(self,star,weekDayRegularPrize,weekEndRegularPrize,weekDayRewardiePrice,weekEndRewardiePrize):
        self.star=star
        self.weekDayRegularPrize=weekDayRegularPrize
        self.weekEndRegularPrize =weekEndRegularPrize
        self.weekDayRewardiePrice =weekDayRewardiePrice
        self.weekEndRewardiePrize =weekEndRewardiePrize

hotelX=Hotel(star=3,weekDayRegularPrize=100,weekEndRegularPrize=120,weekDayRewardiePrice=90,weekEndRewardiePrize=60)
hotelY=Hotel(star=5,weekDayRegularPrize=130,weekEndRegularPrize=150,weekDayRewardiePrice=100,weekEndRewardiePrize=95)
hotelZ=Hotel(star=4,weekDayRegularPrize=195,weekEndRegularPrize=150,weekDayRewardiePrice=120,weekEndRewardiePrize=90)




def prizeComparisionAfterFindingUserType():
    if (prizeForX < prizeForY) and (prizeForX < prizeForZ):
        print('hotelX', prizeForX)
    elif (prizeForX > prizeForY) and (prizeForY < prizeForZ):
        print('hotelY', prizeForY)
    else:
        print('hotelZ', prizeForZ)
n=3
#threeDaysPrizeList=[]

while n>0:
    userType = input("enter regular or rewardie:").lower()
    userDate = input("enter date eg.14/02/2021(sun):")
    enteredDayByUser = userDate[11:len(userDate) - 1]
    weekDay = ['mon', 'tues', 'wed', 'thurs', 'fri']
    weekEnd = ['sat', 'sun']
    if enteredDayByUser in weekDay:
       if userType=='regular':
          prizeForX=hotelX.weekDayRegularPrize
          prizeForY=hotelY.weekDayRegularPrize
          prizeForZ=hotelZ.weekDayRegularPrize
          prizeComparisionAfterFindingUserType()
       elif userType=='rewardie':
          prizeForX = hotelX.weekDayRewardiePrice
          prizeForY = hotelY.weekDayRewardiePrice
          prizeForZ = hotelZ.weekDayRewardiePrice
          prizeComparisionAfterFindingUserType()
       else:
           print("enter valid input")

    elif enteredDayByUser in weekEnd:
       if userType=='regular':
          prizeForX=hotelX.weekEndRegularPrize
          prizeForY=hotelY.weekEndRegularPrize
          prizeForZ=hotelZ.weekEndRegularPrize
          prizeComparisionAfterFindingUserType()

       elif userType=='rewardie':
           prizeForX = hotelX.weekEndRewardiePrize
           prizeForY = hotelY.weekDayRewardiePrice
           prizeForZ = hotelZ.weekEndRewardiePrize
           prizeComparisionAfterFindingUserType()
       else:
           print("enter valid input")
    else:
        print("enter valid input outside if")
    n-=1