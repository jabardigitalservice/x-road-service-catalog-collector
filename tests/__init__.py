#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

import unittest

from click.testing import Result
from typer.testing import CliRunner

from xroadservicecatalogcollector.__main__ import cli
from xroadservicecatalogcollector.restful_api import RestfulApi


URL: str = 'https://bjb-security-server.access.digitalservice.id'
QUERY_ID: str = 'XROAD-DISKOMINFO-JABAR-d60266d4-f4d6-4ef9-b3ab-90f8c4196282'
X_ROAD_INSTANCE: str = 'XROAD-DISKOMINFO-JABAR'
MEMBER_CLASS: str = 'FIN'
MEMBER_CODE: str = 'bjb'
SUBSYSTEM_CODE: str = 'QRIS'


class TestAsicVerifier(unittest.TestCase):
    def __init__(self, methodName: str = 'runTest'):
        super().__init__(methodName)
        self.maxDiff = None

    def test_main(self):
        result: Result = CliRunner().invoke(cli, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(RestfulApi.run.__doc__, result.stdout)
