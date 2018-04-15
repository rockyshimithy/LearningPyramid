# LearningPyramid

### API usando Python 3.6 e Pyramid para exibir citações do Zen do Python e sessões armazenadas  

Antes de começar, é necessário a criação e ativação de uma VirtualEnv com Python 3.6, para isso recomendo pyenv. Após isso, vá para a pasta raiz desse projeto (LearningPyramid) e siga as instruções abaixo.

1) Instale os requisitos do projeto

    ```
    $ pip install -r requeriments.txt
    ```
    
    *nota: Para executar os testes, utilizar o ipython e o ipdb, utilize requeriments_dev.txt.*
    
2) Instale a aplicação

    ```
    $ pip install -e .
    ```
    
3) Inicialize o Banco

    ```
    $ initializedb production.ini
    ```

4) Suba a aplicação

    ```
    $ pserve production.ini --reload
    ```     

### Testando a aplicação

Utilize um browser e faça requisições GET nos seguintes endpoints:

* http://localhost:6543/
    * O retorno sera apenas um conteudo contendo "Desafio Web 1.0".
    
* http://localhost:6543/quotes
    * O retorno sera as citações do Zen do Python.
    
* http://localhost:6543/quotes/{quote_id}
    * O retorno sera uma das citações do Zen do Python, dado a linha informada usando conceito de lista. 
    
* http://localhost:6543/quotes/random
    * O retorno sera uma das citações do Zen do Python aleatoriamente e informando qual linha.
    
* http://localhost:6543/sessions
    * O retorno sera todas as sessoes cadastradas por esse browser ou qualquer outro. Sugestao fazer requisiçoes via CURL para identificar o comportamento.
    



