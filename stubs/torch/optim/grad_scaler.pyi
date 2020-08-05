# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from torch import device, Tensor

class GradScaler(object):
    def __init__(self, init_scale: Optional[float]=..., growth_factor: Optional[float]=..., backoff_factor:Optional[float]=...,
                 growth_interval: Optional[int]=...,
                 enabled: Optional[bool]=...) -> None: ...

class _MultiDeviceReplicator(object):
    def __init__(self, master_tensor: Tensor=...) -> None: ...
    def get(self, device: device=...) -> Tensor: ...
