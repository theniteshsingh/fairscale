# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

class GradScaler(object):
    def __init__(self, init_scale: Optional[float], growth_factor: Optional[float], backoff_factor:Optional[float],
                 growth_interval: Optional[int],
                 enabled: Optional[bool])
