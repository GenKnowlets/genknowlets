# Genknowlets: Crawler e Conversor

Este código extrai montagens(assemblys) de genomas referenciados em uma publicação do PubMed e converte em nanopublicações. 

Para rodar, apenas execute `./biocrawler.sh` na pasta do repositório em um terminal Linux. As nanopublicações são depositadas na pasta converter/output.

A criação desse projeto foi parte da discplina de Bioinformática do Departamento de Ciência da Computação  UFRJ, ministrada pela professora Maria Luiza em conjunto com professores e alunos de mestrado da Fiocruz.

# Crawler de Pubmed e GenBank

Esse crawler usa a biblioteca Colly para navegar pelas páginas do Pubmed e GenBank para capturar dados.

Seu uso deve ser somente para gerar um executável a ser utilizado junto com o código python do Genknowlets.

Passos:
* Na pasta root, rodar _go build_ através do terminal.
* Copiar arquivo .exe gerado para a pasta root do projeto Genknowlets.
* Na pasta root do Genknowlets, rodar _biocrawler_ através do terminal, podendo usar as flags abaixo:
    * _-u [url]_ : Define a url do Pubmed ou Genbank a ser coletada
    * _-g_ : Baixar os arquivos GBFF
    * _-r_ : Procurar outras cepas relacionadas
    * _-q_ : Esconder os logs
    * _-p_ : Printar o JSON gerado após finalização

# Conversor

Converte .json extraídos dos assemblys do NCBI para nanoopublicação/nanopublicações.

Coleta todos os arquivos .json da pasta input/, converte para nanopub e armazena na pasta output/.
O nome dos outputs são `<nome_do_arquivo_original_sem_extensao>_<numero_sample>.rdf`

