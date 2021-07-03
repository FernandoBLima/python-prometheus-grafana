# Python-Prometheus-Grafana

The main objective of this project is to create a simple Python service example that contains Prometheus which is a standalone open source project that monitors and alerts systems and Grafana.

### Mains Tools
- Docker
- Prometheus
- Grafana

### Technical Overview

You will need Docker installed to follow the next steps and build an run the image locally you just need to use the following command:

```bash
docker-compose up --build
```

### How it Works

At first, make some reqeust several times using the following link `http://localhost:5000`, then you be able to see changes in the metrics `http://localhost:5000/metrics`.

After that, you can navigate to grafana's Dashboard via the link `http//localhost:3000` and upload the datasource and dashboard configuration using the JSO files. Or you can use Grafana's Dashboard API to create a new dashboard and datasource using the following requests:

- Enable datasource:
POST http://localhost:3000/api/dashboards/db
Body
```
{
    "name": "prometheus",
    "type": "prometheus",
    "url": "http://localhost:9090",
    "access": "browser",
    "isDefault": true
}
```

- Create Dashboard:
POST http://localhost:3000/api/datasources

For more informations you can access the [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)

After all these actions, you should be able to access the Grafana Dashboard that display some graphs and metrics related to the Flask Web Application that was created.

### Help and Resources

You can read more on:

- [Docker Documentation](https://docs.docker.com/get-started/overview/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)
- [Grafana Documentation](https://grafana.com)
- [Prometheus Documentation](http://prometheus.io)
- [Prometheus Python Client](https://github.com/prometheus/client_python)