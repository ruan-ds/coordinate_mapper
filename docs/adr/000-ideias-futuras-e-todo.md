# ADR-000: Ideias futuras e TODO

## Contexto

O projeto já possui a base funcional, mas continua evoluindo para oferecer uma experiência de uso mais completa e organizada.

### Funcionalidades já implementadas

As seguintes funcionalidades foram incorporadas recentemente ao fluxo principal do projeto:

- exclusão de ponto individual por meio de um menu contextual;
- suporte inicial a desfazer a última ação com Ctrl+Z;
- centralização do gerenciamento de pontos em um componente dedicado para melhorar a organização do código;
- movimentação de pontos via `SelectTool` com arraste e atualização de coordenadas;

Essas mudanças são justificadas e documentadas em:

- [docs/adr/006-introduzir-gerenciador-de-anotacoes.md](docs/adr/006-introduzir-gerenciador-de-anotacoes.md)
- [docs/adr/008-adicionar-selecttool-para-mover-pontos.md](docs/adr/008-adicionar-selecttool-para-mover-pontos.md).

### TODO

As próximas melhorias planejadas para o projeto são:

- criar modos de inserção de pontos, incluindo o modo padrão ponto a ponto e um novo modo por vértices;
- permitir gerar pontos automaticamente entre dois vértices com controle por quantidade ou espaçamento;
- adicionar atalhos para alternar entre a definição do ponto inicial e do ponto final no modo por vértices;
- oferecer um menu contextual mais completo para editar, mover ou excluir pontos selecionados;
- permitir editar pontos já existentes sem precisar removê-los e recriá-los;
- manter a separação entre o gerenciamento de pontos e a lógica visual do Canvas para facilitar futuras expansões.

### Sugestão

Estas melhorias podem ser implementadas de forma incremental, sem comprometer a arquitetura modular atual.

## Sugestão

Estas melhorias podem ser implementadas de forma incremental, sem comprometer a arquitetura modular atual.
