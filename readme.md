## Renderização e transformações de objetos em 3D
Este projeto é parte da avaliação da disciplina de Computação Gráfica, turma de 2020.1, do curso de Ciência da Computação da Universidade Federal Fluminense. O objetivo é implementar um conjunto de funções que permitissem renderizar um objeto (descrito na estrutura Faces e Vértices) e aplicar transformações elementares, como projeções, cisalhamentos, translações e escalas.
___
### Alunos
[Gabriel](https://github.com/madfrr),
[Lucas](https://github.com/Lucasark) e
[Rafael](https://github.com/rafaeldcampbell)

### Pré-Requesitos
- Python 3.5.0 ou superior
- Navegador com WebGL 2.0 Native (Chrome, Firefox, Opera, Edge etc.)
- VPython 7 ou superior (Instalavel via *requirements*, use `pip install -r requirements.txt`)

### Execução
Para iniciar o programa, use:
```
cd ./src
python printableObject.py
```

### Estrutura
Serão utilizados dois dicionários, um para armazenar vértices e outro para armazenar as faces correspondentes. Ao iniciar, o sistema listará todos os objetos encontrados no diretório [/src/objetos](/src/objetos) e o usuário deve selecionar qual objeto deseja renderizar. Os objetos devem estar descritos em dois arquivos, um com as faces (*\*Faces.csv*) e outro com os vértices (*\*Vertex.csv*).

**Faces**

Cada linha descreverá uma face triangular, contendo:
* Identificador
* Os tres vértices
* Uma cor em hexadecimal (opcional)

> \<identificador\>,\<vértice1\>,\<vértice2\>,\<vértice3\>,\<cor\>

**Vértices**

Cada linha descreverá um vértice, contendo:
* Identificador
* As coordenadas x, y e z

> \<identificador\>,\<coordenada x\>,\<coordenada y\>,\<coordenada z\>


### Imagens
Disponibilizamos duas imagem do objeto [Casa](src/objetos/casa/) em [/img](/img), exibindo sua estrutura Vértice-Face e o resultado renderizado.
