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
- Armazenamento de metadata da imagem (caminho, largura e altura)
- Exportação para JSON estruturado
- Estrutura modular para expansão futura

## Estrutura do projeto

- main.py: ponto de entrada da aplicação
- canvas.py: lógica da interface e interação com a imagem
- models.py: modelo de dados para os pontos
- storage.py: persistência em disco em formato JSON

## Requisitos

- Python 3.11+
- PySide6

## Como executar

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python main.py
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
