#!/usr/bin/python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes

from charmhelpers.core import hookenv


class JujuInfoClient(RelationBase):
    scope = scopes.GLOBAL
    
    auto_accessors = ['private-address']

    @hook('{requires:etcd}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.connected')
        self.set_state('{relation_name}.available')

    @hook('{requires:etcd}-relation-{broken, departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')
        self.remove_state('{relation_name}.connected')


