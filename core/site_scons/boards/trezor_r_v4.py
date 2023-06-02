from . import get_hw_model_as_number


def configure(env, features_wanted, defines, sources):
    features_available = []
    hw_model = get_hw_model_as_number('T2B1')
    hw_revision = 4
    board = 'detahard_r_v4.h'
    display = 'vg-2864ksweg01.c'

    defines += [f'detahard_BOARD=\\"boards/{board}\\"', ]
    defines += [f'HW_MODEL={hw_model}', ]
    defines += [f'HW_REVISION={hw_revision}', ]
    sources += [f'embed/detahardhal/displays/{display}', ]

    if "input" in features_wanted:
        sources += ['embed/detahardhal/button.c']
        features_available.append("button")

    if "sbu" in features_wanted:
        sources += ['embed/detahardhal/sbu.c', ]
        features_available.append("sbu")

    env.get('ENV')['detahard_BOARD'] = board

    return features_available
