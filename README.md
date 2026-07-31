# WAN 2.2 RunPod Serverless Worker

## Structure

```
.
├── handler.py
├── config.py
├── Dockerfile
├── start.sh
├── requirements.txt
├── workflows
│   └── vectraos_wan2.2.json
├── input
├── output
├── tmp
└── utils
    ├── cleanup.py
    ├── comfy.py
    ├── download.py
    ├── logger.py
    ├── product_detector.py
    ├── prompt_builder.py
    ├── validator.py
    ├── video_profiles.py
    └── workflow.py
```

## Build

```bash
docker build -t wan22-worker .
```

## Test

```bash
docker run -p 8188:8188 wan22-worker
```

## RunPod Input

```json
{
  "input": {
    "image_url": "https://example.com/image.jpg",
    "quality": "balanced",
    "language": "English",
    "parallel": true
  }
}
```

## Response

```json
{
  "success": true,
  "video_count": 3,
  "videos": [
    {
      "name": "orbit",
      "base64": "..."
    },
    {
      "name": "macro",
      "base64": "..."
    },
    {
      "name": "lifestyle",
      "base64": "..."
    }
  ]
}
```
