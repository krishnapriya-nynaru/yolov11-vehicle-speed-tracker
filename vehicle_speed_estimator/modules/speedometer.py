from collections import defaultdict
import numpy as np

class Speedometer:
    def __init__(self, mapper, fps, unit):
        self.mapper = mapper
        self.fps = fps
        self.unit = unit
        self.speeds = defaultdict(list)

    def update_with_trace(self, idx, image_trace):
        if len(image_trace) > 1:
            world_trace = self.mapper.map(image_trace)
            dx, dy = np.median(np.abs(np.diff(world_trace, axis=0)), axis=0)
            ds = np.linalg.norm([dx, dy])
            self.speeds[idx].append(int(ds * self.fps * self.unit))

    def get_current_speed(self, idx):
        return self.speeds[idx][-1] if self.speeds[idx] else 0
