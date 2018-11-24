# This script converts a Pinboard API result into a bulk update for Elasticsearch

# Select posts (if needed)
# This is to differentiate between
# https://api.pinboard.in/v1/posts/all (posts are flat array)
# and https://api.pinboard.in/v1/posts/get (posts are in JSON object)
if type == "array" then
  .
else
  .posts
end

# Unwrap array into individual objects
| .[]

# Map boolean yes/no values (private, toread) to true booleans
| .shared = .shared == "yes"
| .toread = .toread == "yes"

# Split tags
| .tags = ( .tags | split(" ") )

# Generate a bulk object creation array - first entry is the create command,
# second entry is the document
| [
    { "index": { "_id" : .hash } },
    .
  ]

# Unwrap array into individual objects
| .[]
