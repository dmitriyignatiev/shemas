from aiopg.sa import SAConnection as SAConn
from aiopg.sa.result import RowProxy
from sqlalchemy import and_, select, func

from tables import mainresource, contract, association_t, plan, user, teacher, lessons



async def select_resources(conn:SAConn) -> RowProxy:
    cursor = await conn.execute(mainresource.select())
    item = await cursor.fetchall()
    return item

async def select_resource_contracts(conn: SAConn) -> RowProxy:
    cursor = await conn.execute(select([mainresource, contract,
                                            association_t.c.mainresource_id]).apply_labels().
                                            where
                                            (and_
                                             (association_t.c.mainresource_id==mainresource.c.id,
                                               association_t.c.contract_id==contract.c.id)))
    item = await cursor.fetchall()
    return item

# доработать резолвер
async def select_all_resource_contracts(conn: SAConn) -> RowProxy:
      cursor = await conn.execute(select([mainresource, func.array_agg(contract.c.id), func.array_agg(contract.c.name),
                                            association_t.c.mainresource_id]).apply_labels().
                                            where
                                            (and_
                                             (association_t.c.mainresource_id==mainresource.c.id,
                                               association_t.c.contract_id==contract.c.id)).
                                                    group_by(mainresource.c.id, mainresource.c.name,  association_t.c.mainresource_id))

      item = await cursor.fetchall()
      return item

async def select_planswithcontracts(conn: SAConn) -> RowProxy:
    cursor = await conn.execute(select([plan.c.id, plan.c.name, contract.c.name]).apply_labels().where(contract.c.id == plan.c.id))
    item = await cursor.fetchall()
    return item

###################################################
async def select_plans(conn: SAConn) -> RowProxy:
    cursor = await conn.execute(select([plan]))
    item = await cursor.fetchall()
    return item

async def select_user(conn:SAConn) -> RowProxy:
    cursor = await conn.execute(select([user]))
    item = await cursor.fetchall()
    return item

async def select_lessons(conn:SAConn) -> RowProxy:
    cursor = await conn.execute(select([lessons]))
    item = await cursor.fetchall()
    return item

async def select_teacher(conn: SAConn) -> RowProxy:
    cursor = await conn.execute(select([teacher]))
    item = await cursor.fetchall()
    return item
