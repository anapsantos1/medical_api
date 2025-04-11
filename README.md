# 🏥 API de Gerenciamento de Consultas Médicas

API RESTful para gerenciamento de profissionais da saúde, pacientes e consultas médicas.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12+
- Django 5.x
- Django REST Framework
- PostgreSQL
- Docker
- JWT (via `djangorestframework-simplejwt`)
- Swagger (via `drf-yasg`)

---

## 📦 Organização em Apps

| App            | Função                                              |
|----------------|-----------------------------------------------------|
| `users`        | Gerenciamento de usuários e autenticação JWT        |
| `professionals`| Cadastro de profissionais e especialidades          |
| `appointments` | Cadastro de pacientes e consultas médicas           |

---

## 📚 Documentação Swagger

Após executar o projeto, acesse:

```
http://localhost:8000/swagger/
```

---

## 🔐 Autenticação

Utiliza JWT. Endpoints:

- `POST /api/token/`: Geração de token
- `POST /api/token/refresh/`: Refresh do token

---

## 🔄 Endpoints

### 🔹 Usuários

- `POST /api/users/register/`: Registro de novo usuário

### 🔹 Autenticação

- `POST /api/token/`: Geração de token
- `POST /api/token/refresh/`: Atualização de token

### 🔹 Profissionais

- `GET /api/professionals/`: Lista todos os profissionais
- `GET /api/professionals/<id>/`: Detalhes de um profissional
- `POST /api/professionals/`: Criação de novo profissional
- `PUT /api/professionals/`: Atualização de profissional
- `DELETE /api/professionals/`: Exclusão de profissional

### 🔹 Especialidades

- `GET /api/appointments/especialidades/`: Lista todas as especialidades
- `POST /api/appointments/especialidades/`: Criação de especialidade
- `PUT /api/appointments/especialidades/`: Atualização de especialidade
- `DELETE /api/appointments/especialidades/`: Exclusão de especialidade

### 🔹 Pacientes

- `GET /api/appointments/pacientes/`: Lista todos os pacientes
- `GET /consultas/por_paciente/<id>/`: Consultas por paciente (ID)
- `GET /consultas/por_paciente/<cpf>/`: Consultas por paciente (CPF)
- `POST /api/appointments/pacientes/`: Criação de paciente
- `PUT /api/appointments/pacientes/`: Atualização de paciente
- `DELETE /api/appointments/pacientes/`: Exclusão de paciente

### 🔹 Consultas

- `GET /consultas/`: Lista todas as consultas
- `GET /consultas/<id>/`: Detalhes da consulta
- `GET /consultas/pacientes/`: Consultas agrupadas por paciente
- `GET /consultas/especialidades/`: Consultas agrupadas por especialidade
- `GET /consultas/por_professionals/<id>/`: Consultas por profissional
- `POST /api/appointments/consultas/`: Criação de nova consulta
- `PUT /api/appointments/consultas/`: Atualização de consulta
- `DELETE /api/appointments/consultas/`: Exclusão de consulta

---

## ⚠️ Problemas e Soluções

| Problema                                    | Solução                                                                 |
|--------------------------------------------|-------------------------------------------------------------------------|
| ViewSets exibindo rotas incompletas         | Adição de métodos `get_queryset()` específicos                         |
| Falta de rota `/swagger/`                   | Instalação e configuração do `drf-yasg`                                |
| Separação incorreta de modelos              | Refatoração dos modelos e redistribuição correta entre os apps         |
| Busca de consultas por CPF                  | Implementação de rota customizada com filtro no serializer             |
| PUT e DELETE não funcionando                | Adição de métodos `update()` e `destroy()` nos `ViewSets`              |

---

## 🚀 Futuras Melhorias

- Filtros por intervalo de datas em consultas
- Dashboard de estatísticas por profissional
- Notificações de consultas próximas
- Integração com frontend (React ou Next.js)

---

Para mais dúvidas ou colaboração, abra uma issue ou entre em contato com a equipe de desenvolvimento.