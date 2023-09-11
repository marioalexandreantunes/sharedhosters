# SHARED HOSTER
How to deploy a django app to a shared hoster like namecheap.com

## Fornecedores

Usei `namecheap.com` fiz testes com shared hosting Stellar, que é o mais barato , fica 1,38€/mes. Para pequenos projectos poderás usar um, não é obrigatorio microsserviços e estruturas escalável.<br />
<sub>Atenção o django precisar cache com `redis` não está disponível.<br />
Shared Hoster terão possivelmente alguma limitações, exemplo Pillow que não poderás installar as novas versões, e usar versões antigas em produção poderá não se uma boa idea.</sub><br /><br />
Alguns fornecedores que tem terminal, git e suporte para Python:<br />
namecheap.com | protozoahost.com | greengeeks.com | fastcomet.com | a2hosting.com | hostinger.com<br />
<sub>Verificar bem todas as caracteristicas antes de adquirir qualquer que seja o fornecedor!<br />
Caso precises de maior flexibilidade poderás adquirir uma cloud/Shared VPS, alphavps.com tem VPS desde 2.99€/m</sub>

### Tutorial

- Primeiro é ir ao `CPanel-Terminal` e usar `git clone` para clonar a tua webapp, relembro que na tua conta github adiciona um token 
  ```
          git clone https://TOKEN@github.com/GITUSER/REPOSITORY.git
  ```

- ir ao `CPanel-Python` e criar uma app (**python 3.9**) a apontar para a caminho anterior do git clone onde estará o teu manage.py
  - escolhi o `python 3.9` pois foi onde consegui instalar o django 4.2.5 (ultimo)
- Copiar no `CPanel-Python` o comando para activar `virtual environment`.
- Ir ao `CPanel-Terminal` e correr esse comando
- Instalar os modulos necessarios, usando `pip install`, exemplo:
  ```
          pip install Django PyMySQL python-decouple django-admin-honeypot-updated-2021 cloudinary pillow==8.3.2
  ```
- `CPanel-FileManager` e entrar na pasta onde está a tua webapp e verifica o ficheiro `passenger_wsgi.py`
  - Ainda ai dentro relembro que se usas um `.env` deverás o criar e configurar, ou poderás usar a opção em `CPanel-Python` `add environment variables`
  - Relembro também todas as configurações no `settings.py` deveras fazer para teres `static` e `media` a funcionar.
  - Relembro de todas configurações necessarias para ter uma aplicação segura.
- Modificar para apontar para uma aplicação django
  ```
          import APPNOME.wsgi
          application = APPNOME.wsgi.application
  ```
- `CPanel-Python` reload da app 
- já estará a correr
- `CPanel-FileManager` existe o `stderr.log` tem possiveis erros!
- Para atualizar 
  - `CPanel-Terminal` ainda com ambiente virtual ativado: 
    ```
            git fetch
    ```
    ```
            git pull
    ```
    ```
            python manage.py makemigrations & python manage.py migrate
    ```
    se necessários!
  - `CPanel-Python` e reload da app.
