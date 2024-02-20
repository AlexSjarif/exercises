# Write your code here
def cakes(eggs, butter, flour):
    ei = eggs//5
    boter = butter//250
    bloem = flour //250
    return min(ei,boter,bloem)

print(cakes(18,600,1000))
# cakes(40,400,1000)
