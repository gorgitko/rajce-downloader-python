import argparse
from rajce_downloader import download_album


def cli():
    parser = argparse.ArgumentParser(description="Save album from rajce.net")
    parser.add_argument("link", type=str, help="Link to album.")
    parser.add_argument("output_dir", type=str, help="Directory to save images in.")
    parser.add_argument("-f", "--force-write", action="store_true", help="Whether to overwrite existing images.")
    parser.add_argument("-n", "--n-images", type=int, default=0, help="How many images to download.")

    args = vars(parser.parse_args())

    download_album(args["link"], args["output_dir"], overwrite=args["force_write"], n_images=args["n_images"])


if __name__ == "__main__":
    cli()
