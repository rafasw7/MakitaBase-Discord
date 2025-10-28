# Makita Base — Discord

![Makita Logo](https://github.com/user-attachments/assets/b662c226-f336-4dd1-980d-cfe52fb158f1)

[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)]()
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![discord.py](https://img.shields.io/badge/discord.py-5865F2?style=for-the-badge&logo=discord&logoColor=white)]()

Um bot de Discord modular, leve e fácil de estender, feito por Raphael (rafasw7) com a biblioteca discord.py. Esta base (Makita Base — Discord) traz um exemplo de arquitetura por cogs e um comando de ping interativo com botões.

✨ Pronto para produção, compatível com Termux, e fácil de personalizar. ✨

---

## Índice

- Sobre
- Recursos
- Requisitos
- Instalação rápida
- Como obter o token (Developer Portal)
- Configuração (config.json)
- Estrutura do projeto
- Arquivos incluídos (bot.py / cogs/ping.py)
- Executando o bot
- Boas práticas & segurança
- Contribuição
- Autor & Contato
- Licença

---

## Sobre

A Makita Base — Discord é um esqueleto para construir bots robustos e organizados. Ela utiliza cogs (extensões) para separar funcionalidades e um exemplo interativo de `ping` que usa `discord.ui.View` para mostrar latência, uptime e botões para atualizar/fechar o painel.

---

## Recursos

- Arquitetura modular com cogs
- Comando `!ping` com embed interativo (botões: Repetir Teste / Fechar)
- Tratamento de início e desligamento limpo (asyncio)
- Compatível com Termux, Linux e Windows
- Estrutura simples para adicionar novos cogs e respostas multimídia
- Placeholder para assets (gifs/imagens) em `assets/`

---

## Requisitos

- Python 3.11+ (recomendado)
- pip
- Conta no Discord Developer Portal e um Bot Token
- Biblioteca: discord.py (v2.x)

---

## Instalação rápida

1. Clone o repositório:
```bash
git clone https://github.com/rafasw7/Makita-Discord.git
cd Makita-Discord
```

2. Instale as dependências:
```bash
pip install -U discord.py
```

(Se usar Termux no Android: `pkg install python git -y` antes dos passos acima.)

---

## Como obter o token no Discord Developer Portal

Siga este passo a passo para pegar o token do seu bot:

1. Acesse o Developer Portal: https://discord.com/developers/applications e faça login.  
2. Clique em "New Application", dê um nome (ex.: Makita Discord) e confirme em "Create".  
3. No menu lateral da aplicação, clique em "Bot" → "Add Bot" → "Yes, do it!".  
4. Na seção "TOKEN", clique em "Copy" para copiar o token do bot.  
5. Cole esse token no arquivo `config.json` (exemplo abaixo).  
6. Se o token vazar, volte ao Developer Portal → Bot → "Regenerate" para gerar um novo token.  
7. Habilite intents se necessário (Message Content Intent / Server Members Intent) em "Privileged Gateway Intents" na mesma página do Bot e ative as intents correspondentes no código.

Dica: não compartilhe o token e não publique `config.json` em repositórios públicos.

---

## Configuração (config.json)

Crie um arquivo `config.json` na raiz do projeto com o conteúdo abaixo (somente o token é necessário — o prefixo é tratado no código):

```json
{
  "token": "SEU_TOKEN_AQUI"
}
```

Adicione `config.json` ao `.gitignore` para evitar commits acidentais:

```
config.json
```

---

## Estrutura do projeto

```
Makita-Discord/
├── assets/                # imagens/gifs usados no README e respostas (ex: makita-discord.gif)
├── cogs/                  # cogs / extensões do bot (ex: ping.py)
├── config.json            # token do bot (NÃO comitar)
├── bot.py                 # arquivo principal (inicia o bot e carrega cogs)
├── README.md
└── LICENSE
```

Observação: o prefixo de comandos está definido diretamente em `bot.py` (padrão `!`). Se quiser alterar o prefixo, edite `bot.py`.

---

## Arquivos incluídos

Incluí dois arquivos essenciais neste repositório:

- `bot.py` — inicia o bot, carrega cogs automaticamente e começa o bot usando `config.json`.
- `cogs/ping.py` — cog de exemplo com `PingView` (botões) e comando `!ping`.

Os conteúdos desses arquivos estão na raiz do repositório (veja os exemplos abaixo).

---

## Executando o bot

Depois de preencher `config.json` e instalar `discord.py`:

```bash
python bot.py
```

No console você verá uma mensagem indicando que o bot está online. No Discord, use `!ping` no chat do servidor onde o bot está para abrir o painel interativo.

---

## Boas práticas & segurança

- Nunca compartilhe o token do bot. Se vazar, regenere no Developer Portal.  
- Adicione `config.json` no `.gitignore`.  
- Habilite apenas intents necessárias no Developer Portal; ative as mesmas intents no código.  
- Para produção, utilize um process manager (systemd, pm2, supervisor) para garantir reinício automático.  
- Fixe permissões mínimas ao convidar o bot (OAuth2 → Permissions).

---

## Contribuição

Contribuições são bem-vindas:

- Abra uma issue descrevendo a sugestão/bug.  
- Faça um fork, crie uma branch com a feature/fix e abra um PR.

Posso criar um CONTRIBUTING.md se quiser padronizar o fluxo.

---

## Autor & Contato

Feito com ❤️ por Raphael (rafasw7)  
Instagram: @rafasw7  
WhatsApp: +55 62 8205-3713

---


## Agradecimentos

Criei esta base com muito carinho para a comunidade. Espero que aproveitem e construam coisas incríveis!

— Raphael (@rafasw7)

Se gostou, não esqueça de dar uma estrela no repositório!

<p align="center">
  <img src="https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUyNmdnbTZybGh1M2NiNXlyczF5ZTR2eDhlaG1lMHVqbG5zem1mODdlZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gDyCnwdmwgR36UAq8y/giphy.gif" alt="Makita em obra - animado" width="420" style="border-radius: 12px;">
</p>
