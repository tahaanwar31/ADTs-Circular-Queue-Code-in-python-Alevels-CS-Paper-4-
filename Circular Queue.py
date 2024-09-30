global QueueArray
global HeadPointer
global TailPointer
global NumberOfTimes
QueueArray=[0]*10
HeadPointer=-1
TailPointer=0
NumberOfItems=0
def Enqueue(Data):
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfTimes
    if NumberOfTimes>=9:
        print("Queue is full")
    else:
        QueueArray[TailPointer]=Data
        NumberOfTimes=NumberOfTimes+1
        if TailPointer>=9:
            TailPointer=0
        else:
            TailPointer=TailPointer+1
def Dequeue():
    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfTimes
    if NumberOfTimes==0:
        print("Queue is empty")
    else:
        item=QueueArray[HeadPointer]
        HeadPointer=HeadPointer+1
        NumberOfTimes=NumberOfTimes-1
        if HeadPointer>=9:
            HeadPointer=0



