# unittestのサンプル

起動

```bash
docker compose build
docker compose up -d
```

Sphinxドキュメント生成

```bash
docker compose exec mypython sphinx-apidoc -f -e -o docs/source . docs __pycache__ test
docker compose exec mypython sphinx-build -b html docs/source docs/build/html
```

停止

```bash
docker compose down
```
