from aiohttp import web
from sqlalchemy import text
from sqlalchemy.sql import and_, or_, not_
from sqlalchemy.sql import select
from tables import (plan,
                    contract,
                    mainresource,
                    association_t,
lessons
                    )

stmt = text("""select r.id as rid, r.name, 
                c.id as cid,  c.name, 
                t.c.mainresource_id as tim, t.c.contract_id as tic
                FROM
                    mainresource as r, contract as c, association_t as t
                where 
                    tim=rid
                AND 
                    tic=cid
            """)


async def index(request):
    print("hello")
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(plan.select())
        plans = await cursor.fetchall()
        plans = [dict(q) for q in plans]
        print(plans)

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(contract.select())
        contracts = await cursor.fetchall()
        contracts = [dict(q) for q in contracts]
        print(contracts)

    async with request.app['db'].acquire() as conn:

        #все ресурсы с их котрактами
        t1 = mainresource.alias()
        t2 = contract.alias()


        cursor = await conn.execute(select([mainresource, contract,
                                            association_t.c.mainresource_id]).apply_labels().
                                            where(and_(association_t.c.mainresource_id==mainresource.c.id,
                                                       association_t.c.contract_id==contract.c.id)))
        resources = await cursor.fetchall()
        resources = [dict(q) for q in resources]
        print(resources)




    return web.Response(text='Hello Aiohttp!')