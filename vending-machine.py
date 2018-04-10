from byotest import *

eur_coins = {
    1:20, 
    2:20, 
    5:20, 
    10:20, 
    20:20, 
    50:20, 
    100:20
}

def get_change(amount, coins=eur_coins):
    change = []
    for coin in reversed(sorted(coins.items())):
            while coin[0] <= amount and eur_coins[coin[0]] > 0:
                amount -= coin[0]
                eur_coins[coin[0]] -= 1
                change.append(coin[0])
            
        
            
            
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(9), [5,2,2])

print("All tests passed")
print(eur_coins)