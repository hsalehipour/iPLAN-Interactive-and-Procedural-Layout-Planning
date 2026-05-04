# `from .floorplan_rnn import FloorPlanRNN` is intentionally NOT done here:
# floorplan_rnn.py uses `import utils`, which only resolves when the working
# directory happens to be `room_partition/`. Inference paths use the test
# wrapper below, which imports `from room_partition import utils` correctly.
from .floorplan_rnn_test import FloorPlanRNN as FloorPlanRNNTest  # noqa: F401
