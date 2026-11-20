import heapq
from itertools import count

def huffman_codes(frequencies):
    serial=count()
    heap=[(freq,next(serial),symbol) for symbol,freq in frequencies.items()]
    heapq.heapify(heap)
    if not heap: return {}
    while len(heap)>1:
        f1,_,left=heapq.heappop(heap); f2,_,right=heapq.heappop(heap)
        heapq.heappush(heap,(f1+f2,next(serial),(left,right)))
    codes={}
    def walk(node,prefix):
        if isinstance(node,str): codes[node]=prefix or "0"
        else: walk(node[0],prefix+"0"); walk(node[1],prefix+"1")
    walk(heap[0][2],"")
    return codes

if __name__ == "__main__":
    print(huffman_codes({"a":5,"b":9,"c":12,"d":13,"e":16,"f":45}))
