import structlog

logger = structlog.get_logger(__file__)

logger.info("test", contexto="Contexto de pruebas.........")

logger.info("test funcion", contexto="agregando funcion exactranetete ")