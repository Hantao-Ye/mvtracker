# Copyright (c) ETH VLG.
# Licensed under the terms in the LICENSE file at the root of this repo.

# Forward-port logic that moved into the package, so we can use it programmatically
# without torch.hub if we want, but keep this entrypoint for torch.hub support.

dependencies = ["torch", "huggingface_hub"]

from mvtracker.api import (
    mvtracker_model,
    mvtracker_predictor,
    mvtracker,
    mvtracker_cleandepth
)
