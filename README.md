# unittestのサンプル

起動

```bash
docker compose build
docker compose up -d
```

Sphinxドキュメント生成

```bash
docker compose exec mypython sphinx-build -b html docs docs/_build
```

停止

```bash
docker compose down
```
