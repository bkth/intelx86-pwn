#!/bin/bash

# This script runs the binary on a TCP connection

echo 'starting server on localhost:4444'

socat tcp-l:4444,reuseaddr,fork exec:"./stage1"
