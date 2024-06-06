class KnapSack_UnlimitedItems:
    def __init__(self) -> None:
        self.items = []
        self.Nitems = 0
        self.SelectedItems = []
        self.DParray = []
        self.ComparisonCount = 0
    def addItem(self, weight, profit):
        self.items.append(dict({"weight": weight, "profit": profit}))
        self.Nitems += 1
    def max(self, a, b, Weight, ItemIndex):
        self.ComparisonCount += 1
        if (a>=b):
            return a
        self.SelectedItems[Weight] = (ItemIndex+1)
        return b
    def ComparisonsTotal(self):
        return self.ComparisonCount
    def ItemsChosenAtWeights(self):
        return (self.SelectedItems)
    def getSelectedItems(self, weight = -1):
        if (weight==-1):
            weight = len(self.SelectedItems)-1
        selected = []
        while (weight > 0):
            selected_item = self.SelectedItems[weight]
            if (selected_item > 0):
                selected.append(selected_item)
                weight -= self.items[selected_item-1]["weight"]
            else:
                weight -= 1
        return selected
    def NoDP_Recursive(self, weight, n=-1):
        if (n==-1):
            n = self.Nitems
        self.SelectedItems = [-1 for i in range(weight+1)]
        self.SelectedItems[0] = 0
        return self.PurelyRecursive(weight, n)
    def PurelyRecursive(self, Weight, NumItems):
        if (NumItems < 0 or Weight < 0):
            return -1
        if (NumItems == 0 or Weight == 0):
            return 0
        max_profit = 0
        for item_index in range(NumItems):
            maxProfit_i = self.PurelyRecursive(Weight-self.items[item_index]["weight"], NumItems)
            if (maxProfit_i == -1):
                continue
            max_profit = self.max(max_profit, (maxProfit_i + self.items[item_index]["profit"]), Weight, item_index)
        return max_profit
    def DPBottomUp(self, weight, n=-1):
        if (n==-1):
            n = self.Nitems
        aug_weight = weight+1    
        
        self.SelectedItems = [-1 for i in range(aug_weight)]
        self.SelectedItems[0] = 0

        self.DParray = [-1 for i in range(aug_weight)]
        self.DParray[0] = 0
        
        for possibleWeight in range(aug_weight):
            maxProfit = 0
            itemIndex = -1
            for item in range(n):
                remainderWeight = possibleWeight-self.items[item]["weight"]
                if (remainderWeight < 0): 
                    continue
                possibleProfit = self.DParray[remainderWeight] + self.items[item]["profit"]
                self.ComparisonCount += 1
                if (possibleProfit > maxProfit):
                    maxProfit = possibleProfit
                    itemIndex = item
            self.SelectedItems[possibleWeight] = (itemIndex+1)
            self.DParray[possibleWeight] = maxProfit
        return self.DParray[weight]