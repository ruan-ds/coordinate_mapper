# ADR-000: Ideias futuras e TODO

## Contexto

O projeto já possui a base funcional, mas continua evoluindo para oferecer uma experiência de uso mais completa e organizada.

### Funcionalidades já implementadas

As seguintes funcionalidades foram incorporadas recentemente ao fluxo principal do projeto:

#### Exclusão de ponto individual

- exclusão de ponto individual por meio de um menu contextual;

#### Undo inicial com Ctrl+Z

- suporte inicial a desfazer a última inserção de ponto único com Ctrl+Z;

#### Gerenciamento de pontos separado

- centralização do gerenciamento de pontos em um componente dedicado para melhorar a organização do código;

#### Movimentação de pontos com SelectTool

- movimentação de pontos via `SelectTool` com arraste e atualização de coordenadas;

#### Criação de vértices com VertexTool

- criação de vértices com `VertexTool`, interpolação de pontos e ajuste de densidade.

Essas mudanças são justificadas e documentadas em:

- [docs/adr/006-introduzir-gerenciador-de-anotacoes.md](docs/adr/006-introduzir-gerenciador-de-anotacoes.md)
- [docs/adr/008-adicionar-selecttool-para-mover-pontos.md](docs/adr/008-adicionar-selecttool-para-mover-pontos.md)
- [docs/adr/009-adicionar-vertextool-para-criacao-de-vertices.md](docs/adr/009-adicionar-vertextool-para-criacao-de-vertices.md).

### TODO

As próximas melhorias planejadas para o projeto são:

#### Reestruturar o sistema de Undo/Redo

- substituir o comportamento atual de "remover último ponto" por um histórico real de ações (`Command Pattern`), permitindo desfazer/refazer criação, exclusão, movimentação e edição de vértices.

#### Implementar persistência de projetos

- salvar e carregar anotações (pontos, grupos, vértices, configurações e metadados da imagem) em um formato próprio, permitindo continuar trabalhos posteriormente.

#### Melhorar a edição de vértices existentes

- permitir movimentação dos pontos base do vértice (início/fim) e regeneração automática da interpolação mantendo quantidade e densidade configuradas.

### Sugestão

Estas melhorias podem ser implementadas de forma incremental, sem comprometer a arquitetura modular atual.
