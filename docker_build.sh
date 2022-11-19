#!/usr/bin/env bash

set -ex
VERSION=$(git rev-parse --short HEAD)
docker build -f Dockerfile -t gcdd1993/ssl-check:latest -t gcdd1993/ssl-check:"$VERSION" .
docker push gcdd1993/ssl-check:latest
docker push gcdd1993/ssl-check:"$VERSION"
