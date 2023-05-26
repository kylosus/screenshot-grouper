# Screenshot grouper

Have too many mpv screenshots and want to group them into dirs based on seasons?
This script uses a contrived regex to do just that. The regex is not perfect, and
misses some files occasionally because torrent filenames are very inconsistent.

```bash
usage: main.py [-h] [--groups_dir GROUPS_DIR] [--dry-run] screenshots_dir

Organizes screenshots into groups based on filename

positional arguments:
  screenshots_dir       Path to screenshots

options:
  -h, --help            show this help message and exit

  --groups_dir GROUPS_DIR
                        Path to place groups in
  --dry-run
```

Looks like this

![](https://github.com/kylosus/screenshot-grouper/assets/33132401/28dd5c2e-75aa-4907-8d86-f63f9febab87)
