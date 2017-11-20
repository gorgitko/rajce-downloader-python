# rajce-downloader-python
Simple command-line tool and library for downloading whole albums from rajce.net

# Installation
Download this repository and run `$ python setup.py install`

That will install both Python library (package `rajce_downloader`) and CLI (available as `$ rajce_downloader`).

# Command-line interface
See `$ rajce_downloader -h`

# Library
See `download_album` in [rajce_downloader.py](rajce_downloader/rajce_downloader.py)

```python
from rajce_downloader import download_album

# download_album returns list of paths to downloaded images
r = download_album("http://lidondr.rajce.idnes.cz/Liberec_2017", "c:/Temp/Liberec2017", n_images=10, overwrite=False)
print(r)
```
