# Java Project — ecommerce-app

Overview

- Location: `java-project/ecommerce-app`
- Build system: Maven (`pom.xml`)
- Framework: Spring Boot
- Purpose: Example e-commerce backend demonstrating controllers, services, repositories, and JPA entities.

Project structure (key folders)

- `src/main/java/com/example/ecommerce`
  - `EcommerceApplication.java` — application entry point.
  - `controller/` — REST controllers: `CartController`, `OrderController`, `ProductController`, `UserController`.
  - `entity/` — JPA entities: `CartItem`, `OrderEntity`, `Product`, `User`.
  - `repository/` — Spring Data JPA repositories for data access.
  - `service/` — business logic services coordinating controllers and repositories.
- `src/main/resources`
  - `application.properties` — runtime configuration (database, ports, etc.).
  - `data.sql` — optional seed data loaded at startup.

Build and run

1. Build with Maven from `java-project/ecommerce-app`:

```bash
mvn clean package
```

2a. Run from Maven:

```bash
mvn spring-boot:run
```

2b. Or run the produced jar:

```bash
java -jar target/*.jar
```

Configuration

- Edit `src/main/resources/application.properties` to change database settings, server port, or logging.
- If using the included `data.sql`, the application will load sample rows into the configured datasource at startup (H2 or configured RDBMS).

Testing

- Unit and integration tests (if present) are under `src/test/java` and can be run with:

```bash
mvn test
```

Common tasks and endpoints

- Browse controllers in `controller/` to find available REST endpoints (typical resources: `/products`, `/cart`, `/orders`, `/users`).
- Repositories are Spring Data interfaces; services contain business logic and transaction boundaries.

Notes

- This project assumes a configured datasource; for quick local tests it may be configured to use an in-memory DB (H2). Check `application.properties`.
- To change Java version or dependency versions, edit `pom.xml`.
