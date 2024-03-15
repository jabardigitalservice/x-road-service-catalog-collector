#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from os import getenv

from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from . import META_DATA, SUMMARY


class RestfulApi:
    @staticmethod
    def app() -> FastAPI:
        RESTFUL_API_PATH: str = getenv('RESTFUL_API_PATH', '/')

        if RESTFUL_API_PATH.endswith('/'):
            RESTFUL_API_PATH = RESTFUL_API_PATH[:-1]

        api: FastAPI = FastAPI(
            title=SUMMARY,
            version=META_DATA['Version'],
            contact=dict(
                name=META_DATA['Author'],
                url=META_DATA['Home-page'],
                email=META_DATA['Author-email']
            ),
            license_info=dict(
                name=META_DATA['License'],
                identifier=META_DATA['License'],
                url=f"{META_DATA['Home-page']}/blob/main/LICENSE"
            ),
            docs_url=f'{RESTFUL_API_PATH}/',
            redoc_url=f'{RESTFUL_API_PATH}/redoc',
            openapi_url=f'{RESTFUL_API_PATH}/openapi.json'
        )
        api.add_middleware(
            CORSMiddleware,
            allow_origins=[
                'http://0.0.0.0',
                'http://localhost',
                'http://localhost:8080'
            ],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
        router = APIRouter()

        @router.post('/')
        async def hello_world():
            return 'Hello World!'

        api.include_router(router, prefix=RESTFUL_API_PATH)
        return api

    @staticmethod
    def run(
        host: str = '0.0.0.0', port: int = 80, reload: bool = False
    ):
        'RESTful API'

        uvicorn.run(
            f'{__name__}:RestfulApi.app',
            host=host,
            port=port,
            reload=reload,
            factory=True
        )  # pragma: no cover
