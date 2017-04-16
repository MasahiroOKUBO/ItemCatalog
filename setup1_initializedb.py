from ItemCatalog.utility import Base
from ItemCatalog.utility import engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
