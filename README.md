# FIAP - Pos Tech - Self-service restaurant

## Description

This is a fast food self-service system backend, with the aim of mitigating confusion among waiters and delays in preparing deliveries and orders.

Developed for FIAP's postgraduate software architecture course.

### Phase 1

- Event Storming (DDD) diagrams
  - placing the order and paying
  - order preparation and delivery
- Hexagonal Architecture implementation of an API
  - Customer register
  - Customer identification by CPF document
  - Product CRUD operations
  - Fake Checkout
  - SQL Database
- Docker containers
  - PostgesSQL Database
  - FastAPI

### Phase 2

- Refactor the application to Clean Architecture
  - Add order CRUD operations
  - Add Payment CRUD operations
  - Add payment fake webhook for fake payment provider
- K8s infrastructure
  - Increase and decrease of pods according to demand
- Architecture diagram
  - Kubernetes cluster diagram
  - Api requests examples collection
  - explanatory video

### Phase 3

Coming soon ...

## Demo video

- [YouTube](...)

## API

You can find the requests example collection at the `docs/collection` directory.

## K8s

You can find the Kubernetes manifests at `k8s` directory.

## Event Storming

-[Miro](https://miro.com/welcomeonboard/M0QySElxVFd1a0ozTUs5eUFxUHh3ZTYxeUZoM2kxb2lTWlJBR0RTWDc0aVRLWFg1SWgzam9CcFJuM3FFOG95SHwzMDc0NDU3MzU1MjY5Nzg4Njk5fDI=?share_link_id=271651641849)

## Usage

### Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/)

### How to run

1. `docker compose up -d postgres` - Start the database.
2. `docker compose run --rm migrations` - Run the migrations.
3. `docker compose up api`
4. Go to `https://localhost:8000/docs` to see the swagger documentation.

## Development

### Migrations command examples

- `alembic -c migrations/alembic/alembic.ini revision --autogenerate -m"First commit"`
- `alembic -c migrations/alembic/alembic.ini upgrade head`
