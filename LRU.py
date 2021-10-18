from fractions import Fraction

input_arr = [1, 2, 1, 3, 1, 4, 2, 4, 1, 2, 3, 1, 2, 4, 1, 4, 2, 3]
k = 3
cache={}
cost = 0
for i in range(len(input_arr)):
    out=0
    out_key=0
    if len(cache.items())<k and input_arr[i] not in cache.keys():
        pass
        cost+=1
    elif input_arr[i] not in cache.keys():
        for key, value in cache.items():
            if out<value:
                out=value
                out_key=key
        del cache[out_key]
        cost+=1
    for key, value in cache.items():
        cache[key]+=1
    cache[input_arr[i]]=0
    print(f'Input: {input_arr[i]} \t Kivettem: {out_key if out_key!=0 else "-"} \tA cache most: {[i for i in cache.keys()]}')

print(f'\nA költségem {cost} lett.')

cache=set()
opt=0
for i in range(len(input_arr)):
    out=0
    out_key=0
    if len(cache)<k:
        pass
        opt+=1
    elif input_arr[i] not in cache:
        dist=0
        for key in cache:
            out_i = 0
            for j in range(i, len(input_arr)):
                out_i+=1
                if input_arr[j] == input_arr[i]:
                    break
            if out_i>out:
                out_key = key
        cache.discard(out_key)
        opt+=1
    cache.add(input_arr[i])

print(f'Az optimum {opt}, mindig azt vettem ki, amelyik legkésőbb következne.')
print(f'Az LRU versenyképessége tehát ezen az inputon: {Fraction(cost, opt)}')


    

    
