class Rover:
    def __init__(self,row,column,xCoordinate,yCoordinate,initialPosition,instructions):
        self.row=row
        self.column=column
        self.xCoordinate=xCoordinate
        self.yCoordinate=yCoordinate
        self.initialPosition=initialPosition
        self.instructions=instructions

    def rightInstruction(self,initialPosition):
        if initialPosition=='North':
            initialPosition='East'
        elif initialPosition=='East':
            initialPosition='South'
        elif initialPosition=='South':
            initialPosition='West'
        else:
            initialPosition='North'
        return initialPosition


    def leftInstruction(self,initialPosition):
        if initialPosition=='North':
           initialPosition='West'
        elif initialPosition=='West':
             initialPosition='South'
        elif initialPosition=='South':
             initialPosition='East'
        else:
             initialPosition='North'
        return initialPosition

    def move(self,initialPosition):
        if (initialPosition=='East'):
            self.xCoordinate+=1
            self.yCoordinate=self.yCoordinate
        elif initialPosition=='West':
            self.xCoordinate-=1
            self.yCoordinate=self.yCoordinate
        elif initialPosition=='North':
            self.yCoordinate+=1
            self.xCoordinate=self.xCoordinate
        else:
            self.yCoordinate-=1
            self.xCoordinate=self.xCoordinate
        return self.xCoordinate,self.yCoordinate


    def givenInstruction(self):
        initialPosition = self.initialPosition
        movedPosition=self.xCoordinate,self.yCoordinate
        for instruction in self.instructions:

            if instruction=='R':
                initialPosition=self.rightInstruction(initialPosition)
            elif instruction=='L':
                 initialPosition=self.leftInstruction(initialPosition)
            elif instruction=='M':
                movedPosition=self.move(initialPosition)
            else:
                print("enter valid input")

        return movedPosition,initialPosition
    def checkingCoordinatesOfRectangle(self):
        if self.xCoordinate<=self.row and self.yCoordinate<=self.column:
            finaloutput=self.givenInstruction()
            return finaloutput
        else:
            print("enter valid x and y coordinates")




#LMLMLMLMM
#1,2,'North','LMLMLMLMM'
#rectangleCoordinates=[5,5]
rover1=Rover(5,5,1,2,'North','LMLMLMLMM')
rover2=Rover(5,5,3,3,'East','MMRMMRMRRM')
print(rover1.checkingCoordinatesOfRectangle())
print(rover2.checkingCoordinatesOfRectangle())