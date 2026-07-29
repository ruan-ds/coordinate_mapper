# ADR-003: Salvar o projeto em JSON com metadados da imagem

- Status: Aceito
- Data: 2026-07-28

## Contexto

Era importante preservar não apenas os pontos marcados, mas também informações essenciais sobre a imagem original, como caminho, largura e altura.

## Decisão

Persistir os dados em um arquivo JSON contendo:

- metadata da imagem;
- lista de pontos marcados;
- informações adicionais como grupo e identificador do ponto.

## Consequências

- O arquivo gerado é simples de inspecionar e editar manualmente.
- Os pontos podem ser interpretados corretamente mesmo em diferentes contextos de resolução.
- Abre espaço para futuras integrações com outros formatos de exportação.
