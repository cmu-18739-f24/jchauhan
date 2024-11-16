#!/bin/bash

set -e

socat tcp-listen:5555,reuseaddr,fork SYSTEM:"./format_vuln"