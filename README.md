# acr-uncrustify

Extensao que verifica a identacao de arquivos usando a ferramenta uncrustify

1. Propriedade config se refere ao caminho para o arquivo .cfg do uncrustify
2. Propriedade regexFile é em quais arquivos vai executar a verificação
3. Propriedade regexIgnore é quais arquivos devem ser ignorados mesmo que se enquadrem no regexFile

Arquivo config.json

```json
{
  "regexFile": "",
  "regexIgnore": [
  ],
  "config": ""
}

```

Dependencias

- uncrustify

```shell
sudo apt-get install uncrustify
```
