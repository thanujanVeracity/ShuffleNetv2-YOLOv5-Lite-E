import torch
from  torch.utils.mobile_optimizer import optimize_for_mobile

model = torch.load(r"runs/train/exp3/weights/best.torchscript")
model.eval()

scripted_model = torch.jit.script(model)

optimized_scripted_model = optimize_for_mobile(scripted_model)
optimized_scripted_model._save_for_lite_interpreter(r"runs/train/exp3/weights/best.torchscript.ptl")