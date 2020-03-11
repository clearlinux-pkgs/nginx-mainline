#!/bin/bash

KOJI=
if [ "$1" == "koji" ]; then
    KOJI=1
fi

for p in $(grep -Ev "#|include|^\$" ../../projects/clr-bundles/bundles/nginx-mainline-extras); do
    if [ $p == "nginx-mainline" ]; then
        continue;
    fi
    pushd ../$p
    make bump
    if [ -n "$KOJI" ]; then
        make koji
    fi
    popd
done
