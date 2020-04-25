import graphene
from graphene import ResolveInfo
from aiopg.sa.result import RowProxy
from sqlalchemy import select, and_

from graphene.relay import Node

from tables import contract

from api.models import (Mainresource, ResourceContracts, MainContracts, PlanswithContracts, UserSchema, LessonSchema, TeacherSchema,
                        ContractsSchema
                        )
from db_utils import select_resources, select_resource_contracts, select_all_resource_contracts, select_planswithcontracts, select_user, select_lessons, select_teacher




class MainResourceQuery(graphene.ObjectType):

    contracts = graphene.List(
        ContractsSchema, description='Контракты'
    )



    async def resolve_contracts(self, info:ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            cursor = await conn.execute(select([contract]))
            item = await cursor.fetchall()
            return item

    users = graphene.List(
        UserSchema, description='Все юзеры'
    )

    async def resolve_users(self, info: ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_user(conn)
            return item

    lessons = graphene.List(
        LessonSchema, description='Все уроки'
    )

    async def resolve_lessons(self, info:ResolveInfo) -> RowProxy:
        # app = info.context['request'].app
        # async with app['db'].acquire() as conn:
        #     item = await select_lessons(conn)
        item = [{'name': 'Mathematics'}]
        return item

    teacher = graphene.List(
        TeacherSchema, description='Все учителя'
    )


    async def resolve_teacher(self, info:ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_teacher(conn)
            return item




    resource = graphene.List(
        Mainresource,
        description='все ресурсы'
    )

    resourcecontract =  graphene.List(
        ResourceContracts,
        description = 'Объекты строительства с контрактами'
    )

    # доработать
    all_resource = graphene.List(
        MainContracts,
        description = 'объекты строительства с контрактами по группам'
    )

    planwithcontracts = graphene.List(
        PlanswithContracts,
        description = 'Планы строительства с контрактами'
    )

    async def resolve_planwithcontracts(self, info: ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_planswithcontracts(conn)
            print(item)
            return item

    async def resolve_all_resource(self, info: ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_all_resource_contracts(conn)
            print(item)
            return item

    async def resolve_resource(self, info: ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_resources(conn)
            print(item)
            return item

    async def resolve_resourcecontract(self, info: ResolveInfo) -> RowProxy:
        app = info.context['request'].app
        async with app['db'].acquire() as conn:
            item = await select_resource_contracts(conn)
            print (item)
            return item








class Query(MainResourceQuery):
    """
    The main GraphQL query point.
    """
    node = Node.Field()