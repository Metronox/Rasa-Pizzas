# 🍕 Rasa-Pizzas

Chatbot de pizzaria em português, feito com [Rasa Open Source](https://rasa.com/). Ele conversa com o cliente, anota o pedido (sabor, tamanho e borda), valida as opções, pede confirmação e simula o tempo de entrega.

> Projeto de estudo sobre processamento de linguagem natural e chatbots.

## O que o bot faz

- Cumprimenta o cliente e se despede
- Entende a intenção do cliente: fazer pedido, informar sabor, tamanho e borda, confirmar, cancelar e agradecer
- Extrai **sabor**, **tamanho** e **borda** do texto, usando entidades e slots
- Valida o pedido com ações customizadas em Python:
  - **Sabor:** portuguesa, calabresa, frango, mussarela, margherita e picanha
  - **Tamanho:** pequena, média (com ou sem acento) e grande
  - Se a opção não existir, o bot avisa e pede de novo
- Pergunta o tipo de borda: recheada, vulcão, fina ou sem borda
- Resume o pedido e pede confirmação
- Simula o tempo de entrega, que varia com o tamanho da pizza

## Tecnologias

- Python
- Rasa Open Source e Rasa SDK (ações customizadas)
- Pipeline de NLU em português, com `DIETClassifier`, `TEDPolicy` e `RulePolicy`

## Estrutura do projeto

```
Rasa-Pizzas/
├── actions/
│   └── actions.py     # ações customizadas (validar sabor e tamanho, simular entrega)
├── data/
│   ├── nlu.yml        # exemplos de frases para cada intenção
│   ├── stories.yml    # conversas de exemplo
│   └── rules.yml      # regras de diálogo
├── config.yml         # pipeline de NLU e políticas
├── domain.yml         # intenções, entidades, slots, respostas e ações
└── endpoints.yml      # endpoint das ações customizadas
```

## Como rodar

Você precisa de Python e de uma versão do Rasa compatível com a sua versão do Python (veja a [documentação do Rasa](https://rasa.com/docs/rasa/installation/installing-rasa-open-source)).

1. Clone o repositório

   ```bash
   git clone https://github.com/Metronox/Rasa-Pizzas.git
   cd Rasa-Pizzas
   ```

2. Crie um ambiente virtual e instale o Rasa

   ```bash
   python -m venv venv
   source venv/bin/activate        # no Windows: venv\Scripts\activate
   pip install rasa
   ```

3. Treine o modelo

   ```bash
   rasa train
   ```

4. Em um terminal, inicie o servidor de ações

   ```bash
   rasa run actions
   ```

5. Em outro terminal, converse com o bot

   ```bash
   rasa shell
   ```

## Exemplo de conversa

```
Você: oi
Bot:  Oi, seja bem vindo a nossa pizzaria. Como posso te ajudar?
Você: quero uma pizza de calabresa
Bot:  Boa escolha! Pizza de calabresa é nossa especialidade.
```
