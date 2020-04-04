DEFAULT_OPERATIONS = [
    'rotate',
    'blur',
    'random_noise',
    'horizontal_flip',
    'vertical_flip',
    'cutout',
    'imagenetpolicy',
    'randaugment'
]

# Rotation configuration
DEFAULT_ROTATE_PROBABILITY = 0.5
DEFAULT_ROTATE_MAX_LEFT_DEGREE = 25
DEFAULT_ROTATE_MAX_RIGHT_DEGREE = 25

# Blur configuration
DEFAULT_BLUR_PROBABILITY = 0.1

# Random noise configuration
DEFAULT_RANDOM_NOISE_PROBABILITY = 0.5

# Horizontal flip configuration
DEFAULT_HORIZONTAL_FLIP_PROBABILITY = 0.3

# Horizontal flip configuration
DEFAULT_VERTICAL_FLIP_PROBABILITY = 0.3

# CutOut
DEFAULT_CUTOUT_SIZE = 16

# ImageNetPolicy
DEFAULT_IMAGENETPOLICY_FILLCOLOR = (128, 128, 128)

# RandAugmnet
DEFAULT_RANDAUGMENT_TRANS_LIST = [ 'Invert', 'Cutout', 'Sharpness', 'AutoContrast', 'Posterize',
                                   'ShearX', 'TranslateX', 'TranslateY', 'ShearY', 'Rotate',
                                   'Equalize', 'Contrast', 'Color', 'Solarize', 'Brightness']
