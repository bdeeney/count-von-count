count-von-count
===============

A simple REST API that exposes Counter resources.

Live demo: http://count-von-count.appspot.com/counters/

#### Create a Counter
`% curl -X POST -d '' http://count-von-count.appspot.com/counters/`
```json
{
  "id": "5642554087309312",
  "url": "http://count-von-count.appspot.com/counters/5642554087309312"
}
```

#### Increment a Counter
`% curl -X PUT -d '' http://count-von-count.appspot.com/counters/5642554087309312`
```json
{
  "count": 1,
  "id": "5642554087309312",
  "url": "http://count-von-count.appspot.com/counters/5642554087309312"
}
```
`% curl -X PUT -d '' http://count-von-count.appspot.com/counters/5642554087309312`
```json
{
  "count": 2,
  "id": "5642554087309312",
  "url": "http://count-von-count.appspot.com/counters/5642554087309312"
}
```

#### Retrieve a Counter
`% curl -X GET http://count-von-count.appspot.com/counters/5642554087309312`
```json
{
  "count": 2,
  "id": "5642554087309312",
  "url": "http://count-von-count.appspot.com/counters/5642554087309312"
}
```
