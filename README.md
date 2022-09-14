# apm-tutorial-python-host

The notes application is a REST API available on 'localhost:8080'. The calendar application is also a REST API, and it's available on 'localhost:9090'. Additionally, the notes application POST /notes method has an additional parameters, add_date, that can be set to 'y' in order to make a call to the calendar application for a random date. This can be used to show distributed tracing across applications.

This is a sample Python application made to run on your local machine with two different services, a notes application and calendar application, in order to provide sample distributed tracing. The application is used in a tutorial showcasing how to enable APM tracing for an application running locally with the Datadog Agent also running locally.

The sample application is a very simple pair of rest APIs, as seen below:

# REST APIs

## Calendar Application

### `GET /calendar`

Returns a random date in 2022.

#### Request

```sh
curl 'http://localhost:9090/calendar'
```

#### Response

```json
{"status":"success","date":"3/22/2022"}
```

## Notes Application

### `GET /notes/`

#### Request

```sh
curl 'http://localhost:8080/notes'
```

#### Response

```json
[{ "id": 0, "description": "Hello, this is a note." }]
```

### `POST /notes`

#### Request - without optional add_date parameter

```sh
curl -X POST 'http://localhost:8080/notes?desc=ImANote'
```

#### Response

```json
{ "id": 1, "description": "ImANote" }
```

#### Request - with optional add_date parameter

Makes a request to calendar service on port 9090.

```sh
curl -X POST 'http://localhost:8080/notes?desc=ImANoteWithDate&add_date=y'
```

#### Response

```json
{ "id": 2, "description": "HiImANoteWithDate. Message Date: 09/21/2022" }
```

### `GET /notes/:id`

#### Request

```sh
curl 'http://localhost:8080/notes/1'
```

#### Response

```json
{ "id": 1, "description": "ImANote" }
```

### `PUT /notes/:id`

#### Request

```sh
curl -X PUT 'http://localhost:8080/notes/1?desc=UpdatedNote'
```

#### Response

```json
{ "id": 1, "description": "UpdatedNote" }
```

### `DELETE /notes/:id`

#### Request

```sh
curl -X DELETE 'http://localhost:8080/notes/1'
```

#### Response

```json
{ "message": "note with id 4 deleted." }
```
