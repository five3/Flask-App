
class BaseConfig:
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]atmp/'
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/atmp'
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_POOL_TIMEOUT = 30            # 30s
    SQLALCHEMY_POOL_RECYCLE = 60 * 60       # 1 hour
    SQLALCHEMY_ECHO = False


class TestingConfig(DevelopmentConfig):
    pass


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://autoax:autoax@10.27.12.50:3306/atmp'
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_POOL_TIMEOUT = 30            # 30s
    SQLALCHEMY_POOL_RECYCLE = 60 * 60       # 1 hour
    SQLALCHEMY_ECHO = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
