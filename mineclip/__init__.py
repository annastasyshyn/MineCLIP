from .mineclip import MineCLIP

# optional: dense_reward and mineagent require minedojo
try:
    from .dense_reward import (
        AnimalZooDenseRewardWrapper,
        HuntCowDenseRewardEnv,
        MobCombatDenseRewardWrapper,
        CombatSpiderDenseRewardEnv,
    )
    from .mineagent import *
except ImportError:
    # minedojo not installed - dense reward wrappers unavailable
    pass
