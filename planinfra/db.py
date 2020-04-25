import aiopg.sa
import sqlalchemy as sa
import peewee
import peewee_async

import settings



async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    # database.init(**settings.DATABASE)
    # app.database = database
    # app.objects = peewee_async.Manager(app.database)
    app['db'] = engine

    
async def close_pg(app):
    
    app['db'].close()
    await app['db'].wait_closed()
