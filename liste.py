# Programme qui affiche une liste de 0 à n-1 (à définir)

def simple_range(n):
    l = []
    i = 0
    
    while i < n:
        l.append(i)
        i += 1
        
    return l

print(simple_range(10))