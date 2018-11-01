import sys

import time





COINS = [1, 2, 5, 10, 20 ,50 ,100, 200]

def coins_comb(target = 200):
    combs =[1] + [0]*target
    for coin in COINS:
        for j in range(coin, target + 1):
            combs[j] += combs[j-coin]
        print(combs)

    return combs




if __name__ == '__main__':
    


    timer = time.time()
    print(coins_comb(int(sys.argv[1])))
    print("total time: "+ str(time.time() - timer) + " s")

