from . import get_hw_model_as_number


def configure(env, features_wanted, defines, sources):
    features_available = []
    board = 'detahard_1.h'
    display = 'vg-2864ksweg01.c'
    hw_model = get_hw_model_as_number('T1B1')
    hw_revision = 0

    defines += [f'detahard_BOARD=\\"boards/{board}\\"', ]
    defines += [f'HW_MODEL={hw_model}', ]
    defines += [f'HW_REVISION={hw_revision}', ]
    sources += [f'embed/detahardhal/displays/{display}', ]

    if "input" in features_wanted:
        sources += ['embed/detahardhal/button.c']
        features_available.append("button")

    env.get('ENV')['detahard_BOARD'] = board

    return features_available
