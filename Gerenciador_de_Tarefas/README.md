# Terminal Task Manager (To-Do List) — Python & SQLite

Este repositório contém o desenvolvimento de uma aplicação para gerenciamento de tarefas em ambiente de linha de comando (CLI). O objetivo principal do projeto é aplicar conceitos fundamentais de **Programação Orientada a Objetos (POO)** e **Persistência de Dados Relacional**, mitigando o acoplamento entre as camadas de apresentação e de infraestrutura.

---

## Arquitetura e Padrões de Projeto

A arquitetura do sistema foi projetada seguindo o princípio de **Responsabilidade Única (SRP)**, dividindo-se em duas entidades principais:

1. **Camada de Domínio/Apresentação (Classe `Lista`):** Abstrai as interações de I/O no terminal (captura de dados e exibição). Esta classe não possui conhecimento sobre a implementação da persistência; ela recebe a dependência do banco através de **Injeção de Dependência (DI)** via método construtor.
2. **Camada de Infraestrutura/Persistência (Classe `SQlite`):** Responsável estritamente pelo ciclo de vida das conexões com o SGBD (SQLite), execução de queries e garantia de atomicidade nas transações através de gerenciamento de cursores e *commits*.

Essa abordagem garante um **baixo acoplamento** e uma **alta coesão**, facilitando futuras migrações de tecnologia (como a substituição do SQLite por outro SGBD) sem a necessidade de refatorar a lógica de interface.

---

## Funcionalidades Implementadas (MVP)

A especificação atual do sistema compreende as operações básicas de manipulação de dados:
* **Persistência de Registros (Create):** Captura e sanitização de strings para inserção na base de dados, utilizando *parametrização de queries* para prevenção de vulnerabilidades de *SQL Injection*.
* **Recuperação de Dados (Read):** Consulta exaustiva à tabela de tuplas através do método `SELECT`, retornando os registros estruturados do banco.
* **Exclusão de Registros (Delete):** Remoção física de registros utilizando filtragem por correspondência exata de string.

---

## Roadmap de Desenvolvimento e Escalabilidade

O projeto foi concebido sob a filosofia de desenvolvimento incremental. As próximas melhorias mapeadas para o sistema incluem:

- [ ] **Otimização do Filtro de Deleção:** Refatoração da cláusula `WHERE` para operar sobre chaves primárias (`ID` numérico/INTEGER), reduzindo a complexidade de busca e evitando inconsistências por strings homônimas.
- [ ] **Tratamento e Formatação da Camada de Visualização:** Implementação de estruturas de iteração (`for`) para parsing das tuplas retornadas pelo SGBD, transmutando dados brutos em uma interface amigável ao usuário.
- [ ] **Implementação do Mecanismo de Atualização (Update):** Conclusão do ciclo CRUD com a introdução da edição de registros existentes indexados por ID.

---

## Execução do Sistema

Para instanciar o ambiente e executar o script principal, certifique-se de possuir o interpretador Python 3 instalado e execute:

```bash
python main.py
```
