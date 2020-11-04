#!/bin/sh
CRAWLER="crawler"
CONVERTER="converter"
echo "- Starting Crawler.."
cd $CRAWLER
go build
./biocrawler
echo "- Crawling finished."
cd ../
echo "- Copying contents of $CRAWLER/output/ to $CONVERTER/input/"
cp -r "$CRAWLER/output/"* "$CONVERTER/input/"
echo "- Starting Converter.."
cd $CONVERTER/src
python3 main.py
echo "- Conversion Finished."
