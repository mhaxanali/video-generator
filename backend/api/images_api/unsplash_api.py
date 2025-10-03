import requests
import os
from backend.assets.constants import UNSPLASH_ACCESS_KEY

BASE_URL = "https://api.unsplash.com"


def search_images(query: str, per_page: int = 1) -> list[dict]:
    """
    Search Unsplash for images and download them locally.
    Returns list of image metadata (including saved filename).
    """
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    params = {"query": query, "per_page": per_page}

    response = requests.get(f"{BASE_URL}/search/photos", headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for i, photo in enumerate(data.get("results", []), start=1):
        download_url = photo["links"]["download_location"]

        # Track the download (required by Unsplash ToS)
        track_download(download_url)

        image_url = photo["urls"]["full"]  # "regular" or "full" depending on needs
        folder_path = os.path.join('..', '..', '..', 'downloads')
        os.makedirs(folder_path, exist_ok=True)
        filename = os.path.join(folder_path, f"{query}_{i}.jpg")

        # Save the image locally
        save_image(image_url, filename)

        results.append({
            "url": image_url,
            "filename": filename,
            "photographer": photo["user"]["name"],
            "profile": photo["user"]["links"]["html"],
            "credit": f'Photo by {photo["user"]["name"]} on Unsplash'
        })

    return results


def track_download(download_url: str) -> None:
    """Notify Unsplash about the download (required)."""
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    requests.get(download_url, headers=headers)


def save_image(url: str, filename: str) -> None:
    """Download the image file and save it locally."""
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
