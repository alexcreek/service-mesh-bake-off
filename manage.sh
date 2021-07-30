#!/bin/bash
if [[ "$#" -lt 1 ]]; then
  echo "usage: $(basename "$0") istio|linkerd [create|destroy|stop|start|list]"
  exit 1
fi

SM=$1
ACTION=$2

run_terraform() {
  if ! [[ "$1" =~ apply|destroy ]]; then
    echo "Error: run_terraform(): $1 is not valid input"
    exit 1
  fi
  rm -rf .terraform
  terraform -chdir=terraform init -backend-config=../"$2"/backend.tfvars
  terraform -chdir=terraform "$1" -var-file=../"$2"/terraform.tfvars
}

case "$ACTION" in
  create)
    run_terraform 'apply' "$SM"
    ;;
  destroy)
    run_terraform 'destroy' "$SM"
    ;;
  stop)
    aws lightsail get-instances --query 'instances[*].name' --output json | jq .[] | grep istio | xargs -n1 aws lightsail stop-instance --instance-name
    ;;
  start)
    aws lightsail get-instances --query 'instances[*].name' --output json | jq .[] | grep istio | xargs -n1 aws lightsail start-instance --instance-name
    aws lightsail get-instances --query 'instances[*].[publicIpAddress,name]'
    ;;
  list)
    aws lightsail get-instances --query 'instances[*].[publicIpAddress,name]'
    ;;
  *)
esac
