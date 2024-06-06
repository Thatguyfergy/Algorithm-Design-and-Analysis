from Proj3_KnapSack import KnapSack_UnlimitedItems

def KnapSack_q1(weight):
    ks = KnapSack_UnlimitedItems()
    ks.addItem(4,7)
    ks.addItem(6,6)
    ks.addItem(8,9)
    print(ks.items)
    print(f"Profit: {ks.NoDP_Recursive(weight)}")
    return (ks.ComparisonsTotal(), ks.getSelectedItems(), ks.ItemsChosenAtWeights())

def KnapSack_q4a(weight):
    ks = KnapSack_UnlimitedItems()
    ks.addItem(4,7)
    ks.addItem(6,6)
    ks.addItem(8,9)
    print(ks.items)
    print(f"Profit: {ks.DPBottomUp(weight)}")
    return (ks.ComparisonsTotal(), ks.getSelectedItems(), ks.ItemsChosenAtWeights(), ks.DParray)
    
def KnapSack_q4b(weight):
    ks = KnapSack_UnlimitedItems()
    ks.addItem(5,7)
    ks.addItem(6,6)
    ks.addItem(8,9)
    print(ks.items)
    print(f"Profit: {ks.DPBottomUp(weight)}")
    return (ks.ComparisonsTotal(), ks.getSelectedItems(), ks.ItemsChosenAtWeights(), ks.DParray)
