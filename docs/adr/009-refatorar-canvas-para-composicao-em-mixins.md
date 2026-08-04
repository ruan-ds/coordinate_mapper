# ADR-009: Refatorar o Canvas para composição em mixins especializados

- Status: Aceito
- Data: 2026-08-04

## Contexto

O `Canvas` inicialmente combinava diversas responsabilidades em uma única classe: renderização da cena, interação do usuário, controle de imagem, persistência de projetos, menus de contexto, controle de escala e operações de undo.

Embora funcionasse, essa abordagem criava um componente altamente acoplado e difícil de evoluir. Cada nova funcionalidade exigia tocar em uma classe central que já conhecia muitos detalhes diferentes da aplicação.

## Decisão

Transformar o `Canvas` em um componente de composição, prioritariamente responsável por inicializar a `QGraphicsView` e reunir comportamentos especializados.

A nova estrutura divide o comportamento em módulos independentes dentro de `features/canvas/`:

- `drawing.py`: renderização da cena, desenho de pontos e atualização visual;
- `events.py`: interação do usuário, cliques do mouse, conversão de coordenadas e criação de pontos;
- `commands.py`: sistema de comandos e undo;
- `image.py`: gerenciamento de imagem, carregamento e estado do `QPixmap`;
- `menu.py`: menus de contexto e ações sobre pontos;
- `project.py`: persistência de projetos e diálogo de salvamento;
- `viewport.py`: ajuste de escala e comportamento de redimensionamento.

O `Canvas` passou a ser declarado como:

```python
class Canvas(
    CanvasDrawingMixin,
    CanvasEventsMixin,
    CanvasCommandsMixin,
    CanvasImageMixin,
    CanvasMenuMixin,
    CanvasProjectMixin,
    CanvasViewportMixin,
    QGraphicsView,
):
```

## Consequências

- Menor acoplamento: cada área pode evoluir sem modificar o componente principal.
- Maior extensibilidade: novas funcionalidades podem ser adicionadas em módulos específicos.
- Melhor manutenção: o `Canvas` deixou de ser um arquivo monolítico e passou a compor comportamentos.
- Preparação para futuras evoluções: seleção, ferramentas, múltiplos tipos de desenho, histórico de undo/redo mais completo e exportadores.

## Benefícios obtidos

- O `Canvas` agora reúne apenas os mixins e a inicialização do `QGraphicsView`.
- A renderização ficou isolada em `drawing.py`.
- A lógica de eventos ficou isolada em `events.py`.
- O undo simples foi mantido em `commands.py` com arquitetura preparada para um sistema de comandos mais completo.
- O carregamento de imagens e o cache de `QPixmap` foram centralizados em `image.py`.
- O menu de contexto passou a ser responsabilidade de `menu.py`.
- A persistência do projeto ficou em `project.py`.
- O controle de visualização e escala ficou em `viewport.py`.

## Conclusão

A refatoração tirou do `Canvas` a responsabilidade de implementar diversas funcionalidades e o transformou em um agregador de comportamentos. O resultado é uma base arquitetural mais robusta, mais fácil de entender e mais preparada para crescer.
