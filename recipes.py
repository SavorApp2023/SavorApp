from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float32,
)
pipe = pipe.to("cuda")

prompt = "a photograph of an astronaut riding a horse"
pipe.enable_attention_slicing()
image = pipe(prompt).images[0]

image.save("image.png")
print(type(image))
