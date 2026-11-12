# Mini Project 3: IoT – Fog – Cloud

Smart-city district with two zones. Camera clients send images to their zone's fog node, and the fog node processes part of each request locally and offloads the rest to the cloud. Fog and cloud nodes ship structured logs to a monitoring service.

## Layout

| Path           | Contents                                           |
| -------------- | -------------------------------------------------- |
| `camera/`      | Camera client image                                |
| `fog/`         | Fog node image (shared by `fog_a` and `fog_b`)     |
| `cloud/`       | Cloud node image                                   |
| `monitoring/`  | Log collector / alerting service                   |
| `common/`      | Code shared by fog and cloud (`logging_client.py`) |
| `experiments/` | Experiment, attack and mitigation scripts          |
| `report/`      | Report (`REPORT.md`) and screenshots               |

The fog and cloud images are built with the repository root as the build context so they can include `common/`.

## Run

```bash
docker compose up -d --build
docker compose ps        # all 7 containers should show "(healthy)"
```

Optional overrides go in a `.env` file:

```
FOG_CPU_LIMIT=0.5
FOG_MEM_LIMIT=256m
NETEM_DELAY=50ms
```

## Viewing logs

`mgmt_net` is an internal network, so the monitoring service is not published on the host. Read the collected logs from inside the container:

```bash
docker compose exec monitoring tail -n 20 /logs/events.jsonl
```

## Stop

```bash
docker compose down        # add -v to also delete the collected logs
```
