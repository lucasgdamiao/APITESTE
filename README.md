# Teste da api

# Objetivo
O código deste arquivo foi feito como resposta do teste informado, sua resolução está na folha "main.py" que deve ser executada.
Ao executar o programa, ele acesssa a pagina https://jsonplaceholder.typicode.com/todos e retorna os 5 primeiros itens, mas apenas as informações "id" e "title" destes mesmos 5 itens.

O código retorna também o timestamp, o retorno da API consultada, o HTTP status code da API consultada e um retorno do tipo json caso haja algum erro interno no server.
Estes retornos foram pedidos pelo teste.

Para a elaboração do código foi utilizado o aplicativo Pycharm e as bibliotecas Flask, DateTime e httpx.

# Como utilizar
Descrição de utilização no Pycharm:
- Copiar o conteúdo do arquivo "main.py" em seu projeto.
- Fazer o download das bibliciotes necessárias. No Pycharm, isto pode ser feito seguindo os seguintes passos:
      File -> setting -> Python interpreter -> Install (botão "+") -> selecionar a biblioteca (flask, httpx e datetime) e install package (fazer isto para as três         bibliotecas).
  
 No terminal:
      - pip install flask==2.0.3
      - pip install httpx 
   
- Executar o código (run).
- Ao executar o código, o terminal apresentará a seguinte mensagem: "Running on http://127.0.0.1:5000 (Press CTRL+C to quit)". Ao clicar no link, você será direcionado a uma página não encontrada no navegador.
- Digitar "/registros"ao lado da url para acessar o conteúdo e dar enter, conforme texto a seguir: http://127.0.0.1:5000/registros.
- O navegador irá apresentar na nova página as informações consultadas do site do teste. O terminal irá apresentar, respectivamente, o retorno da API consultada, o HTTP status code da API consultada e o timestamp, realizando o que foi pedido pelo teste.
