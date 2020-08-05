# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from torch import device, Tensor

class GradScaler(object):
    def _unscale_grads_(self, optimizer: torch.optim.Optimizer=..., inv_scale: float=..., found_inf: Any=..., allow_fp16: bool=...
    ) -> Any: ...
