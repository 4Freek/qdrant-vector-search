# qdrant-vector-search

```python
  python3 qdrant.py
```
```
http://localhost:5000/create-collection

(body)
{
    "collection": "tutu" # nombre de la colección (de comenzar por image se usara un embbending size de 384)
}

```

```
http://localhost:5000/upser

(body)
{
  "collection": "tutu",
  "payload": {
      "id": 3213213, # este id se toma como id de Qdrant
      "name": "foo",
      "description": "foo",
  }
}

```

```
http://localhost:5000/search

(body)
{
  "query": "juan",
  "collection": "tutu",
  "filters": { # filtros a tener en cuenta
      "should": {
          "values": {
          "nombre": "juan"
          }
      }
  }
}

```