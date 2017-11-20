import requests
from bs4 import BeautifulSoup
import sys
from glob import glob
import os


def download_album(link, output_dir, overwrite=False, n_images=0):
    """
    Download album from rajce.net

    :param link: Link to rajce.net album.
    :param output_dir: Directory to save images. Will be created automatically.
    :param overwrite: If True, overwrite existing images.
    :param n_images: How many images to download. '0' to download all (default).

    :return: List of paths to saved images.
    """

    if not overwrite:
        existing_files = glob("{}/*".format(output_dir))
        existing_files = list(map(os.path.basename, existing_files))

    r = requests.get(link)

    if r.status_code == 200:
        html = BeautifulSoup(r.text, "html.parser")
        photo_list_div = html.find("div", id="photoList")
        img_links = photo_list_div.find_all("a")

        if n_images > 0:
            img_links = img_links[:n_images]

        n_img_links = len(img_links)
        saved_img_paths = []
        os.makedirs(output_dir, exist_ok=True)
    else:
        print("Cannot download album HTML (response {}).".format(r.status_code), file=sys.stderr)
        return []

    for i, img in enumerate(img_links):
        print("Processing image {}/{} ... ".format(i + 1, n_img_links), end="")

        url = img["href"]
        img_name = url.split("/")[-1]
        r = requests.get(url)
        if r.status_code == 200:
            if overwrite or (not overwrite and img_name not in existing_files):
                img_path = "{}/{}".format(output_dir, img_name)
                with open(img_path, "wb") as f:
                    f.write(r.content)
                saved_img_paths.append(img_path)
                print("Done")
            if not overwrite and img_name in existing_files:
                print("Image '{}' already exists, skipping".format(img_name))
        else:
            print("Failed")
            print("\tCannot download image {} (response {}).".format(url, r.status_code), file=sys.stderr)

    return saved_img_paths
