# ADR-008: Adicionar `SelectTool` para seleção e movimentação de pontos

- Status: Aceito
- Data: 2026-08-04

## Contexto

Os usuários precisam de uma forma direta de ajustar pontos já existentes sem removê-los e recriá-los. A interação por simples clique e arraste é a forma mais esperada e natural para esse tipo de operação em ferramentas gráficas.

Além disso, a arquitetura do `Canvas` foi recentemente refatorada para separar responsabilidades em mixins, criando um ambiente propício para introduzir um sistema de ferramentas (`ToolManager` / `Tool`s) que encapsulam modos de interação.

## Decisão

Implementar um `SelectTool` responsável por:

- permitir a seleção de pontos existentes;
- possibilitar arrastar pontos selecionados para atualizar suas coordenadas;
- integrar-se ao `ToolManager` do sistema para alternância entre ferramentas;
- restaurar a integração do menu de contexto para operações adicionais (ex: excluir);
- fornecer feedback visual ao usuário quando o `SelectTool` estiver ativo (mudança de cursor ou destaque do ponto);
- adicionar atalho de teclado para alternar o modo de movimentação (configurado no `window`/UI).

A implementação adotou uma integração mínima e direta com o `AnnotationManager` para atualizar as coordenadas dos pontos durante o drag, e respeita o princípio de separação de responsabilidades: o `SelectTool` cuida apenas da interação, o `AnnotationManager` atualiza o estado e os mixins do `Canvas` lidam com a renderização e menus.

## Consequências

- Os usuários podem mover pontos rapidamente sem perder sua identidade no projeto.
- A arquitetura de ferramentas abre caminho para novas ferramentas (ex: `PointTool`, `MeasureTool`, `SelectTool` com múltipla seleção).
- O `Canvas` e seus mixins permanecem desacoplados da lógica de ferramentas, favorecendo a manutenção.
- Futuras melhorias podem incluir suporte a undo/redo por comando, múltipla seleção e snapping.

### Referências

- ADR-007: Refatorar o Canvas para composição em mixins
- ADR-006: Introduzir um gerenciador de anotações
- ADR-000: Ideias futuras e TODO (modos de inserção planejados)
