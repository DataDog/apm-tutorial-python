# apm-tutorial-python

The notes application and calendar application are both REST API's. The notes application has POST, GET, PUT and DELETE operations for creating, getting, updating and deleting notes. Additionally, the notes application POST /notes method has an additional parameters, add_date, that can be set to 'y' in order to make a call to the calendar application for a random date. This can be used to show distributed tracing across applications.

This is a sample Python application made to run in various deployment scenarios with two different services, a notes application and calendar application, in order to provide sample distributed tracing. The application is used in a tutorial showcasing how to enable APM tracing for an application. The different ways to deploy these applications are:
- locally on host machine (with Datadog Agent also running on host)
- within Docker containers (with Datadog Agent also in a container)
- within Docker containers (with Datadog Agent running on host)
- Google Kubernetes Engine (GKE)
- Amazon AWS Elastic Kubernetes Service (AWS EKS)

The sample application is a very simple pair of rest APIs, as seen below. All commands below are for host and/or Docker container deployment situations. For Kubernetes deployments, the URL will be that of the Kubernetes notes or calendar service. 

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
