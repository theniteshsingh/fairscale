from typing import Any

import torch
from torch.cuda.amp.grad_scaler import GradScaler


class FairscaleGradScaler(GradScaler):
    def _unscale_grads_(
        self, optimizer: torch.optim.Optimizer, inv_scale: float, found_inf: Any, allow_fp16: bool
    ) -> Any:
        return super()._unscale_grads_(optimizer, inv_scale, found_inf, allow_fp16=True)
