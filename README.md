# 🏫 Escola Inteligente

Sistema web desenvolvido para facilitar o registro e o acompanhamento de problemas relacionados à infraestrutura escolar.

O projeto permite que alunos e colaboradores registrem ocorrências de maneira simples, incluindo informações sobre o problema e uma foto. A equipe responsável pode acessar um painel administrativo para acompanhar, editar e atualizar a situação das ocorrências.

## 🎓 Projeto Acadêmico

Projeto desenvolvido no contexto da disciplina **APIEx III**, com o tema:

**Cidades Inteligentes e Prototipagem de Soluções**

A proposta é utilizar tecnologia para melhorar a comunicação entre a comunidade escolar e os responsáveis pela manutenção da infraestrutura.

## 💡 Problema

Problemas como:

- lâmpadas queimadas;
- ventiladores quebrados;
- torneiras com vazamento;
- móveis danificados;
- equipamentos com defeito;
- problemas de limpeza;

podem demorar para chegar até os responsáveis pela manutenção.

O Escola Inteligente busca tornar esse processo mais simples e organizado.

## 🚀 Funcionalidades

### 👤 Área pública

- Registro de novas ocorrências
- Seleção do local do problema
- Seleção da categoria
- Descrição do problema
- Definição da prioridade
- Envio de foto
- Acompanhamento das ocorrências
- Visualização do status

### 🔐 Área administrativa

- Login administrativo
- Painel de ocorrências
- Pesquisa por local
- Filtro por status
- Filtro por categoria
- Filtro por prioridade
- Visualização das fotos
- Edição das ocorrências
- Alteração do status
- Exclusão de ocorrências
- Controle de acesso para administradores

## 📊 Status das ocorrências

Cada ocorrência pode possuir um dos seguintes status:

- 🟡 Pendente
- 🔵 Em análise
- 🟢 Resolvido

## 🗂️ Categorias

As ocorrências podem ser classificadas como:

- Elétrica
- Hidráulica
- Mobiliário
- Limpeza
- Equipamento
- Outro

## 📱 QR Code

A proposta do projeto utiliza um **QR Code** para facilitar o acesso ao formulário.

O QR Code poderá ser colocado em pontos estratégicos da escola. Ao escaneá-lo com o celular, o usuário será direcionado para a página de registro de ocorrências.

Fluxo:

QR Code → Formulário → Registro do problema → Acompanhamento → Resolução

## 🛠️ Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- SQLite
- Pillow
- WhiteNoise
- Git
- GitHub

## 📁 Estrutura principal

```text
Escola Inteligente/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ocorrencias/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md