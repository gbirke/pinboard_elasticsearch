# This script converts a Pinboard API result into a bulk update for Elasticsearch

# Select posts
.posts

# Unwrap array into individual objects
| .[]

# Map boolean yes/no values (private, toread) to true booleans
| .shared = .shared == "yes"
| .toread = .toread == "yes"

# Generate a bulk object creation array - first entry is the create command,
# second entry is the document
| [
    { "index": { "_id" : .hash } },
    .
  ]

# Unwrap array into individual objects
| .[]
