import subprocess

packages = ["fastapi", "uvicorn[standard]"]

for pkg in packages:
    print(f"Installing {pkg}...")
    subprocess.run(["python3", "-m", "pip", "install", pkg]) 

print("FastAPI 및 Uvicorn 설치 완료!")