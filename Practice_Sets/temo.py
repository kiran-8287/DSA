def mergesort(merged):
    if len(merged)<=1 :
        return merged
    
    mid = len(merged)//2
    s1,s2 = merged[:mid],merged[mid:]
    print(f"Divide : {merged} -> {s1} and {s2}")
    s1 = mergesort(s1)
    s2 =mergesort(s2)
    
    merged,m = merge(s1,s2)
    print(f"merge : {s1} and {s2} --> {merged}  (comparisons : {m})")

    return merged

def merge(a,b):
    s = []
    comp =[]
    i,j = 0,0
    while i < len(a) and j <len(b) :
        if a[i] < b[j]:
            comp.append(f"{a[i]} < {b[j]}")
            s.append(a[i])
            i +=1
        else:
            s.append(b[j])
            comp.append(f"{a[i]} > {b[j]}")
            j+=1
    while i < len(a):
        s.append(a[i])
        i+=1
        
    while j< len(b):
        s.append(b[j])
        j+=1
    return s,",".join(comp)

def final(s):
    m = mergesort(s)
    print(f"sorted array : {m}")
    print("time complexity : O(nlogn) ,space : o(n)")

s= [38, 27, 43, 3, 9, 82, 10]
final(s)