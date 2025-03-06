class is_rectangle:
    def __init__(self,height,base):
        self.height=height
        self.base=base
        right_side=height
        if right_side == base and right_side==height:
            print("**Triange is an rectangle**")
        else:
            print("**Triangle Not an rectangle**")


def Quicksort(list):
    if len(list) < 1:
        return list
    else:
        pivot=list[0]
        lesser=[x for x in list[1:] if x <= pivot]
        greater=[x for x in list[1:] if x > pivot]
        return Quicksort(lesser) + [pivot] + Quicksort(greater)