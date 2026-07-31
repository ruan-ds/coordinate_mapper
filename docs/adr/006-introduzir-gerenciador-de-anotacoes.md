# ADR-008: Introduzir um gerenciador de anotações para o controle de pontos

- Status: Aceito
- Data: 2026-07-31

## Contexto

O fluxo de criação e manipulação de pontos estava concentrado diretamente na lógica visual do Canvas, o que deixava a lógica de estado mais difícil de evoluir. Com o aumento das operações possíveis sobre os pontos, tornou-se importante separar a responsabilidade de gerenciamento dos elementos da interface visual.

## Decisão

Introduzir um gerenciador dedicado de anotações para centralizar o controle dos pontos criados pelo usuário.

Essa abstração passou a ser responsável por:

- registrar novos pontos adicionados na imagem;
- remover pontos individuais quando solicitado pelo usuário;
- desfazer a última ação de inserção por meio de um fluxo simples de undo;
- manter o estado dos pontos de forma independente do componente visual.

A mudança foi feita para preparar a base para futuras operações de edição e expansão do sistema sem sobrecarregar o Canvas.

## Consequências

- O código relacionado ao estado dos pontos ficou mais organizado e fácil de manter.
- O Canvas passou a se concentrar mais na interação visual e menos na gestão de dados.
- A interface ganhou suporte inicial a remoção de pontos específicos e a desfazer a última ação.
- A arquitetura ficou mais preparada para futuras melhorias, como edição, movimentação e enriquecimento de propriedades dos pontos.
