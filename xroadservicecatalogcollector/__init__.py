#!/usr/bin/env python3

# Copyright (C) Free Software Foundation, Inc. All rights reserved.
# Licensed under the AGPL-3.0-only License. See LICENSE in the project root
# for license information.

from dotenv import load_dotenv
from importlib_metadata import PackageMetadata, metadata

load_dotenv()
META_DATA: PackageMetadata = metadata(__name__)
SUMMARY: str = META_DATA['Summary']
