#!/bin/bash
# Copyright (c) 2018 Spotify AB.
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# Exit on any non-zero status
set -e

# Install virtualenv
VIRTUALENV_LOCAL_PATH='/virtualenv-15.1.0/virtualenv.py'
VIRTUALENV_PATH=`python tools/vulcan/bin/vulcan.py -v -f tools/virtualenv.vulcan -p virtualenv-15.1.0`
VIRTUALENV_PATH=$VIRTUALENV_PATH$VIRTUALENV_LOCAL_PATH
$VIRTUALENV_PATH nfdriver_env
source nfdriver_env/bin/activate

# Install Python Packages
pip install pyyaml
pip install flake8
pip install cmakelint

# Execute our python build tools
if [ -n "$BUILD_IOS" ]; then
    python ci/ios.py "$@"
else
    if [ -n "$BUILD_ANDROID" ]; then
        python ci/android.py "$@"
    else
        python ci/osx.py "$@"
    fi
fi
