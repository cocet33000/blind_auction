[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
## ローカルでDynamoDBを起動する
```bash
docker-comose up -d
```

管理画面: http://localhost:8001

## python環境構築
```bash
cd blind_auction/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
