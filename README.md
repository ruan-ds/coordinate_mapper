# Coordinate Mapper

Projeto open-source em Python para marcar coordenadas absolutas sobre imagens por meio de uma interface desktop simples e intuitiva.

## Visão geral

A aplicação permite:

- abrir uma imagem local;
- registrar pontos com clique esquerdo do mouse;
- remover o último ponto com clique direito;
- salvar todas as coordenadas em um arquivo JSON com metadados da imagem.

A arquitetura foi organizada em módulos independentes para facilitar manutenção e evolução futura.

## Funcionalidades

- Interface desktop com PySide6
- Marcação de pontos em coordenadas absolutas
- Armazenamento de metadados da imagem (caminho, largura e altura)
- Exportação para JSON estruturado
- Estrutura modular para expansão futura

## Estrutura do projeto

- main.py: ponto de entrada da aplicação
- src/coordinate_mapper/: pacote principal do projeto
- docs/adr/: registros de decisões de arquitetura
- tests/: testes automatizados

## Arquitetura do Canvas

O `Canvas` foi refatorado para funcionar como um agregador de comportamentos, reunindo mixins especializados em vez de centralizar todas as responsabilidades em uma única classe. Essa separação melhora a manutenção e prepara o projeto para evoluir com recursos como seleção, ferramentas e undo/redo mais completos.

Veja a decisão arquitetural em [docs/adr/007-refatorar-canvas-para-composicao-em-mixins.md](docs/adr/007-refatorar-canvas-para-composicao-em-mixins.md).

## Ferramentas e interação

O projeto agora conta com um sistema inicial de ferramentas que controlam modos de interação no `Canvas`. A funcionalidade `SelectTool` foi adicionada para permitir seleção e movimentação direta de pontos por arraste. Consulte a ADR que registra essa implementação em [docs/adr/008-adicionar-selecttool-para-mover-pontos.md](docs/adr/008-adicionar-selecttool-para-mover-pontos.md).

## Requisitos

- Python 3.11+
- uv

## Como executar

1. Instale o uv, se ainda não estiver disponível:

```bash
pip install uv
```

2. Crie e sincronize o ambiente do projeto:

```bash
uv sync
```

3. Execute a aplicação:

```bash
uv run coordinate_mapper
```

## Fluxo de uso

1. Abra uma imagem.
2. Clique na imagem para adicionar pontos.
3. Use o clique direito para remover o último ponto marcado.
4. Pressione Ctrl+S para salvar o projeto em um arquivo JSON.

## Exemplo de saída

O arquivo JSON gerado contém:

```json
{
  "image": {
    "path": "/caminho/da/imagem.png",
    "width": 1920,
    "height": 1080
  },
  "points": [
    {
      "id": 1,
      "x": 320,
      "y": 480,
      "group": "default"
    }
  ]
}
```

## Status do projeto

Este projeto está em fase inicial, com foco em simplicidade e extensibilidade. Novas funcionalidades podem ser adicionadas conforme a necessidade do uso.

## Licença

Este projeto é livre para uso, adaptação e experimentação. Se desejar, você pode expandir e publicar versões derivadas com suas próprias melhorias.
