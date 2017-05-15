#!/usr/bin/env bash

OSTYPE="$(uname -s)"

if [ "$(uname -m)" == "x86_64" ]; then
	BITS="64"
else
	BITS="32"
fi

if [ $OSTYPE == "Darwin" ]; then
	DRIVERNAME=chromedriver
	ARCHIVE=${DRIVERNAME}_mac${BITS}.zip
elif [ $OSTYPE == "Linux"]; then
	DRIVERNAME=chromedriver
	ARCHIVE=${DRIVERNAME}_linux${BITS}.zip
fi

curl -O https://chromedriver.storage.googleapis.com/2.29/${ARCHIVE}
unzip $ARCHIVE
mv $DRIVERNAME /usr/local/bin
rm $ARCHIVE

virtualenv healenv
source healenv/bin/activate
pip install -r requirements.txt
