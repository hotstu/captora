#!/usr/bin/env python
# Copyright (c) 2012-2021, Cenobit Technologies, Inc. http://cenobit.es/
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# * Neither the name of the Cenobit Technologies nor the names of
#    its contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
from flask import Flask
from typing import Any, Dict, List, Union, NoReturn, Optional
from numbers import Real

from flask_jsonrpc import JSONRPC
from capcha import load_sample, find_rect

# Flask application
app = Flask('application')


# Flask-JSONRPC
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)


@jsonrpc.method('App.index')
def index() -> str:
    return 'Welcome to Flask JSON-RPC'


@jsonrpc.method('App.welcome')
def welcome(name: str) -> str:
    return f'Welcome {name}'


@jsonrpc.method('cap.load')
def api_load(path: str) -> List[int]:
    sample = load_sample(path)
    return list(sample)


@jsonrpc.method('cap.find')
def api_find(
        path: str,
        target_w: int,
        target_h: int,
        thresold: Optional[Real] = .25,
        top_hint: Optional[int] = -1
) -> List[List[int]]:
    rect = find_rect(path, target_w, target_h, thresold, top_hint)
    return [list(n) for n in rect]


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)