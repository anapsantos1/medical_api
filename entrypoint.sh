#!/bin/sh

echo "Esperando pelo banco de dados..."

# Aguarda a disponibilidade do banco
while ! nc -z $MEDICAL_HOST $MEDICAL_PORT; do
  sleep 1
done

echo "Banco de dados disponível. Rodando migrações..."

# Executa as migrações e inicia o servidor
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
