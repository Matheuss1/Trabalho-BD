# Projeto <em>Índices econômicos mundiais</em>

# Equipe <em>Invest Bank - INVB3</em>
- Leonardo Rener de Oliveira - 201270
- César Guedes Carneiro - 261031
- Matheus Silva de Deus - 241882

## Resumo do Projeto
O grupo apresenta como proposta a construção de um dataset contendo dados históricos, no últimos anos, dos índices econômicos de países, como o Bovespa, no caso do Brasil, e o Dow Jones e Nasdaq para os Estados Unidos, por exemplo.

Nossa motivação é disponibilizar estes dados de maneira acessível, gratuita e com uma boa organização. Desta forma, tornando mais simples o processo de estudo, para alguém que tenha interesse de estudar tais tipos de dados.

Esperamos que com o projeto aqui apresentado, sejam possíveis aplicações de análises estatísticas sobre os dados, de forma a responder perguntas do tipo: Qual foi a evolução de determinado indíce em certo período de tempo? Como ele se compara com outros índices? Qual sua relação com o desenvolvimento econômico de determinado país? Dentre muitas outras perguntas que possam ser consideradas, limitadas apenas pela criatividade de quem estiver a manipular tais informações históricas.

## Slides da Apresentação
[Slides](slides/apresentacao2.pdf)

## Modelo Conceitual Preliminar
![Modelo Conceitual](assets/modelo_conceitual.png)

## Modelos Lógicos Preliminares

### Modelos Relacional
~~~
País(_nome_)
PIB(_país_, _ano_, valor)
    país chave estrangeira -> País(nome)
Índice_Econômico(_nome_, moeda)
Pertence(_país_, _índice_)
    país chave estrangeira -> País(nome) e índice chave estrangeira -> Índice(nome)
Histórico_de_preços(_índice_, _ano_, _mês_, pontosAbertura,  pontosFechamento)
    CHE: indíce para Índice_Econômico
~~~

### Modelos Hierárquicos (XML e JSON)
![Modelo Documentos](assets/modelo_documentos.png)

## Dataset Preliminar a ser Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.

## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`<título da base>` | `<link para a página da base>` | `<breve descrição da base>`

## Operações realizadas para a construção do dataset

> Coloque um link para o arquivo do notebook, programas ou workflows que executam as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Liste aqui as perguntas de pesquisa/análise e respectivas análises.
> Nem todas as perguntas precisam de queries que as implementam.
> É possível haver perguntas em que a solução é apenas descrita para
> demonstrar o potencial da base.
>
### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Explicação sucinta da análise que será feita ou conjunto de queries que
>     responde à pergunta.

### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Explicação sucinta da análise que será feita ou conjunto de queries que
>     responde à pergunta.

### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Explicação sucinta da análise que será feita ou conjunto de queries que
>     responde à pergunta.

> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
