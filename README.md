# rajce-downloader-python
Simple command-line tool and library for downloading whole albums from rajce.net

# Installation
Download this repository and run `$ python setup.py install`

# Command-line interface
See `rajce_downloader -h`

# Library
See `download_album` in [rajce_downloader.py](rajce_downloader/rajce_downloader.py)

```python
from rajce_downloader import download_album


r = download_album("http://lidondr.rajce.idnes.cz/Liberec_2017", "c:/Temp/Liberec2017", n_images=0, overwrite=True)

# download_album returns list of paths of downloaded images
print(r)
```
