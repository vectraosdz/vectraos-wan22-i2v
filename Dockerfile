FROM runpod/worker-comfyui:5.8.6-base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/* 

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
ENV COMFYUI_PATH=/ComfyUI

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p \
    /app/input \
    /app/output \
    /app/tmp \
    /app/workflows/generated

RUN chmod +x /app/start.sh

RUN test -f /app/workflows/vectraos_wan2.2.json

EXPOSE 8188

CMD ["/app/start.sh"]
