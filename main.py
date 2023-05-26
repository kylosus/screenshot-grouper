import argparse
import pprint
import re
import sys
from pathlib import Path

pattern = re.compile(
    r'(.*S\d\d?)|(?:(.*)[ -\.\_]{3}\d\d)|(.*)[\. -\_]E(?:pisode)?[\. -\_]?\d\d?|(.*)\.(?:mkv|mp4|webm)')

# Get arg
parser = argparse.ArgumentParser(description='Organizes screenshots into groups based on filename')
parser.add_argument('screenshots_dir', help='Path to screenshots', type=Path)
parser.add_argument('--groups_dir', help='Path to place groups in', type=Path, default='Groups')
parser.add_argument('--dry-run', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    screenshots_dir = args.screenshots_dir
    groups_dir = args.groups_dir
    dry_run = args.dry_run

    groups_path = screenshots_dir / groups_dir

    if not dry_run:
        groups_path.mkdir(exist_ok=True)

    total_moved = 0
    total_missed = 0
    unique_groups = set()

    for f in screenshots_dir.glob('*.png'):
        file_name = f.name
        match = re.match(pattern, file_name)

        if not match:
            print(f'{file_name} did not match', file=sys.stderr)
            total_missed += 1
            continue

        # Shouldn't fail
        group = next(item for item in match.groups() if item)
        group_dir = Path(groups_path / group)

        unique_groups.add(group)

        new_path = group_dir / file_name

        if not dry_run:
            group_dir.mkdir(exist_ok=True)
            f.rename(new_path)
        else:
            print(f'{f.name} -> {new_path.name}')

        total_moved += 1

    print()
    print('Groups:')
    pprint.pprint(list(sorted(unique_groups)), compact=True)
    print()

    print('Done')
    print(f'\tUnique groups: {len(unique_groups)}')
    print(f'\tTotal moved: {total_moved}')
    print(f'\tTotal missed: {total_missed}')
