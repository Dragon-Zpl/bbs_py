from worker.work import cron
from boot.elastic import init_es_cli


if __name__ == '__main__':
    init_es_cli()
    cron()

