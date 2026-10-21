#!/bin/bash
# Script de prueba local para Webhook Backend
WEBHOOK_URL=${1:-"http://localhost:8080"}

echo "=== Probando Endpoint del Webhook CSDC ==="
curl -X POST "$WEBHOOK_URL" \
     -H "Content-Type: application/json" \
     -d @tests/test_webhook_payload.json

echo -e "\n=== Prueba Finalizada ==="
