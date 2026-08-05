# ADR-000: Ideias futuras e TODO

## Contexto

O projeto já possui a base funcional, mas continua evoluindo para oferecer uma experiência de uso mais completa e organizada.

### Funcionalidades já implementadas

As seguintes funcionalidades foram incorporadas recentemente ao fluxo principal do projeto:

- exclusão de ponto individual por meio de um menu contextual;
- suporte inicial a desfazer a última ação com Ctrl+Z;
- centralização do gerenciamento de pontos em um componente dedicado para melhorar a organização do código;
- movimentação de pontos via `SelectTool` com arraste e atualização de coordenadas;
- criação de vértices com `VertexTool`, interpolação de pontos e ajuste de densidade.

Essas mudanças são justificadas e documentadas em:

- [docs/adr/006-introduzir-gerenciador-de-anotacoes.md](docs/adr/006-introduzir-gerenciador-de-anotacoes.md)
- [docs/adr/008-adicionar-selecttool-para-mover-pontos.md](docs/adr/008-adicionar-selecttool-para-mover-pontos.md)
- [docs/adr/009-adicionar-vertextool-para-criacao-de-vertices.md](docs/adr/009-adicionar-vertextool-para-criacao-de-vertices.md).

### TODO

As próximas melhorias planejadas para o projeto são:


### Sugestão

Estas melhorias podem ser implementadas de forma incremental, sem comprometer a arquitetura modular atual.
