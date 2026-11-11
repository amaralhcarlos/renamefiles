# renamefiles

Aplicativo simples (interface gráfica em Tkinter) para remover acentos dos nomes de arquivos de uma pasta.

## Uso

```
python3 rename_files.py
```

1. Clique em "Procurar..." e selecione a pasta.
2. Clique em "Renomear arquivos".
3. O log mostra o que foi renomeado, o que foi ignorado (sem acento) e conflitos (quando o nome sem acento já existe na pasta).

## Requisitos

- Python 3 com Tkinter (`python3-tk` no Linux).

## Releases

Builds prontos (executável, sem precisar instalar Python) são publicados automaticamente para Linux e Windows a cada nova tag:

```
git tag v1.0.0
git push origin v1.0.0
```

Isso dispara a Action em `.github/workflows/release.yml`, que gera e publica:

- `renamefiles-linux`
- `renamefiles-windows.exe`

na página de Releases do repositório.
