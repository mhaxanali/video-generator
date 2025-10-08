import requests
import os
from backend.assets.constants import PEXELS_API_KEY

BASE_URL = "https://api.pexels.com/v1"

def search_images(query: str, _type: str, per_page: int = 1) -> list[dict]:
    """
    Search Pexels for images and download them locally.
    Returns list of image metadata (including saved filename).
    """
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": f'{query} related to {_type}', "per_page": per_page}

    response = requests.get(f"{BASE_URL}/search", headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for i, photo in enumerate(data.get("photos", []), start=1):
        image_url = photo["src"]["original"]
        folder_path = os.path.join("downloads")
        os.makedirs(folder_path, exist_ok=True)
        filename = os.path.join(folder_path, f"{query}_{i}.jpg")

        save_image(image_url, filename)

        results.append({
            "url": image_url,
            "filename": filename,
            "photographer": photo["photographer"],
            "profile": photo["photographer_url"],
            "credit": f'Photo by {photo["photographer"]} on Pexels'
        })

    return results


def save_image(url: str, filename: str) -> None:
    """Download the image file and save it locally."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, "wb") as f:
        for chunk in response.iter_content(1024):
            f.write(chunk)
