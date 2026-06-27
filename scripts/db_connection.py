from sqlalchemy import create_engine

def get_engine():
    """
    Creates and returns a SQLAlchemy engine
    connected to the SQLite database.
    """
    engine = create_engine("sqlite:///../apexplanet.db")
    return engine