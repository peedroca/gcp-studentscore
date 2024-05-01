# gcp-studentscore

Connecting GCP with my Student Score application.

First steps to configure Google Cloud Platform [here.](https://cloud.google.com/firestore/docs/create-database-server-client-library?hl=en#python)

![](/diagrams/architecture.png)

### Setting up enviroment variables
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account-file.json"
```

### Executing Cloud Functions
Run below code:
```
functions-framework --target hello --debug
```
