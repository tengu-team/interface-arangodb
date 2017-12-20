# !/usr/bin/env python3
# Copyright (C) 2017  Qrama
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# pylint: disable=c0111,c0301,c0325, r0903,w0406

from charms.reactive import scopes, hook, RelationBase

class ArangoDBPeers(RelationBase):
    scope = scopes.UNIT

    @hook('{peers:arangodb}-relation-joined')
    def peer_joined(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.departed')
        conv.set_state('{relation_name}.connected')

    @hook('{peers:arangodb}-relation-departed')
    def peers_departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.connected')
        conv.set_state('{relation_name}.departed')

    def dismiss(self):
        '''Remove the departing state from all other units in the conversation,
        and we can resume normal operation.
        '''
        for conv in self.conversations():
            conv.remove_state('{relation_name}.departed')

    def get_peer_addresses(self):
        addresses = []
        for conversation in self.conversations():
            addresses.append(conversation.get_remote('private-address'))
        return addresses
