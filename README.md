# Análise de dados com Python #

Análise de dados é um mercado que cresce ano a ano, e junto com esse mercado a quantidade de dados que devem ser analisados também crescem dia a dia.
Imaginem a quantidade de dados de um Facebook por exemplo, como analisar e otimizar um volume tão grande de dados?

Outro ponto que deve ser destacado é a adoção de diferentes linguagens de programação para um sistema, os sistemas não necessitam mais serem desenvolvidos apenas em uma linguagem de programação, uma frase que gosto muito de dizer: "cada problema uma solução", ou melhor "cada problema tem uma linguagem de programação que o resolve mais facilmente".

Nessa crescente demanda por análise de grandes volumes de dados uma linguagem de programação se destaca, o Python.
Mas o Python não faz isso sozinho, a biblioteca responsável por isso chama-se **Pandas**.

# Pandas

Pandas é a biblioteca open-source de análise de dados mais importante em Python.

Mas como o Pandas faz e otimiza esse trabalho?

Criando DataFrames!

Os *DataFrames* são estruturas que comportam dados de forma tabular. Os DataFrames são compostos de linhas e colunas, sendo cada coluna um campo da tabela e cada linha um registro. Cada coluna possui dados de um mesmo tipo. Você pode imaginar uma tabela de Excel, mas nesse caso, cada coluna é limitada a um tipo de dado.

É possível criar um DataFrames de diversas formas, aqui iremos criar um à partir de um CSV.

Vamos à prática!
*Para melhores resultados execute esses comandos em um terminal interativo python, basta em um terminal executar a instrução `python` que você estará em um terminal interativo python :)*

# Prática

Vamos fazer o download de um CSV que contém diversos imóveis da cidade de Seattle nos Estados Unidos, e vamos praticar a manipulação de algumas informações.

#### Download CSV

```python
import pandas as pd
import io
import requests

url = 'https://raw.githubusercontent.com/fabiohbarbosa/pandas_samples/master/files/house_data.csv'
csv = requests.get(url).content
```

#### Criar um DataFrame à partir de um CSV
```python
df = pd.read_csv(io.StringIO(csv.decode('utf-8')))
```

#### Agrupar os imóveis pelo número de casas de banho
```python
pd.value_counts(df['bedrooms'])
```

**Output**
```
>>> pd.value_counts(df['bedrooms'])
3.0     9822
4.0     6881
2.0     2759
5.0     1601
6.0      272
1.0      199
7.0       38
8.0       13
0.0       13
9.0        6
10.0       3
11.0       1
33.0       1
```

#### Listar somente os imóveis com 3 casas de banho
```python
df.loc[df['bedrooms'] == 3]
```

**Output**
```
>>> df.loc[df['bedrooms'] == 3]
               id             date      price  bedrooms  bathrooms  \ ...
0      7129300520  20141013T000000   221900.0       3.0       1.00
1      6414100192  20141209T000000   538000.0       3.0       2.25
4      1954400510  20150218T000000   510000.0       3.0       2.00
6      1321400060  20140627T000000   257500.0       3.0       2.25
...
```

### Criar uma nova coluna classificando os imóveis pelo preço
Iremos classificar os imóveis que custam mais de um $1.000.000 como `Very expensive`, os que estão entre $500.000 e $1.000.000 como `Expensive` e os abaixo de $500.000 como `Normal`

```python
# Primeiro criamos uma função
def type_price(price):
    if price < 500000:
       return 'Normal'
    if price >= 500000 and price < 1000000:
       return 'Expensive'
    if price >= 1000000:
       return 'Very Expensive'

# Em seguida aplica-se a função para criarmos uma nova coluna com o nome 'cat_by_price' no DataFrame
df['cat_by_price'] = df['price'].apply(type_price)

df[['price', 'cat_by_price']]
```

**Output**
```
>>> df[['price', 'cat_by_price']]
           price    cat_by_price
0       221900.0          Normal
1       538000.0       Expensive
2       180000.0          Normal
3       604000.0       Expensive
4       510000.0       Expensive
5      1225000.0  Very Expensive
6       257500.0          Normal
7       291850.0          Normal
8       229500.0          Normal
9       323000.0          Normal
...
```

# Conclusão
A biblioteca **Pandas** é muito eficaz e poderosa, pode-se manipular diversos dados de uma forma simples e rápida. Para mais informações consulte a [documentação oficial](http://pandas.pydata.org/pandas-docs/stable/).
Você pode conferir o código usado no exemplo no meu [github](https://github.com/fabiohbarbosa/pandas_samples).