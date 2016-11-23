import logging
import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database(object):
    """Operations interface to database"""

    def __init__(self, env):
        with open("config.yml") as f:
            self.config = yaml.load(f.read())["database"][env]
        db_url = self._db_url_template().format(**self.config)
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def initialize(self):
        """Sets up database if needed.

        :returns: None
        """
        logger.info("Database initializing...")
        try:
            # Check if DB exists
            conn = self.engine.connect()
            logger.info("DB already exists.")
            conn.close()
        except Exception as e:
            logger.info("DB not found. Creating...")
            self._create_app_database()
        logger.info("Creating tables...")
        self._create_tables()

    def persist(self, model):
        session = self.Session()
        session.merge(model)
        session.commit()

    def _create_tables(self):
        from parser.pending_article import Base, PendingArticle
        Base.metadata.create_all(self.engine)

    def _db_url_template(self):
        return "postgres://{username}:{password}@{host}:{port}/{database}"

    def _create_app_database(self):
        app_db = self.config["database"]
        self.config["database"] = "postgres"
        db_url = self._db_url_template().format(**self.config)
        postgres_engine = create_engine(db_url, echo=True)
        pg_conn = postgres_engine.connect()
        pg_conn.execute("commit")
        pg_conn.execute("create database {0}".format(app_db))
        pg_conn.close()

