import logging
import yaml
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database(object):
    """Operations interface to database"""

    def __init__(self, env):
        with open("config.yml") as f:
            self.config = yaml.load(f.read())["database"][env]
        db_url = self._db_url_template().format(**self.config)
        self.engine = create_engine(db_url)

    def initialize(self):
        """Sets up database if needed.

        :returns: None
        """
        logger.info("Database initializing...")
        try:
            # Check if DB exists
            conn = self.engine.connect()
            logger.info("DB already exists.")
        except Exception as e:
            # Create DB
            logger.info("DB not found. Creating...")
        else:
            conn.close()

    def _db_url_template(self):
        return "postgres://{username}:{password}@{host}:{port}/{database}"
