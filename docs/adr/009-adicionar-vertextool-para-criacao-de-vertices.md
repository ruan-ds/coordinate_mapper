# ADR-009: Adicionar VertexTool para criação de vértices com interpolação

- Status: Aceito
- Data: 2026-08-05

## Contexto

O sistema de ferramentas do `Coordinate Mapper` já suportava seleção, movimento e desenho de pontos, mas não havia um modo estruturado para criar sequências de pontos derivados de dois extremos.

Antes desta implementação, o projeto trabalhava apenas com pontos independentes. A adição de vértices exigia um novo conceito composto, um estado temporário para a criação e um conjunto de regras para cancelar ou confirmar a operação sem poluir o canvas.

## Decisão

Implementar um `VertexTool` que se integra ao `ToolManager` existente e adiciona suporte a:

- seleção de dois pontos consecutivos na imagem;
- abertura de um diálogo de configuração para densidade e contagem;
- geração de pontos interpolados entre os extremos;
- criação de um objeto `Vertex` que agrupa `start_point`, `end_point`, pontos internos, `count` e `density`;
- limpeza de estado temporário quando a ferramenta é desativada ou o diálogo é cancelado.

O `VertexTool` mantém estado interno com:

- `start_point`;
- `end_point`;
- `current_vertex_id`;
- `creating`.

No primeiro clique, a ferramenta cria o `start_point` e define o `current_vertex_id`. No segundo clique, ela cria o `end_point`, abre o `VertexDialog` e só gera o `Vertex` se o diálogo for aceito.

Se o usuário cancelar, o `VertexTool` remove `start_point` e `end_point`, redesenha o canvas e zera o estado interno.

A geração do `Vertex` usa `interpolate_points()` para calcular as coordenadas internas e `apply_density()` para ajustar a distribuição em torno do centro do segmento.

O `AnnotationManager` foi estendido para gerenciar vertices com capacidades como:

- `self.vertices` e `self.next_vertex_id`;
- `add_vertex()`;
- `get_vertex(vertex_id)`;
- `clear_vertex_points(vertex)`;
- `remove_vertex(vertex)`.

Também foi estendido o fluxo de reset do `BaseTool` para aceitar `canvas=None`, permitindo que ferramentas stateful limpem seu próprio estado quando desativadas.

## Consequências

- A ferramenta de criação de vértices passa a existir como um modo explícito e estruturado.
- O canvas não mantém pontos temporários de vértices abandonados.
- O estado de criação é limpo corretamente ao trocar de ferramenta.
- O `AnnotationManager` agora registra não apenas pontos, mas também entidades de `Vertex`.
- A arquitetura do sistema de ferramentas fica mais clara: cada ferramenta é responsável pelo próprio estado, enquanto o `ToolManager` coordena a troca.
- Futuras melhorias podem incluir edição de vertices existentes, undo/redo específico por tool e múltiplos tipos de ferramentas baseadas em estado.

### Referências

- Implementação em `src/coordinate_mapper/features/tools/vertex.py`
- `ToolManager` e `BaseTool` em `src/coordinate_mapper/features/tools/manager.py` e `src/coordinate_mapper/features/tools/base.py`
- `AnnotationManager` em `src/coordinate_mapper/features/annotation/manager.py`
- `VertexDialog` em `src/coordinate_mapper/features/dialogs/vertex_dialog.py`
- `interpolate_points` em `src/coordinate_mapper/features/geometry/interpolation.py`
- ADR-007: Refatorar o Canvas para composição em mixins
