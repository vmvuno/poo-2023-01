# POO 2023-1
 [![Build Status](https://app.travis-ci.com/vmvuno/poo-2023-01.svg?branch=main)](https://app.travis-ci.com/vmvuno/poo-2023-01) [![Coverage Status](https://coveralls.io/repos/github/vmvuno/poo-2023-01/badge.svg?branch=main)](https://coveralls.io/github/vmvuno/poo-2023-01?branch=main)

___

## Finalidade e conteúdo
Repositório criado a fim de promover a entrega das atividades avaliativas da disciplina de Programação Orientada a Objetos, no primeiro semestre de 2023, do curso de Engenharia de Software da Universidade Federal de Goiás.  

O material da disciplina, juntamente com os enunciados das atividades propostas, podem ser encontrados no repositório de [Orientação a Objetos (OO)](https://www.github.com/kyriosdata/oo), mantido pelo Prof. Fábio Nogueira de Lucena.

___

## Comandos inclusos no poetry

```sh
poetry run_tests
```
Executa a suite de testes do projeto, compreendendo:
- Análise de conformidade à PEP8 (Flake8);
- Análise estática (mypy);
- Testes unitários (pytest); e
- Análise de cobertura (pytest-cov).

<br>

```sh
poetry run_style_analysis
```
Executa a análise de conformidade ao guia de estilo da linguagem (PEP8) isoladamente.  
Ferramenta: Flake8

<br>

```sh
poetry run_static_analysis
```
Executa a análise estática isoladamente.  
Ferramenta: mypy

<br>

```sh
poetry run_tests_and_coverage_analysis
```
Executa os testes unitários e a análise de cobertura isoladamente.  
Obs.: Testes unitários foram desenvolvidos apenas para o módulo T07, visto o tempo que demandavam e que não eram requisitados pela proposta do professor.  
Ferramentas: pytest e pytest-cov

<br>

```sh
poetry count_lines
```
Mostra estatísticas acerca da quantidade de linhas de código elaboradas na implementação das classes propostas.  
Ferramenta: pygount

<br>

```sh
poetry count_classes
```
Mostra a quantidade de classes implementadas e em quantos arquivos estão distribuídos
___

## Licença
O conteúdo deste repositório é disponibilizado sob licença [GNU GPLv3.0](LICENSE).
