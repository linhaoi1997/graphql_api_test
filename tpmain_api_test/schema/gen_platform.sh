python \
    -m sgqlc.introspection \
    --exclude-deprecated \
    --exclude-description \
    http://127.0.0.1:2001/graphql/ \
    platform_schema.json || exit 1

sgqlc-codegen schema platform_schema.json platform_schema.py;

