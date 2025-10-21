**Full Stack Developer Interview Q\&A - Pratik Saundarmal**

---

### **Easy Questions (8)**

**1. What is a RESTful API and how is it typically used in web application development?**
A RESTful API (Representational State Transfer) allows communication between client and server via HTTP methods like GET, POST, PUT, DELETE. It is stateless, scalable, and commonly used to fetch or send data between frontend (React) and backend (Spring Boot).

**2. Describe the difference between monolithic and microservices architectures.**
Monolithic architecture is a single unit where all components are tightly coupled. Microservices architecture breaks down functionality into independent services, allowing scalability, isolated deployment, and easier fault tolerance.

**3. Explain the difference between SQL databases (like PostgreSQL) and NoSQL databases (like MongoDB). When might you choose one over the other?**
SQL databases are relational and use schemas, suitable for structured data with relationships. NoSQL like MongoDB is schema-less, ideal for unstructured or hierarchical data. Use SQL when data integrity is key; NoSQL for flexible schema needs.

**4. What are the core concepts of React (components, props, state, and virtual DOM)?**

* **Components**: Reusable UI pieces.
* **Props**: Inputs to components.
* **State**: Internal data of components.
* **Virtual DOM**: React’s in-memory representation of UI to efficiently update real DOM.

**5. How does Spring Boot simplify application development compared to the traditional Spring framework?**
Spring Boot reduces boilerplate by offering auto-configuration, embedded servers (like Tomcat), and opinionated project structures, allowing faster setup and development.

**6. What is Docker and how is it different from a virtual machine?**
Docker is a containerization platform that packages applications with dependencies. It is lightweight, shares OS kernel, and starts faster than VMs, which emulate full OS.

**7. What are AWS EC2, S3, and RDS services typically used for?**

* **EC2**: Virtual servers.
* **S3**: Object storage.
* **RDS**: Managed relational databases.

**8. What is Git and what are platforms like Bitbucket or GitHub used for in the development process?**
Git is a version control system. Platforms like GitHub or Bitbucket host repositories, enable collaboration, version tracking, pull requests, and CI/CD integration.

---

### **Medium Questions (6)**

**9. How would you design the database schema for an e-commerce application?**
**PostgreSQL (Relational)**: Tables - Users, Products, Orders, OrderItems. Use foreign keys, indexes.
**MongoDB (NoSQL)**: Collections - Users, Products. Embed Orders inside Users or reference via IDs for flexibility.

**10. Describe user authentication and authorization in Spring Boot using Keycloak or JWT.**
With **JWT**, the backend issues a token after login; client uses it for subsequent requests. With **Keycloak**, externalized auth server handles login, and Spring Boot validates tokens via Keycloak adapters or Spring Security.

**11. How to containerize a Spring Boot microservice using Docker and deploy it on AWS?**

* Dockerfile builds app image.
* Push to Docker Hub/ECR.
* Use EC2 or ECS to deploy.
* CI/CD tools like Jenkins/GitHub Actions automate builds/tests/deploys.

**12. How to resolve performance issues in a React application?**

* Use `React.memo`, `useCallback`, `useMemo`
* Code splitting (lazy loading)
* Avoid unnecessary re-renders
* Monitor with React DevTools and Lighthouse

**13. How to optimize a slow PostgreSQL query?**

* Add appropriate indexes
* Use `EXPLAIN ANALYZE`
* Avoid SELECT \*
* Optimize joins and filters

**14. How have you used Agile and tools like JIRA and Confluence?**
Participated in stand-ups, sprint planning, retrospectives. Used **JIRA** for task tracking, **Confluence** for documentation. Agile improves delivery through iterations and feedback.

---

### **Hard Questions (6)**

**15. Design a microservices architecture for an e-commerce platform.**
Services: Product, Order, User, Payment. Communicate via REST or message queues (e.g., RabbitMQ). Use API Gateway, Service Registry (like Eureka), Config Server. Ensure data consistency via event sourcing or sagas.

**16. How to implement auth across microservices using OAuth2/JWT/Keycloak?**

* Use a centralized auth provider (e.g., Keycloak).
* Clients authenticate and receive JWT.
* Microservices verify token without contacting auth server every time.
* Add scopes/roles to tokens for fine-grained access.

**17. Troubleshooting a slow Spring Boot microservice under load?**

* Profile CPU/memory with JVisualVM
* Enable caching (e.g., Redis)
* Use load balancers, increase thread pool
* Apply asynchronous processing
* Scale horizontally

**18. Steps for a CI/CD pipeline in Spring Boot with AWS:**

* **Build**: Maven + Unit tests
* **Test**: Integration tests + Static analysis
* **Package**: Docker image
* **Deploy**: Push to AWS (EC2, ECS, or Elastic Beanstalk)
* Use GitHub Actions or Jenkins
* Enable rollback with versioning/tagging

**19. Managing state in large React apps?**

* Use `useState` for local state
* Use `Context API` or `Redux` for global state
* Structure components into containers and presentational components
* Normalize data to avoid prop drilling

**20. What is the circuit breaker pattern and how to implement it in Spring Boot?**
Used to prevent cascading failures when a service is down. Implement with Resilience4j or Hystrix.

* Define fallback methods
* Configure thresholds (timeout, failure rate)
* Helps maintain system stability
