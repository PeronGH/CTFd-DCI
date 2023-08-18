# CTFd-DCI

## Architecture

```mermaid
graph TB
  subgraph Docker
      subgraph DCI["Dynamic Challenge Instance Module"]
          subgraph DM["Docker Management"]
            subgraph DIND[Docker in Docker]
             Instances
            end
            DAPI["RESTful API (Docker Compose Spawn)"]
          end
          CP[CTFd Integration]
      end
      CTFd[CTFd]
  end

    U[Users]
    A[Admin]

  CTFd -->|Management UI| A
  CTFd -->|Participation UI| U
    DAPI <-->|Direct Docker Interactions| DIND
    DAPI -->|APIs: start/stop/list Instances| CP
    CP <-->|Plugin Integration| CTFd
    CP -->|Stack Config Management| DAPI
    Instances -->|Directly Exposed Ports| U

```

## Testing

Start the test server:

```shell
docker compose up
```

## TODOs

- [ ] Admin modifying configuration
- [ ] Admin listing all instances
- [ ] Admin creating `dynamic instance` challenge
  - [ ] Admin uploading stack configuration
- [ ] Admin updating `dynamic instance` challenge
- [ ] Scheduled cleaning up expired instances every minute
- [ ] User participating in a `dynamic instance` challenge

## Contributing

Please feel free to contribute to this project. Any help is appreciated. But please make sure to follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
