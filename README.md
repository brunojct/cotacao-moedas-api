# Cotação de Moedas - TkInter

<div align = 'center'>
 <img src = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/bbada2c0-b1d5-4b3d-9f42-c350ed529bef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220925T153328Z&X-Amz-Expires=86400&X-Amz-Signature=73cd233a2d4d3d2eaf7e45490f3afaee6c820f74f06279ca84d3f3f308e4ae0f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject' width = '40%'/>
</div>

### Objetivo

Construir um sistema através do tkinter no qual o usuário consegue consultar a cotação de diferentes moedas de duas maneiras:<br><br>

- Primeira Maneira: Cotação de uma única moeda em um único dia.

Por exemplo: cotação do dólar canadense no dia 12/06/2022.<br><br>

- Segunda Maneira:  Cotação de múltiplas moedas em um determinado período.

Por exemplo: cotação do euro, bitcoin e dólar no período de 20/07/2022 até 14/08/2022.<br><br>


A busca dos valores é feita através do consumo de uma API.


### Funcionamento do sistema

Para o primeiro caso, o sistema já te dá uma resposta automática com a cotação desejada.

<div align = 'center'>
 <img src = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/53c96a63-0205-4f9d-b915-415d8b53649e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220925T153447Z&X-Amz-Expires=86400&X-Amz-Signature=01dfea1ab47cd9b07c32827407a00bc85ebbfaeaa3a037b159fd528748f5038a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject' width = '50%'/>
</div>

Já para o segundo caso, o usuário insere uma planilha com as moedas que deseja buscar a cotação e o sistema retorna com a planilha atualizada com a cotação de cada moeda em todos os dias do período selecionado pelo usuário.

<div align = 'center'>
 <img src = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8d9f183b-bb56-4696-b250-11c978b45f5a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220925T153523Z&X-Amz-Expires=86400&X-Amz-Signature=916295d307c6aa733accb4e0707e26f0523a8daa238885548c58ded24ac3cafd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject' width = '50%'/>
</div>

<div align = 'center'>
 <img src = 'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/832eda3c-7db0-45e1-bc8e-a1b13e06b0ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220925T153557Z&X-Amz-Expires=86400&X-Amz-Signature=0e9307380d34cf665fbc5afbf4f8a06faf0f5829733bbd9a3f3ef66ab2c7a6d8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject' width = '30%'/>
</div>

