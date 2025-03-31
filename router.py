from fastapi import APIRouter, status, HTTPException, Response, Request
from schemas import CreateIssue, config_emulate
import random
import json
import asyncio


router = APIRouter()
db = []


# Создание задачи
#async def create(request: Request, issue: CreateIssue):
@router.post('/rest/api/2/issue', status_code=status.HTTP_201_CREATED)
async def create(request: Request):
    await asyncio.sleep(0.2)
    issue_id = str(random.randrange(1, 9)) + "".join(str(random.randrange(0, 9)) for _ in range(4))
    # if issue_id not in (i['id'] for i in db):
    #     issue_dict = issue.model_dump()
    #     issue_dict['id'] = issue_id
    #     issue_dict['key'] = f'TEST-{str(random.randrange(1, 9)) + "".join(str(random.randrange(0, 9)) for _ in range(4))}'
    #     issue_dict['self'] = f'{config_emulate.PROTOCOL}://{config_emulate.HOST}:{str(config_emulate.PORT)}{request.url.path}/{issue_id}'
    #     db.append(issue_dict)
    return Response(
        status_code=status.HTTP_201_CREATED,
        content=json.dumps({'id': issue_id,
                                'self': "TEST",
                                'key': "TEST",
                                'fields': "TEST"}),
            # content=json.dumps({'id': issue_id,
            #                     'self': issue_dict['self'],
            #                     'key': issue_dict['key'],
            #                     'fields': issue_dict['fields']}),
        headers={
                'Content-Type': 'application/json',
                'Location': f'{request.url.path}'
            }
        )
    # else:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
    #                         detail='Задача с таким id уже существует!')

# Получение информации обо всех задачах
@router.get('/rest/api/2/issue/all')
async def all_get(request: Request):
    await asyncio.sleep(0.01)
    if len(db) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(
        status_code=status.HTTP_200_OK,
        content=json.dumps(db),
        headers={
            'Content-Type': 'application/json',
            'Location': f'{request.url.path}'
        }
    )

# Получение информации об одной задаче
@router.get('/rest/api/2/issue/{issueIdOrKey}')
async def get(request: Request, issueIdOrKey: str):
    await asyncio.sleep(0.01)
    # result = None
    # for i in db:
    #     if i['id'] == issueIdOrKey or i['key'] == issueIdOrKey:
    #         result = i
    #         break
    #
    # if result is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return Response(
    #     status_code=status.HTTP_200_OK,
    #     content=json.dumps({'id': result['id'],
    #                         'self': result['self'],
    #                         'key': result['key'],
    #                         'fields': result['fields']}),
    #     headers={
    #         'Content-Type': 'application/json',
    #         'Location': f'{request.url.path}'
    #     }
    # )
    return Response(
        status_code=status.HTTP_200_OK,
        content=json.dumps({'id': issueIdOrKey,
                            'self': "TEST",
                            'key': "TEST",
                            'fields': "TEST"}),
        headers={
            'Content-Type': 'application/json',
            'Location': f'{request.url.path}'
        }
    )

# Изменение задачи
# async def updateDict(request, issue, issueIdOrKey, i):
#     issue_dict = issue.model_dump()
#     if i['id'] == issueIdOrKey:
#         issue_dict['id'] = issueIdOrKey
#     if i['key'] == f'TEST-{issueIdOrKey}':
#         issue_dict['key'] = f'TEST-{issueIdOrKey}'
#
#     for key, value in issue_dict['fields'].items():
#         if value is not None and value != "":
#             i['fields'][key] = value
#
#     return Response(
#         status_code=status.HTTP_204_NO_CONTENT,
#         headers={
#             'Content-Type': 'application/json',
#             'Location': f'{request.url.path}'
#         }
#     )
#     # return Response(
#     #     status_code=status.HTTP_200_OK,
#     #     content=json.dumps({'id': i['id'],
#     #                         'self': i['self'],
#     #                         'key': i['key'],
#     #                         'fields': i['fields']}),
#     #     headers={
#     #         'Content-Type': 'application/json',
#     #         'Location': f'{request.url.path}',
#     #     }
#     # )

#async def update(request: Request, issueIdOrKey: str, issue: CreateIssue):
@router.put('/rest/api/2/issue/{issueIdOrKey}', status_code=status.HTTP_204_NO_CONTENT)
async def update(request: Request):
    await asyncio.sleep(0.1)
    # for i in db:
    #     if i['id'] == issueIdOrKey or i['key'] == issueIdOrKey:
    #         return await updateDict(request, issue, issueIdOrKey, i)
    #
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
        headers={
            'Content-Type': 'application/json',
            'Location': f'{request.url.path}'
        }
    )

# Удаление задачи
@router.delete('/rest/api/2/issue/{issueId}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(request: Request, issueId: str):
    await asyncio.sleep(0.05)
    # for i in db:
    #     if i['id'] == issueId or i['key'] == issueId:
    #         db.remove(i)
    #         return Response(
    #             status_code=status.HTTP_204_NO_CONTENT,
    #             headers={
    #                 'Content-Type': 'application/json',
    #                 'Location': f'{request.url.path}'
    #             }
    #         )
    #
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(
                status_code=status.HTTP_204_NO_CONTENT,
                headers={
                    'Content-Type': 'application/json',
                    'Location': f'{request.url.path}'
                }
            )
