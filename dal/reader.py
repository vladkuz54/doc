from pathlib import Path

import httpx


def fetch_csv_to_file(source_url: str, output_path: Path, timeout: float = 30.0) -> bool:
    
	try:
		output_path.parent.mkdir(parents=True, exist_ok=True)

		with httpx.Client(timeout=timeout, follow_redirects=True) as client:
			response = client.get(source_url)
			response.raise_for_status()

		output_path.write_bytes(response.content)
		return True
	except httpx.HTTPError as e:
		print(f"HTTP Error: {e}")
		return False
	except Exception as e:
		print(f"Error downloading file: {e}")
		return False
