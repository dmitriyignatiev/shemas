import graphene
from aiopg.sa.result import RowProxy
from graphql import ResolveInfo
from db_utils import select_lessons
from tables import lessons, user, mainresource, association_t, contract
from sqlalchemy import select, and_
from aiopg.sa import SAConnection as SAConn

class ContractsSchema(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Mainresource(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    contracts = graphene.List(ContractsSchema)
    async def resolve_contracts(self, info:ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            cursor = await conn.execute(select([contract, self
                                                association_t.c.mainresource_id]).apply_labels().
                                        where
                                        (and_
                                         (association_t.c.mainresource_id == self.id,
                                         association_t.c.contract_id == contract.c.id)))



            item = await cursor.fetchall()
            print('это контракты', item)
            return item




class ResourceContracts(graphene.ObjectType):
    mainresource_id = graphene.Int()
    mainresource_name = graphene.String()
    contract_id = graphene.Int()
    contract_name = graphene.String()

#доработаю группировку по для ресолвера select_all_resource_contracts
class MainContracts(graphene.ObjectType):
    mainresource_id = graphene.Int()
    mainresource_name = graphene.String()
    contract_id = graphene.Int()
    contract_name = graphene.Int()

# планы и контракты
class PlanswithContracts(graphene.ObjectType):
    plan_id = graphene.Int()
    plan_name = graphene.String()
    contract_name = graphene.String()


#####################################
class LessonSchema(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()


class UserSchema(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    lessons = graphene.List(LessonSchema)
    async def resolve_lessons(self, info:ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            cursor = await conn.execute(select([lessons]).where(lessons.c.user_id==self.id))
            item = await cursor.fetchall()
            print('ЭТо уроки: ',  item)
                # item = [{'name': 'Mathematics'}]
            return item

##############################

class TeacherSchema(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()





