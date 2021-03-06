# Dados-zup

Projeto dividido em 5 camadas e seguindo as boas práticas do DDD:<br/>
* domain - responsável por receber as entidades de negócio da aplicação
* jobs - responsábel por receber o(s) job(s) que serão executados pela a aplicação
* repository - responsável por receber todas as classes relacionadas com acesso a dados (foi utilizado orm SqlAlachemy)
* services - responsável por receber todas as classes de serviço da aplicação
* utils - responsável por receber as classes com funções de utilidade para toda a aplicação


Neste documento está descrito o passo a passo para a execução do projeto. 

## Instalação

Após "clonar" o projeto verificar que o mesmo está organizado da seguite forma:

![alt text](https://github.com/thiagop7/dados-zup/blob/main/clone.png)

Na raiz do projeto, executar o arquivo requirements.txt para instalar as dependências do projeto.

```bash
pip install -r requirements.txt
```

Na raiz do projeto, utilizar o comando docker para iniciar o banco de dados.

```bash
docker-compose up -d
```

Verificar que o container docker do postgresql está iniciado.

```bash
docker-compose ps
```

![alt text](https://github.com/thiagop7/dados-zup/blob/main/imageposgres.png)

De dentro do diretório raiz do projeto, executar o comando abaixo iniciar o processo.

```bash
python main.py
```

Verificar que todos os passos foram executados.

![alt text](https://github.com/thiagop7/dados-zup/blob/main/log.png)

Verificar que o arquivo de saída foi gerado com sucesso no diretório de output /data/output/TotalCost.xlsx

![alt text](https://github.com/thiagop7/dados-zup/blob/main/output.png)

Verificar no container do postgresql que a tabela foi criada e os dados foram inseridos (utilizar o CONTAINER_ID gerado pelo docker para executar os comandos).

```bash
docker ps -a
```

![alt text](https://github.com/thiagop7/dados-zup/blob/main/dockerps.png)

```bash
docker exec -it [CONTAINER_ID] bash
```
![alt text](https://github.com/thiagop7/dados-zup/blob/main/dockerexec.png)

Após entrar no container, verificar que a tabela foi criada pala aplicação e os dados foram inseridos.

```bash
psql -U postgres
```
Password: pwd0123456789

![alt text](https://github.com/thiagop7/dados-zup/blob/main/result_banco.png)

