#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

import unittest

from fastapi.testclient import TestClient
from httpx import Response

from xroadservicecatalogcollector.restful_api import RestfulApi


class TestRestfulApi(unittest.TestCase):
    def __init__(self, methodName: str = 'runTest'):
        super().__init__(methodName)
        self.maxDiff = None

    def test_app(self):
        client: TestClient = TestClient(RestfulApi.app())
        response: Response = client.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Hello World!')
