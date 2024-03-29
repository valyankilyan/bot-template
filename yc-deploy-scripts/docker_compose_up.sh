#!/bin/bash
set -e

export PROJECT_DIR=${PROJECT_DIR:-"/var/otvali"}
export BOT_IMAGE=${BOT_IMAGE:-valyankilyan/bot_template:0.0.1}
export USER_WEBHOOK=${USER_WEBHOOK:-False}
export SECRET_ID=${SECRET_ID:-insert_secret_id}

source "${PROJECT_DIR}/.env"

export IAM_TOKEN=$(curl -H Metadata-Flavor:Google http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token | jq -r .access_token)

export SECRET_PAYLOAD=$(curl -X GET -H "Authorization: Bearer ${IAM_TOKEN}" https://payload.lockbox.api.cloud.yandex.net/lockbox/v1/secrets/${SECRET_ID}/payload)
: ${SECRET_PAYLOAD:?"SECRET_PAYLOAD could not be retrieved"}

export BOT_TOKEN=$(echo $SECRET_PAYLOAD | jq -r '.entries[] | select(.key=="BOT_TOKEN") | .textValue')
export ADMIN_PASSWORD=$(echo $SECRET_PAYLOAD | jq -r '.entries[] | select(.key=="admin-password") | .textValue')

export SQL_ENGINE_URL=sqlite://app.sqlite

docker-compose up -d