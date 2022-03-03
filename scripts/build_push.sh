#!/bin/bash

VERSION=$(head -n 1 VERSION | xargs echo -n)
TAG="ifrn-demo-${VERSION}"
IMAGE="docker.io/apahim/cloudy:${TAG}"

echo "Building ${IMAGE}..."
docker build -t "${IMAGE}" .

echo "Pushing ${IMAGE}..."
docker push "${IMAGE}"
