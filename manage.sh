#!/bin/bash
if [[ "$#" -lt 1 ]]; then
  echo "usage: $(basename "$0") istio|linkerd [destroy|shutdown|stop|start|info]"
  exit 1
fi

SM=$1
ACTION=${2:-apply}

case "$ACTION" in
  stop)
    aws lightsail get-instances --query 'instances[*].name' --output json | jq .[] | grep istio | xargs -n1 aws lightsail stop-instance --instance-name
    exit
    ;;
  start)
    aws lightsail get-instances --query 'instances[*].name' --output json | jq .[] | grep istio | xargs -n1 aws lightsail start-instance --instance-name
    aws lightsail get-instances --query 'instances[*].[publicIpAddress,name]'
    exit
    ;;
  info)
    aws lightsail get-instances --query 'instances[*].[publicIpAddress,name]'
    exit
    ;;
  *)
esac

rm -rf .terraform
terraform -chdir=terraform init -backend-config=../"$SM"/backend.tfvars
terraform -chdir=terraform "$ACTION" -var-file=../"$SM"/terraform.tfvars
