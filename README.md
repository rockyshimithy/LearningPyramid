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

...
    



