<h1 align="center"> Teste para estágio dev na dti - Sistema de Lembretes </h1>

### O sistema

Permite a criação de lembretes, contendo título, descrição, data e a prioridade. Os lembretes criados são listados em uma página, organizados 
de forma cronológica, da data mais recente para a mais distante, sendo permitido também a edição e remoção de lembretes. É possível também 
fazer o cadastro de usuários, dessa forma apenas o usuário que criou o lembrete terá acesso a lista. No desenvolvimento foi usado o framework 
Django e o SQLite para armazenar os dados.

### Instruções para executar

O sistema está hospedado no Heroku, sendo possível acessar através do link abaixo:
```
 https://lembretes-dti.herokuapp.com/
```
Para rodar o sistema localmente é necessário ter o Python instalado se seguir os passos (no windows):

1. Baixe o código e extraia a pasta.
2. Na área de trabalho, crie uma pasta chamada "sistema_lembretes".
3. Dentro da pasta criada, crie outra, dessa vez chamada "gerenciador_tarefas".
4. Pegue os arquivos da pasta extraída no passo 1 e cole na pasta criada no passo 3.
5. Dentro da pasta "gerenciador_tarefas" tem que estar assim agora:

<div>
 <img src="https://user-images.githubusercontent.com/74077027/187863494-6d6cccc6-e112-4cf0-ba49-e271c2b21987.png" width="500px">
</div>

6. Abra o cmd, navegue até a pasta "sistema_lembretes" e digite o comando abaixo para criar um ambiente virtual chamado "env":
```
python -m venv env
```
<div>
 <img src="https://user-images.githubusercontent.com/74077027/187865762-c9fabe68-2e5e-4754-9963-1c486ed61573.png" width="750px">
</div>

7. Ainda no terminal, digite o comando para ativar o ambiente virtual que foi criado:
```
env\Scripts\activate.bat
```
<div>
 <img src="https://user-images.githubusercontent.com/74077027/187866660-d84d8fa3-3966-45dd-b7b0-1799d8871fe1.png" width="750px">
</div>

8. No mesmo terminal, digite o comando para instalar o Django:
```
pip install django
```
9. Ainda no terminal, digite o comando para entrar no diretório do projeto:
```
cd gerenciador_tarefas
```
10. Para rodar o servidor, digite o comando:
```
python manage.py runserver
```
11. Acesse o link que foi retornado:
<div>
 <img src="https://user-images.githubusercontent.com/74077027/187868558-055c774c-f1dc-4539-8bc4-bc6974c703b3.png" width="800px">
</div>

12. Crie um novo usuário para poder cadastrar lembretes ou use os usuários abaixo, que já existem tanto no sistema local quanto no que ta hospedado na nuvem:

Usuário  | Senha
------------- | -------------
usuario1  | user1234
usuario2  | user1234
