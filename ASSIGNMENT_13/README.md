# Assignment 13 - Dynamic String Buffer in C

## Question
Implement a Dynamic String Buffer in C that automatically grows as needed.

### Requirements:

1. Create a \StringBuffer\ struct with:
   - \char *data\
   - \size_t length\
   - \size_t capacity\

2. \sb_init(size_t initial_capacity)\ â€” allocates struct and data buffer on heap; handle NULL from malloc

3. \sb_append(StringBuffer *sb, const char *str)\ â€” if new string exceeds capacity, use realloc to double it; handle realloc safely (don't overwrite original pointer if NULL)

4. \sb_free(StringBuffer *sb)\ â€” destructor that frees both internal data and the struct itself

### Demonstrate:
- Buffer growing at least twice
- All memory freed at the end

## Language
C

## Files
- \dynamic_string_buffer.c\
