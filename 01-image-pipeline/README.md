# Image Pipeline

Generate an image with Flux 1.1 Pro and remove its background with rembg — in two API calls.

## What this does

1. **`/image/generate`** — Generate image from text prompt (Flux 1.1 Pro)
2. **`/image/remove-bg`** — Remove background with rembg AI

## Cost
- Image generation: $0.005/call
- Background removal: $0.003/call
- **Total: ~$0.008 per image**

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Shell version
bash generate-and-remove-bg.sh "a red sports car in a showroom"

# Python version
python3 generate-and-remove-bg.py "a red sports car in a showroom"
```

## Expected Output

```
Generating image...
Image URL: https://storage.iteratools.com/images/abc123.png

Removing background...
Result URL: https://storage.iteratools.com/images/abc123-nobg.png

Done! Transparent PNG saved.
```
