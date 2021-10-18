def bubble(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            aux = 0
            if(arr[i]>arr[i+1]):
                aux = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = aux

vet = [5,3,2,4,7,1,0,6]
bubble(vet)
print(vet)