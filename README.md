# 🏫 Escola Inteligente

Sistema web desenvolvido para facilitar o **registro, gerenciamento e acompanhamento de problemas relacionados à infraestrutura escolar**.

O projeto permite que alunos e colaboradores registrem ocorrências de forma simples pelo celular, incluindo informações sobre o problema e uma foto. A equipe responsável possui uma área administrativa para acompanhar, editar, atualizar o status e gerenciar as ocorrências.

🌐 **Sistema online:**  
https://escola-inteligente-django-one.vercel.app/

---

## 🎓 Projeto Acadêmico

Projeto desenvolvido no contexto da disciplina **APIEx III**, com o tema:

**Cidades Inteligentes e Prototipagem de Soluções**

A proposta utiliza tecnologia para melhorar a comunicação entre a comunidade escolar e os responsáveis pela manutenção da infraestrutura.

**Aluno:** Edison Campos Cavalcante  
**Matrícula:** 01704611

---

## 💡 Problema

Problemas de infraestrutura podem ser comunicados informalmente e acabar demorando para chegar aos responsáveis pela manutenção.

Alguns exemplos:

- 💡 Lâmpadas queimadas
- 🌀 Ventiladores quebrados
- 🚰 Torneiras com vazamento
- 🪑 Móveis danificados
- 🖥️ Equipamentos com defeito
- 🧹 Problemas de limpeza
- 🔧 Outros problemas de infraestrutura

O **Escola Inteligente** busca tornar esse processo mais rápido, organizado e fácil de acompanhar.

---

## 💡 Solução

A solução consiste em disponibilizar um **QR Code** em pontos estratégicos da escola.

Ao escanear o código com o celular, o usuário é direcionado diretamente para o formulário de registro de ocorrências.

O fluxo funciona da seguinte maneira:

```text
QR Code
   ↓
Formulário de ocorrência
   ↓
Registro do problema
   ↓
Banco de dados
   ↓
Painel administrativo
   ↓
Atualização do status
   ↓
Acompanhamento
```

---

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
- Acesso direto pelo QR Code

### 🔐 Área administrativa

- Login administrativo
- Painel de gerenciamento
- Pesquisa de ocorrências por local
- Filtro por status
- Filtro por categoria
- Filtro por prioridade
- Visualização das fotos
- Edição das ocorrências
- Substituição da foto
- Alteração do status
- Exclusão de ocorrências
- Controle de acesso exclusivo para administradores

---

## 📊 Status das ocorrências

Cada ocorrência pode possuir um dos seguintes status:

- 🟡 **Pendente**
- 🔵 **Em análise**
- 🟢 **Resolvido**

Isso permite acompanhar o andamento de cada problema registrado.

---

## 🗂️ Categorias

As ocorrências podem ser classificadas como:

- ⚡ Elétrica
- 🚰 Hidráulica
- 🪑 Mobiliário
- 🧹 Limpeza
- 🖥️ Equipamento
- 🔧 Outro

---

## 📸 Registro com foto

O usuário pode adicionar uma foto ao registrar uma ocorrência.

As imagens são armazenadas utilizando o **Vercel Blob**, permitindo que continuem disponíveis mesmo após novos deploys da aplicação.

Quando uma ocorrência é editada, o administrador também pode enviar uma nova foto.

---

## 📱 QR Code

O projeto utiliza um QR Code para permitir acesso rápido ao formulário pelo celular.

Ao escanear o código, o usuário é direcionado diretamente para:

https://escola-inteligente-django-one.vercel.app/registrar/

Assim, não é necessário pesquisar ou digitar manualmente o endereço do sistema.

---

## 🛠️ Tecnologias utilizadas

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3

### Banco de dados

- SQLite para desenvolvimento local
- PostgreSQL com Neon em produção

### Armazenamento de imagens

- Vercel Blob

### Deploy e infraestrutura

- Vercel
- WhiteNoise

### Bibliotecas e ferramentas

- Pillow
- dj-database-url
- psycopg2-binary
- Vercel Python SDK
- Git
- GitHub

---

## ☁️ Arquitetura do projeto

```text
Usuário
   │
   ▼
QR Code
   │
   ▼
Aplicação Django
   │
   ├──────────────► Vercel Blob
   │                 │
   │                 └── Fotos
   │
   ▼
Neon PostgreSQL
   │
   └── Dados das ocorrências
```

A aplicação Django é hospedada na **Vercel**, os dados são armazenados no **Neon PostgreSQL** e as imagens são armazenadas no **Vercel Blob**.

---

## 📁 Estrutura principal

```text
Escola Inteligente/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
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
```

---

## 💻 Executando localmente

Clone o repositório:

```bash
git clone https://github.com/EdisonC-Dev/escola-inteligente-django.git
```

Entre na pasta do projeto:

```bash
cd escola-inteligente-django
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute as migrations:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A aplicação estará disponível localmente em:

```text
http://127.0.0.1:8000/
```

> Para realizar upload de imagens pelo Vercel Blob durante o desenvolvimento local, é necessário configurar a variável de ambiente correspondente ao Blob.

---

## 🔒 Segurança

Informações sensíveis não são armazenadas diretamente no código-fonte.

O projeto utiliza variáveis de ambiente para configurações como:

- `SECRET_KEY`
- `DATABASE_URL`
- `BLOB_READ_WRITE_TOKEN`
- `DEBUG`

O arquivo `.env` e outros arquivos locais sensíveis são ignorados pelo Git.

Em produção, o Django utiliza `DEBUG=False`.

---

## 🌐 Deploy

A aplicação está publicada utilizando a **Vercel**.

### Produção

https://escola-inteligente-django-one.vercel.app/

### Registrar uma ocorrência

https://escola-inteligente-django-one.vercel.app/registrar/

---

## 🎯 Objetivo do protótipo

O objetivo é demonstrar como uma solução digital simples pode contribuir para uma **escola mais inteligente, organizada e participativa**, facilitando a identificação de problemas e o acompanhamento das ações necessárias.

---

## 👨‍💻 Autor

**Edison Campos Cavalcante**  
Matrícula: **01704611**

Projeto acadêmico — **APIEx III**  
**Cidades Inteligentes e Prototipagem de Soluções**

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos e educacionais.