# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
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


import os
import site
import json
from fnmatch import fnmatch
site_packages = site.getsitepackages()[-1]
steps_file = 'steps.json'
pattern = "*steps.json"


__version__ = '0.0.3'


# TODO: dynamic steps.json creation using Antlr for every function with :step: in its docstring
def create_steps(*,
        mode    = 'w',
        save    = steps_file,
        root    = site_packages,
        pattern = pattern):

    steps = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                file = os.path.join(path, name)
                with open(file) as steps_file:
                    try:
                        for project in json.load(steps_file):
                            steps.append(project)
                    except:
                        pass

    with open(save, mode) as fp:
        json.dump(steps, fp, indent=2)
    return steps
