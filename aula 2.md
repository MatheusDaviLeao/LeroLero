# Controle de versão

- Desempenho excelente;
- Todas as funcionalidades imagináveis existem;
- Hoje em dia, multiplataforma;
- Permite integrar fluxo de desenvolvimento e de implementação/operação;
- Viabializa fluxo de trabalho;
- Projetos livres migraram em massa
- Até a Microsoft está usando, além de ter comprado o Github

> "Mas na verdade o git é uma merda" (CSSL, Nelson)

- Os nomes dos comandos e suas opções são inconsistentes

- A documentação é voa e completa, mas é preciso saver *onde* procurar


## Mãos na massa

##### Primeiros passos
```bash
git config --local user.name "Seu nome"
git config --local user.mail "email@provedor.com"
```
Configurando a pasta ssh

```bash
ssh-keygen
```

Esse comando gera uma nova chave `ssh`


```bash
git init .          // Inicializa o diretório atual como repositório git
git remote add origin <REPO.GIT.URL>
```


É bom criar um arquivo README no seu git:
```bash
git add README.md
git add <file-name>
git commit -m "Mensagem sobre a alteração"
git push origin master // copia o repositório local para o remoto
```

Ou, para adicionar um repositório remoto, 
```bash
git clone https://github.com/urrameu/lerolero.git
```

Para verificar o status atual do repositório e exibir as alterações (comitadas ou não), use o comando 

```bash
git status
git commit //copia o conteudo da area de montagem
```

Usamos o `git diff` para exibir o que há de diferente entre o repositório local e o repositório remoto:

```bash
git diff
git diff ID
git diff --staged
```


Para exibir o histórico de alterações e commits, use o comando:
```bash
git log
```

```bash
vi lerolero.py
git status
git diff
git add lerolero.py
git diff --staged
git push
git status
```


```bash
git branch <NOME> // cria um novo branch
git switch <NOME> // alterna entre branchs
git branch        // exibe lista com todas as branchs

```

