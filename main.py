import httpx

lista=[]
i = 1

while(i <=5):
    params = {'id': str(i)}
    dicelemento = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
    dic = (dicelemento.json())[0]
    lista.append(dic)
    i = i+1

print(lista)