from pycheckstyle import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True)
parser.add_argument('--config')
parser.add_argument('--default', choices=['sun', 'google'], default='sun')

args = parser.parse_args()
if __name__ == "__main__":
    path = args.path
    config = args.config
    default_std_name = args.default
    assert path is not None

    print("Checking", path, '...')

    default_std = SunStandard if default_std_name == 'sun' else GoogleStandard
    std = CheckStandard(config) if config is not None else default_std()
    check_res = std.check(path)
    if len(check_res) > 0:
        for message in check_res:
            print(message.level, message.type, message.message)
            print(message.position)
        exit(1)
