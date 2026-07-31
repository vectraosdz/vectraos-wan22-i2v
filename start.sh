#!/usr/bin/env bash

set -e

echo "======================================"
echo "WAN 2.2 RunPod Worker"
echo "======================================"

mkdir -p /app/input
mkdir -p /app/output
mkdir -p /app/tmp
mkdir -p /app/workflows/generated

echo "Starting ComfyUI..."

python /ComfyUI/main.py \
    --listen 0.0.0.0 \
    --port 8188 \
    >/tmp/comfyui.log 2>&1 &

echo "Waiting for ComfyUI..."

until curl -s http://127.0.0.1:8188/system_stats >/dev/null
do
    sleep 2
done

echo "ComfyUI Ready"

if [ ! -f /app/workflows/vectraos_wan2.2.json ]; then
    echo "ERROR: workflows/vectraos_wan2.2.json not found"
    exit 1
fi

echo "Starting RunPod Worker..."

exec python /app/handler.py
