# CI/CD

This repository contains scripts and configurations for deploying a project using Google Cloud Platform (GCP) service: Cloud Build and Cloud Run

# Prerequisites

Before you begin, ensure you have the following:

- Google Cloud SDK installed on your local machine
- A GCP account with the necessary permissions

# Installation

1. Install the Google Cloud SDK:
Follow the instructions in the official documentation to install the Google Cloud SDK for your operating system.

2. Authenticate with your GCP account:
Open a terminal and run:

```sh
gcloud auth login
```
This will open a browser window where you can log in with your GCP account. Follow the prompts to complete the authentication process.

# Enabling Required APIs

Ensure the necessary APIs are enabled for your project. You need to enable the following APIs:

- Cloud Run
- Cloud Build
You can enable these APIs via the GCP Console or using the command line:

```sh
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

# Configuration

Set your GCP project:
Replace <project-id> with your actual GCP project ID and run the following command:

```sh
gcloud config set project <project-id>
```

# Deployment

Deploy using the provided YAML configuration:
Use the following command to submit your build and deploy using the cloudbuild.yml file in this repository:

```sh
gcloud builds submit --config cloudbuild.yml
```

This command will start the build process and deploy your application according to the specifications in the `cloudbuild.yml` file.