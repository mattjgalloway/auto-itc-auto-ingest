# auto-itc-auto-ingest

## Introduction

`auto-itc-auto-ingest` is a tool designed to be run as a cron to automatically run the iTunes Connect 
auto ingest tool to download missing daily and weekly reports.

## License

auto-itc-auto-ingest uses the 2-clause BSD license. So you should be free to use it pretty much however 
you want. Contact me if you require further information.

Copyright (c) 2011 Matt Galloway. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

## Author

`auto-itc-auto-ingest` is written and maintained by Matt Galloway <http://iphone.galloway.me.uk>.

## How to use

 1. Create your own `config.cfg` file by copying `example.cfg` and editing to suit your requirements. 
    All you really need to edit is the `creds` section by enterring your iTunes Connect credentials.
    
 1. Create your reports directory exists (it defaults to a folder called `reports` in the base 
    directory of the script).
    
 1. Download the `Autoingestion.class` Java class from Apple.
 
 1. Run the `ingest.py` script and it will download your reports! Set this on a cron and you're good 
    to go.
