#!/bin/bash

set -e

echo "🚀 Building portfolio..."

GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "${BLUE}🧱 Generating pages...${NC}"
python3 scripts/build_site.py

if [ ! -d "node_modules" ]; then
    echo "${BLUE}📦 Installing dependencies...${NC}"
    npm install
fi

echo "${BLUE}🎨 Minifying CSS...${NC}"
npx clean-css-cli -o css/styles.min.css css/styles.css
echo "${GREEN}✓ CSS minified: css/styles.min.css${NC}"

echo "${BLUE}📜 Minifying JavaScript...${NC}"
npx terser css/script.js -o css/script.min.js -c -m
echo "${GREEN}✓ JS minified: css/script.min.js${NC}"

echo ""
echo "${BLUE}📊 File sizes:${NC}"
echo "CSS original: $(wc -c < css/styles.css | awk '{print int($1/1024)"KB"}')"
echo "CSS minified: $(wc -c < css/styles.min.css | awk '{print int($1/1024)"KB"}')"
echo "JS original:  $(wc -c < css/script.js | awk '{print int($1/1024)"KB"}')"
echo "JS minified:  $(wc -c < css/script.min.js | awk '{print int($1/1024)"KB"}')"

echo ""
echo "${GREEN}✨ Build complete!${NC}"
echo ""
